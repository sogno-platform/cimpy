import os
import importlib
import chevron
from datetime import datetime
from enum import Enum
import copy


# ToDo: support readInProfile and possibleProfileList for export
# ToDo: revise structure
# ToDo: comment code
# ToDo: use logger errors for errors

# Input Object dictionary
def _create_package_classes_dict(res):
    package_classes_dict = {}
    for key in res.keys():
        # objects of type: cimpy.cimversion.package_name.file_name.class_name
        package = str(type(res[key])).split('.')[2]
        class_name = str(type(res[key])).split('.')[-1]
        class_name = class_name.split("'")[0]
        if package not in package_classes_dict.keys():
            package_classes_dict[package] = []
            package_classes_dict[package].append({class_name: res[key], 'mRID': key})
        else:
            package_classes_dict[package].append({class_name: res[key], 'mRID': key})
    return package_classes_dict


# ToDo: comment
def _get_class_attributes_with_references(res, version):
    class_attributes_dict = {}
    class_attributes_list = []

    for key in res.keys():
        class_dict = dict(name=res[key].__class__.__name__)
        class_dict['mRID'] = key
        # array containing all attributes, attribute references to objects
        attributes_dict = _get_attributes(res[key])
        print(key)
        # change attribute references to mRID of the object, res needed because classes like SvPowerFlow does not have
        # mRID as an attribute. Therefore the corresponding class has to be searched in the res dictionary
        class_dict['attributes'] = _get_reference_uuid(attributes_dict, version, res)
        class_attributes_list.append(class_dict)
        del class_dict

    return class_attributes_list


# Input Attributes Dictionary
# ToDo: comment code
def _get_reference_uuid(attr_dict, version, res):
    reference_list = []
    base_class_name = 'cimpy.' + version + '.Base'
    base_module = importlib.import_module(base_class_name)
    base_class = getattr(base_module, 'Base')
    for key in attr_dict:
        if key in ['readInProfile', 'possibleProfileList']:
            reference_list.append({key: attr_dict[key]})
            continue

        attributes = {}
        if isinstance(attr_dict[key], list):
            array = []
            for elem in attr_dict[key]:
                if issubclass(type(elem), base_class):
                    if not hasattr(elem, 'mRID'):
                        UUID = '%' + _search_mRID(elem, res)
                        if UUID == '%':
                            # ToDo: logger error
                            continue
                    else:
                        UUID = '%' + elem.mRID

                    array.append(UUID)
                    # resource = key + ' rdf:resource='
                    # reference_dict[resource] = array
                else:
                    # ToDo: log error
                    print('Error!')
            if len(array) == 1:
                attributes['value'] = array[0]
            else:
                attributes['value'] = array
        elif issubclass(type(attr_dict[key]), base_class):
            # resource = key + ' rdf:resource='
            if not hasattr(attr_dict[key], 'mRID'):
                UUID = '%' + _search_mRID(attr_dict[key], res)
                if UUID == '%':
                    # ToDo: logger error
                    continue
            else:
                UUID = '%' + attr_dict[key].mRID
            attributes['value'] = UUID
        elif attr_dict[key] == "" or attr_dict[key] is None:
            # ToDo: check if needed
            pass
        else:
            # reference_dict[key] = attr_dict[key]
            attributes['value'] = attr_dict[key]

        attributes['attr_name'] = key
        if 'value' in attributes.keys():
            if isinstance(attributes['value'], list):
                # ToDo: check if needed, why should the list contain non UUID entries
                for reference_item in attributes['value']:
                    if reference_item not in ['', None, 0.0]:
                        reference_list.append({'value': reference_item, 'attr_name': key})
            elif attributes['value'] not in ['', None, 0.0, 0]:
                reference_list.append(attributes)

    return reference_list


# ToDO: comment
def _search_mRID(class_object, res):
    for mRID, class_obj in res.items():
        if class_object == class_obj:
            return mRID
    return ""


# ToDo: comment
def _set_attribute_or_reference(text, render):
    result = render(text)
    result = result.split('@')
    value = result[0]
    attr_name = result[1]
    if '%' in value:
        reference = value.split('%')[1]
        return ' rdf:resource="#' + reference + '"/>'
    else:
        return '>' + value + '</cim:' + attr_name + '>'


