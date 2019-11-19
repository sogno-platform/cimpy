from lxml import etree
from time import time
import importlib
import logging
import os
import cimpy

logger = logging.getLogger(__name__)


# package_map[package_name][class_name] = cimpy.cim_version.package_name.class_name
def _create_package_map(cim_version):
    package_map = {}
    subfolders = os.listdir(cim_version)
    for folder in subfolders:
        path = os.path.join(cim_version, folder)
        if os.path.isdir(path):
            package_map[folder] = {}
            files = os.listdir(path)
            for file in files:
                file = file.split('.')[0]
                full_path = os.path.join(path, file)
                full_path = full_path.replace('/', '.').replace('\\', '.')
                full_path = "cimpy." + full_path
                package_map[folder][file] = full_path
    # return use_config(package_map, cim_version)
    return package_map


def cim_import(xml_files, cim_version, start_dict=None):
    """Function to read cimgen files and instantiate the classes

    This function parses xml files containing a cgmes topology and instantiates these classes with their attributes.
    The instantiation is done in two steps. In the first step all classes are instantiated with default values and
    in a second step the attributes contained in the xml files are set.

    :param xml_files: CIM RDF/XML file.
    :param cim_version: cgmes version, e.g. "cimgen_v2_4_15"
    :param start_dict: a list of classes which indicates which classes will be read
        e.g. elements=["BaseVoltage", "ACLineSegment"]
        * If start_dict=None the complete file will be read
    :return: res: map containing all classes contained in the xml file(s), assessable via the mRID
    :return: namespaces: a map containing all RDF namespaces
    """

    # Import cim version class
    cim_version_path = "cimpy." + cim_version
    importlib.__import__(cim_version_path)
    path = os.path.dirname(cimpy.__file__)
    cwd = os.getcwd()
    os.chdir(path)
    # Start the clock.
    t0 = time()

    # Mapping between the cim classes and the modules
    package_map = _create_package_map(cim_version)
    os.chdir(cwd)

    # logger.info('##########################################################################')
    # map used to group errors
    logger_errors_grouped = {}

    # A map of uuids to CIM objects to be returned.
    res = start_dict if start_dict is not None else {}

    # Obtain the namespaces from one of the input files
    namespaces = _get_namespaces(xml_files[0])
    namespace_rdf = _get_rdf_namespace(namespaces)

    # CIM element tag base (e.g. {http://iec.ch/TC57/2012/CIM-schema-cim16#} )
    base = "{" + namespaces["cim"] + "}"

    res, package, logger_errors_grouped = _instantiate_classes(res, xml_files, package_map,
                                                               namespace_rdf, base, logger_errors_grouped)
    res, logger_errors_grouped = _set_attributes(res, package, xml_files, namespace_rdf, base, logger_errors_grouped)

    if logger_errors_grouped:
        for error, count in logger_errors_grouped.items():
            logging_message = '{} : {} times'.format(error, count)
            logger.warning(logging_message)

    logger.info('Created totally {} CIM objects in {}s\n\n'.format(len(res), time() - t0))

    return res, namespaces


def _instantiate_classes(res, xml_files, package_map, namespace_rdf, base, logger_errors_grouped):
    # length of element tag base
    m = len(base)
    # first step: create the dict res{uuid}=instance_of_the_cim_class
    for xml_file in xml_files:

        logger.info('START of parsing file \"%s\"', xml_file)

        # get an iterable
        context = etree.iterparse(xml_file, ("start", "end"))

        # Turn it into an iterator (required for cElementTree).
        context = iter(context)

        # Get the root element ({http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF).
        _, root = next(context)

        for event, elem in context:
            # Process 'end' elements in the CIM namespace.
            if event == "end" and elem.tag[:m] == base:

                # check if the element has the attribute "rdf:ID" --> cim class located
                uuid = elem.get("{%s}ID" % namespace_rdf)
                if uuid is not None:  # cim class
                    # Element tag without namespace (e.g. VoltageLevel).
                    tag = elem.tag[m:]
                    try:
                        module_name = package_map[package][tag]
                    except KeyError:
                        error_msg = 'Module {} not implemented'.format(tag)
                        try:
                            logger_errors_grouped[error_msg] += 1
                        except KeyError:
                            logger_errors_grouped[error_msg] = 1

                        root.clear()
                        continue
                    # Import the module for the CIM object.
                    module = importlib.import_module(module_name)
                    # Get the CIM class from the module.
                    klass = getattr(module, tag)
                    # Instantiate the class and map it to the uuid.
                    # res[uuid] = klass(UUID=uuid)
                    res[uuid] = klass()
                    if hasattr(res[uuid], 'mRID'):
                        res[uuid].mRID = uuid

            elif event == "end" and 'Model.profile' in elem.tag:
                for package_key in package_map.keys():
                    if package_key in elem.text:
                        package = package_key
                        break

            # Clear children of the root element to minimise memory usage.
            root.clear()

    return res, package, logger_errors_grouped


