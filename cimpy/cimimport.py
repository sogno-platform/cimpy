from lxml import etree
from time import time
import importlib
import logging
import os
import cimpy

logger = logging.getLogger(__name__)


def cim_import(xml_files, cgmes_version, start_dict=None):
    """Function to read cimgen files and instantiate the classes

    This function parses xml files containing a cgmes topology and instantiates these classes with their attributes.
    The instantiation is done in two steps. In the first step all classes are instantiated with default values and
    in a second step the attributes contained in the xml files are set. The origin of all classes and attributes are
    stored in the class attribute serializationProfile.

    :param xml_files: CIM RDF/XML file.
    :param cgmes_version: cgmes version, e.g. "cgmes_v2_4_15"
    :param start_dict: a list of classes which indicates which classes will be read
        e.g. elements=["BaseVoltage", "ACLineSegment"]
        * If start_dict=None the complete file will be read
    :return: import_result: a dictionary containing the topology and meta information. The topology can be extracted via \
    import_result['topology']. The topology dictionary contains all objects accessible via their mRID. The meta \
    information can be extracted via import_result['meta_info']. The meta_info dictionary contains a new dictionary with \
    the keys: 'author', 'namespaces' and 'urls'. The last two are also dictionaries. 'urls' contains a mapping \
    between references to URLs and the extracted value of the URL, e.g. 'absoluteValue': \
    'http://iec.ch/TC57/2012/CIM-schema-cim16#OperationalLimitDirectionKind.absoluteValue' These mappings are accessible \
    via the name of the attribute, e.g. import_result['meta_info']['urls'}[attr_name] = {mapping like example above}. \
    'namespaces' is a dictionary containing all RDF namespaces used in the imported xml files.
    """

    # Import cim version class
    cgmes_version_path = "cimpy." + cgmes_version

    # Start the clock.
    t0 = time()

    # map used to group errors and infos
    logger_grouped = dict(errors={}, info={})

    # create a dict which will contain meta information and the topology
    import_result = start_dict if start_dict is not None else dict(meta_info={}, topology={})

    # create sub-dictionaries
    import_result['meta_info'] = dict(namespaces=_get_namespaces(xml_files[0]), urls={})
    namespace_rdf = _get_rdf_namespace(import_result['meta_info']['namespaces'])

    # CIM element tag base (e.g. {http://iec.ch/TC57/2012/CIM-schema-cim16#} )
    base = "{" + import_result['meta_info']['namespaces']["cim"] + "}"

    import_result, logger_grouped, = _instantiate_classes(import_result, xml_files, cgmes_version_path, namespace_rdf,
                                                          base, logger_grouped)

    import_result, logger_grouped = _set_attributes(import_result, xml_files, namespace_rdf, base, logger_grouped)

    if logger_grouped['errors']:
        for error, count in logger_grouped['errors'].items():
            logging_message = '{} : {} times'.format(error, count)
            logger.warning(logging_message)

    if logger_grouped['info']:
        for info, count in logger_grouped['info'].items():
            logging_message = '{} : {} times'.format(info, count)
            logger.info(logging_message)

            # print info which classes and how many were instantiated
            print(logging_message)

    elapsed_time = time() - t0
    logger.info('Created totally {} CIM objects in {}s\n\n'.format(len(import_result['topology']), elapsed_time))
    # print info of how many classes in total were instantiated to terminal
    print('Created totally {} CIM objects in {}s'.format(len(import_result['topology']), elapsed_time))

    return import_result


