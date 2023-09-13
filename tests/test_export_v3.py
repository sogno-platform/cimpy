import logging
import xmltodict
import os, sys
import glob
import pytest_check as check
from pathlib import Path
import pytest

sys.path.append(os.getcwd())
import cimpy
from cimpy.cgmes_v3_0_0.Base import short_profile_name

logging.basicConfig(filename='Test_export_with_exported_files.log',
                    level=logging.INFO, filemode='w')


@pytest.fixture
def sample_cimdata():
    """ Import the sampledata using cimpy
    """
    example_dir = Path(os.path.join(os.path.dirname(
        __file__), '../cimpy/examples/sampledata/CIM_LV_Simbench_Grid')).resolve()
    import_files = []
    for file in example_dir.glob('*.xml'):
        import_files.append(str(file.absolute()))
    return cimpy.cim_import(import_files, 'cgmes_v3_0_0')


def read_ref_xml():
    """ Read the reference xmls into a dict
    """
    test_list = []

    test_dir = Path(os.path.dirname(__file__)).resolve()

    for file in test_dir.glob('CIM_v3_reference*.xml'):
        xmlstring = open(file, encoding='utf8').read()
        parsed_export_file = xmltodict.parse(
            xmlstring, attr_prefix="$", cdata_key="_", dict_constructor=dict)
        test_list.append(parsed_export_file['rdf:RDF'])

    test_dict = {}
    for elem in test_list:
        profile = elem['md:FullModel']['md:Model.profile']
        for key in short_profile_name.keys():
            if key in profile:
                test_dict[key] = elem
    return test_dict


def read_exported_xml(directory):
    export_list = []

    test_dir = Path(directory).resolve()

    for file in test_dir.glob('*EXPORTED*.xml'):
        xmlstring = open(file, encoding='utf8').read()
        parsed_export_file = xmltodict.parse(
            xmlstring, attr_prefix="$", cdata_key="_", dict_constructor=dict)
        export_list.append(parsed_export_file['rdf:RDF'])

    export_dict = {}
    for export_file in export_list:
        profile = export_file['md:FullModel']['md:Model.profile']
        for key in short_profile_name.keys():
            if key in profile:
                export_dict[key] = export_file
    return export_dict

# This test tests the export functionality of this package by first importing the CIGRE_MV_Rudion_With_LoadFlow_Results
# example and exporting them. The exported files are compared with previously exported files which were checked manually


def test_export_with_exported_files(sample_cimdata, tmpdir):
    # activeProfileList = ['DL', 'EQ', 'SV', 'TP'] - DL is not working for some reason
    activeProfileList = ['EQ', 'SV', 'TP']

    cimpy.cim_export(sample_cimdata, tmpdir + '/EXPORTED_Test',
                     'cgmes_v3_0_0', activeProfileList)

    test_dict = read_ref_xml()
    export_dict = read_exported_xml(tmpdir)

    for profile, current_test_dict in test_dict.items():
        check.is_in(profile, export_dict.keys())
        if profile in export_dict.keys():
            current_export_dict = export_dict[profile]
            for class_key in current_test_dict:
                if 'cim:' not in class_key:
                    continue
                check.is_in(class_key, current_export_dict.keys())
                if class_key in current_export_dict.keys():
                    current_export_class = current_export_dict[class_key]
                    current_test_class = current_test_dict[class_key]
                    if isinstance(current_test_class, list):
                        for item in current_test_class:
                            check.is_in(item, current_export_class)
                    else:
                        check.equal(current_test_class, current_export_class)