def _set_attributes(res, package, xml_files, namespace_rdf, base, logger_errors_grouped):
    m = len(base)
    # Second step pass sets attributes and references.
    for xml_file in xml_files:

        # get an iterable and turn it into an iterator (required for cElementTree).
        context = iter(etree.iterparse(xml_file, ("start", "end")))

        # Get the root element ({http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF).
        _, root = next(context)

        for event, elem in context:
            # Process 'start' elements in the CIM namespace.
            if event == "start" and elem.tag[:m] == base:
                uuid = elem.get("{%s}ID" % namespace_rdf)
                if uuid is None:
                    uuid = elem.get("{%s}about" % namespace_rdf)
                    if uuid is not None:
                        uuid = uuid[1:]
                if uuid is not None:
                    # Locate the CIM object using the uuid.
                    try:
                        obj = res[uuid]
                    except KeyError:
                        error_msg = 'Missing {} object with uuid: {}'.format(elem.tag[m:], uuid)
                        try:
                            logger_errors_grouped[error_msg] += 1
                        except KeyError:
                            logger_errors_grouped[error_msg] = 1
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
                                        logger_errors_grouped[error_msg] += 1
                                    except KeyError:
                                        logger_errors_grouped[error_msg] = 1
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
                                        pass

                                else:  # reference or enum (uuid2 is not None)
                                    # Use the '#' prefix to distinguish between references and enumerations.
                                    if uuid2[0] == "#":  # reference
                                        try:
                                            val = res[uuid2[1:]]  # remove '#' prefix
                                        except KeyError:
                                            error_msg = 'Referenced {} [{}] object missing.'.format(
                                                obj.__class__.__name__, uuid2[1:])
                                            try:
                                                logger_errors_grouped[error_msg] += 1
                                            except KeyError:
                                                logger_errors_grouped[error_msg] = 1

                                            continue

                                        default = getattr(obj, attr)
                                        if default is None:  # 1..1 or 0..1
                                            # Rely on properties to set any bi-directional references.
                                            setattr(obj, attr, [val])
                                        elif isinstance(default, list):  # many
                                            attribute = getattr(obj, attr)
                                            attribute.append(val)
                                            setattr(obj, attr, attribute)

                                        if hasattr(val, obj.__class__.__name__):
                                            default1 = getattr(val, obj.__class__.__name__)
                                            if default1 is None:
                                                setattr(val, obj.__class__.__name__, [obj])
                                            elif isinstance(default, list):  # many
                                                # Use 'add*' method to set reference.
                                                attribute = getattr(obj, attr)
                                                attribute.append(val)
                                                setattr(obj, attr, attribute)

                                        # else:
                                        # logger.error("Reference error [%s].", default)
                                    else:  # enum
                                        val = uuid2.rsplit(".", 1)[1]
                                        setattr(obj, attr, val)

                            else:  # if elem.get("{%s}ID" % nd_rdf is not None:
                                # Finished setting object attributes.
                                break

            # Clear children of the root element to minimise memory usage.
            root.clear()

        logger.info('END of parsing file {}'.format(xml_file))

    return res, logger_errors_grouped


def _get_namespaces(source):
    """
    Returns a map of prefix to namespace for the given XML file.
    """

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


def _get_rdf_namespace(namespaces):
    try:
        namespace = namespaces['rdf']
    except KeyError:
        ns = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
        logger.warning('No rdf namespace found. Using %s' % ns)

    return namespace
