import os
import importlib
import chevron
from datetime import datetime
from time import time
from cimpy.cgmes_v2_4_15.Base import Profile
import logging
import sys
from cimpy.cgmes_v2_4_15.Base import Base
cgmesProfile = Base.cgmesProfile
from pathlib import Path
import copy

logger = logging.getLogger(__name__)


# This function gets all attributes of an object and resolves references to other objects
def _get_class_attributes_with_references(import_result, version):
    class_attributes_list = []
    # extract topology and urls
    topology = import_result['topology']
    urls = import_result['meta_info']['urls']
    for key in topology.keys():
        class_dict = dict(name=topology[key].__class__.__name__)
        class_dict['mRID'] = key
        # array containing all attributes, attribute references to objects
        attributes_dict = _get_attributes(topology[key])
        # change attribute references to mRID of the object, res needed because classes like SvPowerFlow does not have
        # mRID as an attribute. Therefore the corresponding class has to be searched in the res dictionary
        class_dict['attributes'] = _get_reference_uuid(attributes_dict, version, topology, key, urls)
        class_attributes_list.append(class_dict)
        del class_dict

    return class_attributes_list


# This function resolves references to objects
def _get_reference_uuid(attr_dict, version, topology, mRID, urls):
    reference_list = []
    base_class_name = 'cimpy.' + version + '.Base'
    base_module = importlib.import_module(base_class_name)
    base_class = getattr(base_module, 'Base')
    for key in attr_dict:
        if key in ['serializationProfile', 'possibleProfileList']:
            reference_list.append({key: attr_dict[key]})
            continue

        attributes = {}
        if isinstance(attr_dict[key], list):  # many
            array = []
            for elem in attr_dict[key]:
                if issubclass(type(elem), base_class):
                    # classes like SvVoltage does not have an attribute called mRID, the mRID is only stored as a key
                    # for this object in the res dictionary
                    # The % added before the mRID is used in the lambda _set_attribute_or_reference
                    if not hasattr(elem, 'mRID'):
                        # search for the object in the res dictionary and return the mRID
                        UUID = '%' + _search_mRID(elem, topology)
                        if UUID == '%':
                            logger.warning('Object of type {} not found as reference for object with UUID {}.'.format(
                                elem.__class__.__name__, mRID))
                    else:
                        UUID = '%' + elem.mRID

                    array.append(UUID)
                else:
                    logger.warning('Reference object not subclass of Base class for object with UUID {}.'.format(mRID))
            if len(array) == 1:
                attributes['value'] = array[0]
            else:
                attributes['value'] = array
        elif issubclass(type(attr_dict[key]), base_class):  # 0..1, 1..1
            # resource = key + ' rdf:resource='
            if not hasattr(attr_dict[key], 'mRID'):
                # search for object in res dict and return mRID
                # The % added before the mRID is used in the lambda _set_attribute_or_reference
                UUID = '%' + _search_mRID(attr_dict[key], topology)
                if UUID == '%':
                    logger.warning('Object of type {} not found as reference for object with UUID {}.'.format(
                        attr_dict[key].__class__.__name__, mRID))
            else:
                UUID = '%' + attr_dict[key].mRID
            attributes['value'] = UUID
        elif attr_dict[key] == "" or attr_dict[key] is None:
            pass
        else:
            # attribute in urls dict?
            if key.split('.')[1] in urls.keys():
                # value in urls dict? should always be true
                if attr_dict[key] in urls[key.split('.')[1]].keys():
                    attributes['value'] = '%URL%' + urls[key.split('.')[1]][attr_dict[key]]
                else:
                    logger.warning('URL reference for attribute {} and value {} not found!'.format(
                        key.split('.')[1], attr_dict[key]))
            else:
                attributes['value'] = attr_dict[key]

        attributes['attr_name'] = key
        if 'value' in attributes.keys():
            if isinstance(attributes['value'], list):
                for reference_item in attributes['value']:
                    # ignore default values
                    if reference_item not in ['', None, 0.0, 0]:
                        reference_list.append({'value': reference_item, 'attr_name': key})
            # ignore default values
            elif attributes['value'] not in ['', None, 0.0, 0, 'list']:
                reference_list.append(attributes)

    return reference_list


# This function searches a class_object in the res dictionary and returns the corresponding key (the mRID). Necessary
# for classes without mRID as attribute like SvVoltage
def _search_mRID(class_object, topology):
    for mRID, class_obj in topology.items():
        if class_object == class_obj:
            return mRID
    return ""