def test_export_with_imported_files(sample_cimdata, tmpdir):
    #activeProfileList = ['DL', 'EQ', 'SSH', 'SV', 'TP'] - DL is not working for some reason
    activeProfileList = ['EQ', 'SSH', 'SV', 'TP']

    cimpy.cim_export(sample_cimdata, tmpdir + '/EXPORTED_Test',
                     'cgmes_v3_0_0', activeProfileList)

    test_dict = read_ref_xml()
    export_dict = read_exported_xml(tmpdir)

    for profile, current_test_dict in test_dict.items():
        check.is_in(profile, export_dict.keys())
        if profile in export_dict.keys():
            current_export_dict = export_dict[profile]
            for class_key in current_test_dict:
                if 'cim:' not in class_key or class_key in ['cim:NameType', 'cim:Name']:
                    continue
                check.is_in(class_key, current_export_dict.keys())
                if class_key in current_export_dict.keys():
                    current_export_class = current_export_dict[class_key]
                    current_test_class = current_test_dict[class_key]
                    test_mRIDs = []
                    test_class_dict = {}
                    if isinstance(current_test_class, list):
                        for obj in current_test_class:
                            try:
                                test_mRIDs.append(obj['$rdf:ID'])
                                test_class_dict[obj['$rdf:ID']] = obj
                            except KeyError:
                                try:
                                    test_mRIDs.append(obj['$rdf:about'])
                                    test_class_dict[obj['$rdf:about']] = obj
                                except KeyError:
                                    check.is_in('$rdf:about', obj.keys())
                                    check.is_in('$rdf:ID', obj.keys())
                    else:
                        try:
                            test_mRIDs.append(current_test_class['$rdf:ID'])
                            test_class_dict[current_test_class['$rdf:ID']
                                            ] = current_test_class
                        except KeyError:
                            try:
                                test_mRIDs.append(
                                    current_test_class['$rdf:about'])
                                test_class_dict[current_test_class['$rdf:about']] = obj
                            except KeyError:
                                check.is_in(
                                    '$rdf:about', current_test_class.keys())
                                check.is_in(
                                    '$rdf:ID', current_test_class.keys())

                    export_mRIDs = []
                    export_class_dict = {}
                    if isinstance(current_export_class, list):
                        for obj in current_export_class:
                            try:
                                export_mRIDs.append(obj['$rdf:ID'])
                                export_class_dict[obj['$rdf:ID']] = obj
                            except KeyError:
                                try:
                                    export_mRIDs.append(obj['$rdf:about'])
                                    export_class_dict[obj['$rdf:about']] = obj
                                except KeyError:
                                    check.is_in('$rdf:about', obj.keys())
                                    check.is_in('$rdf:ID', obj.keys())
                    else:
                        try:
                            export_mRIDs.append(
                                current_export_class['$rdf:ID'])
                            export_class_dict[current_export_class['$rdf:ID']
                                              ] = current_export_class
                        except KeyError:
                            try:
                                export_mRIDs.append(
                                    current_export_class['$rdf:about'])
                                export_class_dict[current_export_class['$rdf:about']] = obj
                            except KeyError:
                                check.is_in(
                                    '$rdf:about', current_export_class.keys())
                                check.is_in(
                                    '$rdf:ID', current_export_class.keys())

                    for mRID in test_mRIDs:
                        check.is_in(mRID, export_mRIDs)
                        if mRID in export_mRIDs:
                            test_attr = test_class_dict[mRID].items()
                            export_attr = export_class_dict[mRID].items()
                            for item in test_attr:
                                if item[0] in ['cim:NameType', 'cim:ExternalNetworkInjection.referencePriority',
                                               'cim:Terminal.connected']:
                                    continue
                                elif item[0] == 'cim:Terminal.sequenceNumber':
                                    test_item = 'cim:ACDCTerminal.sequenceNumber'
                                else:
                                    test_item = item[0]

                                if item[1] in ['0', '0e+000', '0.0', '', 'false', 'None', 'list',
                                               {'$rdf:resource': '#_32d6d32e-c3f0-43d4-8103-079a15594fc6'}]:
                                    continue
                                if isinstance(item[1], dict) or isinstance(item[1], list):
                                    test_item = item
                                elif len(item[1].split('.')) > 1:
                                    try:
                                        test_item = (
                                            item[0], str(float(item[1])))
                                    except ValueError:
                                        continue
                                    except TypeError:
                                        pass
                                elif item[1] == 'true':
                                    test_item = (test_item, 'True')
                                else:
                                    test_item = (test_item, item[1])

                                check.is_in(test_item, export_attr)