# ToDo: comment
def _set_attribute_or_reference_model(text, render):
    result = render(text)
    result = result.split('@')
    value = result[0]
    attr_name = result[1]
    if '%' in value:
        reference = value.split('%')[1]
        return ' rdf:resource="' + reference + '"/>'
    else:
        return '>' + value + '</md:Model.' + attr_name + '>'


# ToDo: comment
def _create_namespaces_list(namespaces_dict):
    namespaces_list = []

    for key in namespaces_dict:
        namespace = {}
        namespace['key'] = key
        namespace['url'] = namespaces_dict[key]
        namespaces_list.append(namespace)

    return namespaces_list


# ToDo: comment!!
def _sort_classes_to_package(class_attributes_list):
    export_dict = {}
    export_about_dict = {}

    # iterate over classes
    for klass in class_attributes_list:
        same_package_list = []
        about_dict = {}

        readInProfile = klass['attributes'][0]['readInProfile']
        possibleProfileList = klass['attributes'][1]['possibleProfileList']

        class_origin = ''
        if klass['name'] in readInProfile.keys():
            if 'class' in readInProfile[klass['name']].keys():
                class_origin = readInProfile[klass['name']]['class']

        if class_origin == '':
            if klass['name'] in possibleProfileList.keys():
                if 'class' in possibleProfileList[klass['name']].keys():
                    class_origin_default = min(possibleProfileList[klass['name']]['class'])
                    class_origin = cgmesProfile(class_origin_default).name
                else:
                    # ToDo: logger error
                    pass
            else:
                # ToDo: logger error
                pass

        # iterate over attributes
        for attribute in klass['attributes']:
            if 'attr_name' in attribute.keys():
                attribute_class = attribute['attr_name'].split('.')[0]
                attribute_name = attribute['attr_name'].split('.')[1]
                attribute_origin = ''

                # was the attribute read in or set?
                if attribute_class in readInProfile.keys():
                    if attribute_name in readInProfile[attribute_class].keys():
                        attribute_origin = readInProfile[attribute_class][attribute_name]

                if attribute_origin == '':
                    # attribute was not read in, therefore it is an added attribute, get origin from possibleProfileList
                    if attribute_class in possibleProfileList.keys():
                        if attribute_name in possibleProfileList[attribute_class].keys():
                            attribute_origin_default = min(possibleProfileList[attribute_class][attribute_name])
                            attribute_origin = cgmesProfile(attribute_origin_default).name
                        else:
                            # ToDo: logger error
                            pass
                    else:
                        # ToDo: logger error:
                        pass

                if attribute_origin == class_origin:
                    same_package_list.append(attribute)
                else:
                    if attribute_origin in about_dict.keys():
                        about_dict[attribute_origin].append(attribute)
                    else:
                        about_dict[attribute_origin] = [attribute]

        if class_origin in export_dict.keys():
            export_class = dict(name=klass['name'], mRID=klass['mRID'], attributes=same_package_list)
            export_dict[class_origin]['classes'].append(export_class)
            del export_class
        else:
            export_class = dict(name=klass['name'], mRID=klass['mRID'], attributes=same_package_list)
            export_dict[class_origin] = {'classes': [export_class]}

        for about_key in about_dict.keys():
            if about_key in export_about_dict.keys():
                export_about_class = dict(name=klass['name'], mRID=klass['mRID'], attributes=about_dict[about_key])
                export_about_dict[about_key]['classes'].append(export_about_class)
            else:
                export_about_class = dict(name=klass['name'], mRID=klass['mRID'], attributes=about_dict[about_key])
                export_about_dict[about_key] = {'classes': [export_about_class]}

    return export_dict, export_about_dict