# This function instantiates the classes defined in all RDF files. All attributes are set to default values.
# The only exception is the mRID which is set for all classes that have this attribute. The attributes of a class
# are set in the _set_attributes function because some attributes might be stored in one package and the class in
# another. Since after this function all classes are instantiated, there should be no problem in setting the attributes.
# Also the information from which package file a class was read is stored in the serializationProfile dictionary.
def _instantiate_classes(import_result, xml_files, cgmes_version_path, namespace_rdf, base,
                         logger_grouped):

    # extract topology from import_result
    topology = import_result['topology']

    # length of element tag base
    m = len(base)
    # first step: create the dict res{uuid}=instance_of_the_cim_class
    for xml_file in xml_files:

        logger.info('START of parsing file \"%s\"', xml_file)

        # Reset stream
        if hasattr(xml_file, "seek"):
            xml_file.seek(0)

        # get an iterable
        context = etree.iterparse(xml_file, ("start", "end"))

        # Turn it into an iterator (required for cElementTree).
        context = iter(context)

        # Get the root element ({http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF).
        _, root = next(context)

        package = ''

        for event, elem in context:

            # Process 'end' elements in the CGMES namespace.
            if event == "end" and elem.tag[:m] == base:

                # check if the element has the attribute "rdf:ID" --> CGMES class located
                uuid = elem.get("{%s}ID" % namespace_rdf)
                if uuid is not None:  # cim class
                    # Element tag without namespace (e.g. VoltageLevel).
                    tag = elem.tag[m:]
                    try:
                        # module_name = package_map[package][tag]
                        # Import the module for the CGMES object.
                        module_name = cgmes_version_path + '.' + tag
                        module = importlib.import_module(module_name)
                    except ModuleNotFoundError:
                        error_msg = 'Module {} not implemented'.format(tag)
                        try:
                            logger_grouped['errors'][error_msg] += 1
                        except KeyError:
                            logger_grouped['errors'][error_msg] = 1

                        root.clear()
                        continue

                    # Get the CGMES class from the module.
                    klass = getattr(module, tag)
                    # Instantiate the class and map it to the uuid.
                    # res[uuid] = klass(UUID=uuid)
                    topology[uuid] = klass()
                    info_msg = 'CIM object {} created'.format(module_name.split('.')[-1])
                    try:
                        logger_grouped['info'][info_msg] += 1
                    except KeyError:
                        logger_grouped['info'][info_msg] = 1

                    # check if the class has the attribute mRID and set the mRID to the read in UUID. If the class
                    # does not has this attribute, the UUID is only stored in the res dictionary.
                    if hasattr(topology[uuid], 'mRID'):
                        topology[uuid].mRID = uuid

                    if package != '':
                        topology[uuid].serializationProfile['class'] = short_package_name[package]
                    else:
                        error_msg = 'Package information not found for class {}'.format(
                            klass.__class__.__name__
                        )
                        try:
                            logger_grouped['errors'][error_msg] += 1
                        except KeyError:
                            logger_grouped['errors'][error_msg] = 1

            # Check which package is read
            elif event == "end":
                if 'Model.profile' in elem.tag:
                    for package_key in short_package_name.keys():
                        if package_key in elem.text:
                            package = package_key
                            break
                # the author of all imported files should be the same, avoid multiple entries
                elif 'author' in import_result['meta_info'].keys():
                    pass
                # extract author
                elif 'Model.createdBy' in elem.tag:
                    import_result['meta_info']['author'] = elem.text
                elif 'Model.modelingAuthoritySet' in elem.tag:
                    import_result['meta_info']['author'] = elem.text

            # Clear children of the root element to minimise memory usage.
            root.clear()

    return import_result, logger_grouped