# Lambda function for chevron renderer to decide whether the current element is a reference or an attribute
def _set_attribute_or_reference(text, render):
    result = render(text)
    result = result.split('@')
    value = result[0]
    attr_name = result[1]
    if '%URL%' in value:
        reference = value.split('%')[2]
        return ' rdf:resource="' + reference + '"/>'
    elif '%' in value:
        reference = value.split('%')[1]
        return ' rdf:resource="#' + reference + '"/>'
    else:
        return '>' + value + '</cim:' + attr_name + '>'


# Lambda function for chevron renderer to set an attribute or a reference in the model description.
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


# Restructures the namespaces dict into a list. The template engine writes each entry in the RDF header
def _create_namespaces_list(namespaces_dict):
    namespaces_list = []

    for key in namespaces_dict:
        namespace = dict(key=key, url=namespaces_dict[key])
        namespaces_list.append(namespace)

    return namespaces_list


# This function sorts the classes and their attributes to the corresponding profiles. Either the classes/attributes are
# imported or they are set afterwards. In the first case the serializationProfile is used to determine from which
# profile this class/attribute was read. If an entry exists the class/attribute is added to this profile. In the
# possibleProfileList dictionary the possible origins of the class/attributes is stored. All profiles have a different
# priority which is stored in the enum cgmesProfile. As default the smallest entry in the dictionary is used to
# determine the profile for the class/attributes.
def _sort_classes_to_profile(class_attributes_list, activeProfileList):
    export_dict = {}
    export_about_dict = {}

    # iterate over classes
    for klass in class_attributes_list:
        same_package_list = []
        about_dict = {}

        # store serializationProfile and possibleProfileList
        # serializationProfile class attribute, same for multiple instances of same class, only last origin of variable stored
        serializationProfile = copy.deepcopy(klass['attributes'][0]['serializationProfile'])
        possibleProfileList = copy.deepcopy(klass['attributes'][1]['possibleProfileList'])

        class_serializationProfile = ''

        if 'class' in serializationProfile.keys():
            # class was imported
            if Profile[serializationProfile['class']] in activeProfileList:
                # else: class origin profile not active for export, get active profile from possibleProfileList
                if Profile[serializationProfile['class']].value in possibleProfileList[klass['name']]['class']:
                    # profile active and in possibleProfileList
                    # else: class should not have been imported from this profile, get allowed profile
                    # from possibleProfileList
                    class_serializationProfile = serializationProfile['class']
                else:
                    logger.warning('Class {} was read from profile {} but this profile is not possible for this class'
                                   .format(klass['name'], serializationProfile['class']))
            else:
                logger.info('Class {} was read from profile {} but this profile is not active for the export. Use'
                            'default profile from possibleProfileList.'.format(klass['name'], serializationProfile['class']))

        if class_serializationProfile == '':
            # class was created
            if klass['name'] in possibleProfileList.keys():
                if 'class' in possibleProfileList[klass['name']].keys():
                    possibleProfileList[klass['name']]['class'].sort()
                    for klass_profile in possibleProfileList[klass['name']]['class']:
                        if Profile(klass_profile).name in activeProfileList:
                            # active profile for class export found
                            class_serializationProfile = Profile(klass_profile).name
                            break
                    if class_serializationProfile == '':
                        # no profile in possibleProfileList active
                        logger.warning('All possible export profiles for class {} not active. Skip class for export.'
                                       .format(klass['name']))
                        continue
                else:
                    logger.warning('Class {} has no profile to export to.'.format(klass['name']))
            else:
                logger.warning('Class {} has no profile to export to.'.format(klass['name']))

        # iterate over attributes
        for attribute in klass['attributes']:
            if 'attr_name' in attribute.keys():
                attribute_class = attribute['attr_name'].split('.')[0]
                attribute_name = attribute['attr_name'].split('.')[1]

                # IdentifiedObject.mRID is not exported as an attribute
                if attribute_name == 'mRID':
                    continue

                attribute_serializationProfile = ''

                if attribute_name in serializationProfile.keys():
                    # attribute was imported
                    if Profile[serializationProfile[attribute_name]] in activeProfileList:
                        attr_value = Profile[serializationProfile[attribute_name]].value
                        if attr_value in possibleProfileList[attribute_class][attribute_name]:
                            attribute_serializationProfile = serializationProfile[attribute_name]

                if attribute_serializationProfile == '':
                    # attribute was added
                    if attribute_class in possibleProfileList.keys():
                        if attribute_name in possibleProfileList[attribute_class].keys():
                            possibleProfileList[attribute_class][attribute_name].sort()
                            for attr_profile in possibleProfileList[attribute_class][attribute_name]:
                                if Profile(attr_profile) in activeProfileList:
                                    # active profile for class export found
                                    attribute_serializationProfile = Profile(attr_profile).name
                                    break
                            if attribute_serializationProfile == '':
                                # no profile in possibleProfileList active, skip attribute
                                logger.warning('All possible export profiles for attribute {}.{} of class {} '
                                               'not active. Skip attribute for export.'
                                               .format(attribute_class, attribute_name, klass['name']))
                                continue
                        else:
                            logger.warning('Attribute {}.{} of class {} has no profile to export to.'.
                                           format(attribute_class, attribute_name, klass['name']))
                    else:
                        logger.warning('The class {} for attribute {} is not in the possibleProfileList'.format(
                            attribute_class, attribute_name))

                if attribute_serializationProfile == class_serializationProfile:
                    # class and current attribute belong to same profile
                    same_package_list.append(attribute)
                else:
                    # class and current attribute does not belong to same profile -> rdf:about in
                    # attribute origin profile
                    if attribute_serializationProfile in about_dict.keys():
                        about_dict[attribute_serializationProfile].append(attribute)
                    else:
                        about_dict[attribute_serializationProfile] = [attribute]

        # add class with all attributes in the same profile to the export dict sorted by the profile
        if class_serializationProfile in export_dict.keys():
            export_class = dict(name=klass['name'], mRID=klass['mRID'], attributes=same_package_list)
            export_dict[class_serializationProfile]['classes'].append(export_class)
            del export_class
        else:
            export_class = dict(name=klass['name'], mRID=klass['mRID'], attributes=same_package_list)
            export_dict[class_serializationProfile] = {'classes': [export_class]}

        # add class with all attributes defined in another profile to the about_key sorted by the profile
        for about_key in about_dict.keys():
            if about_key in export_about_dict.keys():
                export_about_class = dict(name=klass['name'], mRID=klass['mRID'], attributes=about_dict[about_key])
                export_about_dict[about_key]['classes'].append(export_about_class)
            else:
                export_about_class = dict(name=klass['name'], mRID=klass['mRID'], attributes=about_dict[about_key])
                export_about_dict[about_key] = {'classes': [export_about_class]}

    return export_dict, export_about_dict


