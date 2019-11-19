import os
import importlib
import chevron
from datetime import datetime
import copy


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


# Input class dictionary
def _get_class_attributes(object_list, version):
    i = 0
    print_list = []
    about_dict = {}
    for elem in object_list:
        for key in elem.keys():
            if key == "mRID":
                continue
            hit_dict = {}
            no_hit_dict = {}
            class_attributes = _get_attributes(elem[key])
            class_attributes_with_references, mRID = _get_reference_uuid(class_attributes, version)

            if mRID == '':
                mRID = elem['mRID']

            hit_dict['mRID'] = mRID
            hit_dict['name'] = key
            no_hit_dict['mRID'] = mRID
            no_hit_dict['name'] = key

            no_hit_list = class_attributes_with_references
            # cyclic references like TransformerEnd <-> PowerTransformer both in output file
            search_class = elem[key]
            while search_class.__class__.__name__ != 'Base':
                no_hit_copy = no_hit_list
                if hasattr(search_class, 'reference_dict'):
                    no_hit_list = []
                    for attr_elem in no_hit_copy:
                        hit = False
                        for package, value in search_class.reference_dict.items():
                            package_name = package.split('Version')[0]
                            if attr_elem['attr_name'].split('.')[1] in value:
                                hit = True
                                # hit_list.append(attr_elem)
                                hit_dict['attributes'] = attr_elem
                                if package_name in about_dict.keys():
                                    hit_copy = copy.deepcopy(hit_dict)
                                    about_dict[package_name].append(hit_copy)
                                else:
                                    hit_copy = copy.deepcopy(hit_dict)
                                    about_dict[package_name] = [hit_copy]
                                break
                        if not hit:
                            no_hit_list.append(attr_elem)
                if len(no_hit_list) == 0:
                    break
                search_class = search_class.__class__.__bases__[0]()

                # process about attributes
                # if len(hit_list) > 0:
                #     hit_dict['attributes'] = hit_list
                #     if package_name in about_dict.keys():
                #         about_dict[package_name].append(hit_dict)
                #     else:
                #         about_dict[package_name] = [hit_dict]

            if len(no_hit_list) > 0:
                # process other attributes
                no_hit_dict['attributes'] = no_hit_list
                print_list.append(no_hit_dict)

    return print_list, about_dict


# Input Attributes Dictionary
def _get_reference_uuid(attr_dict, version):
    reference_list = []
    base_class_name = 'cimpy.' + version + '.Base'
    base_module = importlib.import_module(base_class_name)
    base_class = getattr(base_module, 'Base')
    mRID = ''
    UUID = ''
    for key in attr_dict:
        attributes = {}
        if isinstance(attr_dict[key], list):
            array = []
            for elem in attr_dict[key]:
                if issubclass(type(elem), base_class):
                    UUID = '%' + elem.mRID
                    array.append(UUID)
                    # resource = key + ' rdf:resource='
                    # reference_dict[resource] = array
                else:
                    print('Error!')
            if len(array) == 1:
                attributes['value'] = array[0]
            else:
                attributes['value'] = array
        elif issubclass(type(attr_dict[key]), base_class):
            # resource = key + ' rdf:resource='
            UUID = '%' + attr_dict[key].mRID
            attributes['value'] = UUID
        elif key == 'IdentifiedObject.mRID':
            mRID = attr_dict[key]
        elif attr_dict[key] == "" or attr_dict[key] is None:
            pass
        else:
            # reference_dict[key] = attr_dict[key]
            attributes['value'] = attr_dict[key]

        attributes['attr_name'] = key
        if 'value' in attributes.keys():
            if isinstance(attributes['value'], list):
                for reference_item in attributes['value']:
                    if reference_item not in ['', None, 0.0]:
                        reference_list.append({'value': reference_item, 'attr_name': key})
            elif attributes['value'] not in ['', None, 0.0]:
                reference_list.append(attributes)

    return reference_list, mRID


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


def _create_namespaces_list(namespaces_dict):
    namespaces_list = []

    for key in namespaces_dict:
        namespace = {}
        namespace['key'] = key
        namespace['url'] = namespaces_dict[key]
        namespaces_list.append(namespace)

    return namespaces_list


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
    package_classes_dict = _create_package_classes_dict(res)
    export_dict = {}
    cwd = os.getcwd()
    os.chdir(os.path.dirname(__file__))

    about_list = []
    for key in package_classes_dict.keys():
        export_dict[key], about_dict = _get_class_attributes(package_classes_dict[key], version)
        about_list.append(about_dict)

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
    attributes_dict = {}
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

    return attributes_dict