# This function sets all attributes after the classes are instantiated by _instanciate_classes. Cyclic attributes like
# PowerTransformerEnd <-> PowerTransformer are set. This function also stores the information from which package file
# the attributes are read in the serializationProfile dictionary.
def _set_attributes(import_result, xml_files, namespace_rdf, base, logger_grouped):

    topology = import_result['topology']
    urls = import_result['meta_info']['urls']

    m = len(base)

    # Second step pass sets attributes and references.
    for xml_file in xml_files:

        # get an iterable and turn it into an iterator (required for cElementTree).
        context = iter(etree.iterparse(xml_file, ("start", "end")))

        # Reset stream
        if hasattr(xml_file, "seek"):
            xml_file.seek(0)

        # Get the root element ({http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF).
        _, root = next(context)

        package = ''

        for event, elem in context:

            # Process 'start' elements in the CGMES namespace.
            if event == "start" and elem.tag[:m] == base:
                uuid = elem.get("{%s}ID" % namespace_rdf)
                if uuid is None:
                    uuid = elem.get("{%s}about" % namespace_rdf)
                    if uuid is not None:
                        uuid = uuid[1:]
                if uuid is not None:
                    # Locate the CGMES object using the uuid.
                    try:
                        obj = topology[uuid]
                    except KeyError:
                        error_msg = 'Missing {} object with uuid: {}'.format(elem.tag[m:], uuid)
                        try:
                            logger_grouped['errors'][error_msg] += 1
                        except KeyError:
                            logger_grouped['errors'][error_msg] = 1
                        root.clear()
                        continue

                    # Iterate over attributes/references.
                    for event, elem in context:
                        # Process end events with elements in the CIM namespace.
                        if event == "end" and elem.tag[:m] == base:
                            # Break if class closing element (e.g. </cim:Terminal>).
                            if elem.get("{%s}ID" % namespace_rdf) is None \
                                    and elem.get("{%s}about" % namespace_rdf) is None:
                                # Get the attribute/reference name.
                                attr = elem.tag[m:].rsplit(".")[-1]

                                if not hasattr(obj, attr):
                                    error_msg = "'%s' has not attribute '%s'" % (obj.__class__.__name__, attr)
                                    try:
                                        logger_grouped['errors'][error_msg] += 1
                                    except KeyError:
                                        logger_grouped['errors'][error_msg] = 1
                                    continue

                                # Use the rdf:resource attribute to distinguish between attributes and references/enums.
                                uuid2 = elem.get("{%s}resource" % namespace_rdf)

                                if uuid2 is None:  # attribute
                                    # Convert value type using the default value.
                                    try:
                                        typ = type(getattr(obj, attr))
                                        if isinstance(getattr(obj, attr), bool):  # if typ==<class 'bool'>
                                            # The function bool("false") returns True,
                                            # because it is called upon non-empty string!
                                            # This means that it wrongly reads "false" value as boolean True.
                                            # This is why this special case testing is necessary.
                                            if str.title(elem.text) == 'True':
                                                setattr(obj, attr, True)
                                            else:
                                                setattr(obj, attr, False)
                                        else:
                                            setattr(obj, attr, typ(elem.text))
                                    except TypeError:
                                        try:
                                            setattr(obj, attr, elem.text)
                                        except TypeError:
                                            pass

                                else:  # reference or enum (uuid2 is not None)
                                    # Use the '#' prefix to distinguish between references and enumerations.
                                    if uuid2[0] == "#":  # reference
                                        try:
                                            val = topology[uuid2[1:]]  # remove '#' prefix
                                        except KeyError:
                                            error_msg = 'Referenced {} [{}] object missing.'.format(
                                                obj.__class__.__name__, uuid2[1:])
                                            try:
                                                logger_grouped['errors'][error_msg] += 1
                                            except KeyError:
                                                logger_grouped['errors'][error_msg] = 1

                                            continue

                                        default = getattr(obj, attr)
                                        if default is None:  # 1..1 or 0..1
                                            # Rely on properties to set any bi-directional references.
                                            setattr(obj, attr, val)
                                        elif default == 'list':  # many
                                            setattr(obj, attr, [val])
                                        elif isinstance(default, list):  # many
                                            attribute = getattr(obj, attr)
                                            if val not in attribute:
                                                attribute.append(val)
                                                setattr(obj, attr, attribute)
                                        elif default == val:
                                            # attribute reference already resolved
                                            pass
                                        else:
                                            # note here
                                            error_msg = 'Multiplicity Error for class {} [{}], attribute {}. Multiplicity should be 1..1 or 0..1'.format(
                                                obj.__class__.__name__, uuid, attr)
                                            try:
                                                logger_grouped['errors'][error_msg] += 1
                                            except KeyError:
                                                logger_grouped['errors'][error_msg] = 1

                                        if hasattr(val, obj.__class__.__name__):
                                            default1 = getattr(val, obj.__class__.__name__)
                                            if default1 is None:
                                                setattr(val, obj.__class__.__name__, obj)
                                            elif default1 == 'list':  # many
                                                setattr(val, obj.__class__.__name__, [obj])
                                            elif isinstance(default1, list):  # many
                                                attribute2 = getattr(val, obj.__class__.__name__)
                                                if obj not in attribute2:
                                                    attribute2.append(obj)
                                                    setattr(val, obj.__class__.__name__, attribute2)
                                            elif default1 == obj:
                                                pass
                                            else:
                                                error_msg = 'Multiplicity Error for class {} [{}], attribute {}. Multiplicity should be 1..1 or 0..1'.format(
                                                    val.__class__.__name__, uuid2[1:], obj.__class__.__name__)
                                                try:
                                                    logger_grouped['errors'][error_msg] += 1
                                                except KeyError:
                                                    logger_grouped['errors'][error_msg] = 1

                                    else:  # enum
                                        # if http in uuid2 reference to URL, create mapping
                                        if 'http' in uuid2:
                                            if attr in urls.keys():
                                                if uuid2.rsplit(".", 1)[1] not in urls[attr].keys():
                                                    urls[attr][uuid2.rsplit(".", 1)[1]] = uuid2
                                            else:
                                                urls[attr] = {uuid2.rsplit(".", 1)[1]: uuid2}

                                            # url_reference_dict[uuid2.rsplit(".", 1)[1]] = uuid2
                                        val = uuid2.rsplit(".", 1)[1]
                                        setattr(obj, attr, val)

                                if package != '':
                                    obj.serializationProfile[attr] = short_package_name[package]
                                else:
                                    error_msg = 'Package information not found for class {}, attribute {}'.format(
                                        obj.__class__.__name__, attr
                                    )
                                    try:
                                        logger_grouped['errors'][error_msg] += 1
                                    except KeyError:
                                        logger_grouped['errors'][error_msg] = 1
                            else:  # if elem.get("{%s}ID" % nd_rdf is not None:
                                # Finished setting object attributes.
                                break

            # Check which package is read
            elif event == "end" and 'Model.profile' in elem.tag:
                for package_key in short_package_name.keys():
                    if package_key in elem.text:
                        package = package_key
                        break

            # Clear children of the root element to minimise memory usage.
            root.clear()

        logger.info('END of parsing file "{}"'.format(xml_file))
    return import_result, logger_grouped


# Returns a map of prefix to namespace for the given XML file.
def _get_namespaces(source):
    namespaces = {}
    events = ("end", "start-ns", "end-ns")
    for (event, elem) in etree.iterparse(source, events):
        if event == "start-ns":
            prefix, ns = elem
            namespaces[prefix] = ns
        elif event == "end":
            break

    # Reset stream
    if hasattr(source, "seek"):
        source.seek(0)

    return namespaces


# Returns the RDF Namespace from the namespaces dictionary
def _get_rdf_namespace(namespaces):
    try:
        namespace = namespaces['rdf']
    except KeyError:
        ns = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
        logger.warning('No rdf namespace found. Using %s' % ns)

    return namespace


# TODO: use cimpy.cgmes.Profile instead
# used to map the profile name to their abbreviations according to the CGMES standard
short_package_name = {
    "DiagramLayout": 'DL',
    "Dynamics": "DY",
    "Equipment": "EQ",
    "GeographicalLocation": "GL",
    "StateVariables": "SV",
    "SteadyStateHypothesis": "SSH",
    "Topology": "TP"
}