def cim_export(import_result, file_name, version, activeProfileList):
    """Function for serialization of cgmes classes

    This function serializes cgmes classes with the template engine chevron. The classes are separated by their profile
    and one xml file for each profile is created. The package name is added after the file name. The
    set_attributes_or_reference function is a lamda function for chevron to decide whether the value of an attribute is
    a reference to another class object or not.

    :param import_result: a dictionary containing the topology and meta information. The topology can be extracted via \
    :func:`~cimpy.cimimport.cim_import()`. The topology dictionary contains all objects accessible via their mRID. The meta \
    information can be extracted via import_result['meta_info']. The meta_info dictionary contains a new dictionary with \
    the keys: 'author', 'namespaces' and 'urls'. The last two are also dictionaries. 'urls' contains a mapping \
    between references to URLs and the extracted value of the URL, e.g. 'absoluteValue': \
    'http://iec.ch/TC57/2012/CIM-schema-cim16#OperationalLimitDirectionKind.absoluteValue' These mappings are accessible \
    via the name of the attribute, e.g. import_result['meta_info']['urls'}[attr_name] = {mapping like example above}. \
    'namespaces' is a dictionary containing all RDF namespaces used in the imported xml files.
    :param file_name: a string with the name of the xml files which will be created
    :param version: cgmes version, e.g. version = "cgmes_v2_4_15"
    :param activeProfileList: a list containing the strings of all short names of the profiles used for serialization
    """

    t0 = time()
    logger.info('Start export procedure.')

    profile_list = list(map(lambda a: Profile[a], activeProfileList))

    # iterate over all profiles
    for profile in profile_list:

        # File name
        full_file_name = file_name + '_' + profile.long_name() + '.xml'

        if not os.path.exists(full_file_name):
            output = generate_xml(import_result, version, file_name, profile, profile_list)

            with open(full_file_name, 'w') as file:
                logger.info('Write file \"%s\"', full_file_name)

                file.write(output)
        else:
            logger.error('File {} already exists. Delete file or change file name to serialize CGMES '
                           'classes.'.format(full_file_name))
            print('[ERROR:] File {} already exists. Delete file or change file name to serialize CGMES '
                           'classes.'.format(full_file_name), file=sys.stderr)
            exit(-1)

    logger.info('End export procedure. Elapsed time: {}'.format(time() - t0))