def cim_export(res, namespaces_dict, file_name, version):
    """Function for serialization of cgmes classes

    This function serializes cgmes classes with the template engine chevron. The classes are separated by their package
    and one xml file for each package is created. The package name is added after the file name. The
    set_attributes_or_reference function is a lamda function for chevron to decide whether the value of an attribute is
    a reference to another class object or not.

    :param res: a dictionary containing the cgmes classes accessible via the mRID
    :param namespaces_dict: a dictionary containing the RDF namespaces used in the imported xml files
    :param file_name: a string with the name of the xml files which will be created
    :param version: cgmes version, e.g. version = "cgmes_v2_4_15"
    """
    # package_classes_dict = _create_package_classes_dict(res)
    export_dict = {}
    cwd = os.getcwd()
    os.chdir(os.path.dirname(__file__))

    class_attributes_list = _get_class_attributes_with_references(res, version)

    export_dict, about_dict = _sort_classes_to_package(class_attributes_list)

    # ToDo: export_dict and about_dict should be complete. check if correct
    # ToDo: process dicts to write python files

    about_list = []
    # Iterate over objects in res
    # for key in res.keys():
    #     export_dict[key], about_dict = _get_class_attributes(res[key], version)
    #     about_list.append(about_dict)

    new_export_dict = {}
    for key in export_dict.keys():
        new_export_dict[key] = {}
        new_export_dict[key]['classes'] = export_dict[key]

    for about_dict in about_list:
        for about_key in about_dict.keys():
            if about_key in new_export_dict.keys():
                if 'about' in new_export_dict[about_key].keys():
                    new_export_dict[about_key]['about'].append(about_dict[about_key])
                else:
                    new_export_dict[about_key]['about'] = about_dict[about_key]
            else:
                new_export_dict[about_key] = {'about': about_dict[about_key]}

    namespaces_list = _create_namespaces_list(namespaces_dict)

    created = {'attr_name': 'created', 'value': datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
    authority = {'attr_name': 'modelingAuthoritySet', 'value': 'www.acs.eonerc.rwth-aachen.de'}

    for key in new_export_dict.keys():
        model_name = {'mRID': file_name, 'description': []}
        model_description = {'model': [model_name]}
        model_description['model'][0]['description'].append(created)
        model_description['model'][0]['description'].append(authority)

        if 'classes' in new_export_dict[key].keys():
            classes = new_export_dict[key]['classes']
        else:
            classes = False

        if 'about' in new_export_dict[key].keys():
            about = new_export_dict[key]['about']
        else:
            about = False

        full_file_name = file_name + '_' + key + '.xml'

        full_path = os.path.join(cwd, full_file_name)

        profile = {'attr_name': 'profile', 'value': key}
        model_description['model'][0]['description'].append(profile)

        if not os.path.exists(full_path):
            with open(full_path, 'w') as file:
                with open('export_template.mustache') as f:
                    output = chevron.render(f, {"classes": classes,
                                                "about": about,
                                                "set_attributes_or_reference": _set_attribute_or_reference,
                                                "set_attributes_or_reference_model": _set_attribute_or_reference_model,
                                                "namespaces": namespaces_list,
                                                "model": model_description['model']})
                file.write(output)
        del model_description, model_name
    os.chdir(cwd)


def _get_attributes(class_object):
    # list containing all parent classes after while loop
    inheritance_list = [class_object]
    class_type = type(class_object)
    parent = class_object
    # get parent class, ignore base class (class without attributes)
    while 'Base.Base' not in str(class_type):
        parent = parent.__class__.__bases__[0]()
        # insert parent class at beginning of list, classes inherit from top to bottom
        inheritance_list.insert(0, parent)
        class_type = type(parent)

    # dictionary containing all attributes with key: 'Class_Name.Attribute_Name'
    attributes_dict = dict(readInProfile={}, possibleProfileList={})
    # __dict__ of a subclass returns also the attributes of the parent classes
    # to avoid multiple attributes create list with all attributes already processed
    attributes_list = []

    for parent_class in inheritance_list:
        # get all attributes of the current parent class
        parent_attributes_dict = parent_class.__dict__
        class_name = parent_class.__class__.__name__
        for key in parent_attributes_dict.keys():
            if key not in attributes_list:
                attributes_list.append(key)
                attributes_name = class_name + '.' + key
                attributes_dict[attributes_name] = getattr(class_object, key)
            else:
                continue

        if class_name is not 'Base':
            attributes_dict['readInProfile'][class_name] = parent_class.readInProfile
            attributes_dict['possibleProfileList'][class_name] = parent_class.possibleProfileList

    return attributes_dict


# ToDo: comment
short_package_name = {
    "DiagramLayout": 'DI',
    "Dynamics": "DY",
    "Equipment": "EQ",
    "GeographicalLocation": "GL",
    "StateVariables": "SV",
    "SteadyStateHypothesis": "SSH",
    "Topology": "TP"
}

cgmesProfile = Enum("cgmesProfile", {"EQ": 0, "SSH": 1, "TP": 2, "SV": 3, "DY": 4, "GL": 5, "DI": 6})