def generate_xml(cim_data, version, model_name, profile, available_profiles):
    """Function for serialization of cgmes classes

    This function serializes cgmes classes with the template engine chevron and returns them as a string.

    :param cim_data: a dictionary containing the topology and meta information. It can be created via :func:`~cimpy.cimimport.cim_import()`
    :param version: cgmes version, e.g.  ``version="cgmes_v2_4_15"``
    :param profile: The :class:`~cimpy.cgmes_v2_4_15.Base.Profile` for which the serialization should be generated.
    :param model_name: a string with the name of the model.
    :param available_profiles: a list of all :class:`~cimpy.cgmes_v2_4_15.Base.Profile`s in `cim_data`
    """

    # returns all classes with their attributes and resolved references
    class_attributes_list = _get_class_attributes_with_references(
        cim_data, version)

    # determine class and attribute export profiles. The export dict contains all classes and their attributes where
    # the class definition and the attribute definitions are in the same profile. Every entry in about_dict generates
    # a rdf:about in another profile
    export_dict, about_dict = _sort_classes_to_profile(
        class_attributes_list, available_profiles)

    namespaces_list = _create_namespaces_list(
        cim_data['meta_info']['namespaces'])

    if profile.name not in export_dict.keys() and profile.name not in about_dict.keys():
        raise RuntimeError("Profile " + profile.name + " not available for export, export_dict=" + str(export_dict.keys()) + ' and about_dict='+ str(about_dict.keys()) + '.')

    # extract class lists from export_dict and about_dict
    if profile.name in export_dict.keys():
        classes = export_dict[profile.name]['classes']
    else:
        classes = False

    if profile.name in about_dict.keys():
        about = about_dict[profile.name]['classes']
    else:
        about = False

    #Model header
    model_description = {
        'mRID': model_name,
        'description': [
            {'attr_name': 'created', 'value': datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S")},
            {'attr_name': 'modelingAuthoritySet',
             'value': 'www.acs.eonerc.rwth-aachen.de'},
            {'attr_name': 'profile',
             'value': profile.long_name()}
        ]
    }
    template_path = Path(os.path.join(os.path.dirname(__file__), 'export_template.mustache')).resolve()
    with open(template_path) as f:
        output = chevron.render(f, {"classes": classes,
                                    "about": about,
                                    "set_attributes_or_reference": _set_attribute_or_reference,
                                    "set_attributes_or_reference_model": _set_attribute_or_reference_model,
                                    "namespaces": namespaces_list,
                                    "model": [model_description]})
    del model_description
    return output

# This function extracts all attributes from class_object in the form of Class_Name.Attribute_Name
def _get_attributes(class_object):
    inheritance_list = [class_object]
    class_type = type(class_object)
    parent = class_object

    # get parent classes
    while 'Base.Base' not in str(class_type):
        parent = parent.__class__.__bases__[0]()
        # insert parent class at beginning of list, classes inherit from top to bottom
        inheritance_list.insert(0, parent)
        class_type = type(parent)

    # dictionary containing all attributes with key: 'Class_Name.Attribute_Name'
    attributes_dict = dict(serializationProfile=class_object.serializationProfile, possibleProfileList={})

    # __dict__ of a subclass returns also the attributes of the parent classes
    # to avoid multiple attributes create list with all attributes already processed
    attributes_list = []

    # iterate over parent classes from top to bottom
    for parent_class in inheritance_list:
        # get all attributes of the current parent class
        parent_attributes_dict = parent_class.__dict__
        class_name = parent_class.__class__.__name__

        # check if new attribute or old attribute
        for key in parent_attributes_dict.keys():
            if key not in attributes_list:
                attributes_list.append(key)
                attributes_name = class_name + '.' + key
                attributes_dict[attributes_name] = getattr(class_object, key)
            else:
                continue

        # get all possibleProfileLists from all parent classes except the Base class (no attributes)
        # the serializationProfile from parent classes is not needed because entries in the serializationProfile
        # are only generated for the inherited class
        if class_name != 'Base':
            attributes_dict['possibleProfileList'][class_name] = parent_class.possibleProfileList

    return attributes_dict
