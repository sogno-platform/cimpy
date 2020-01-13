import logging
import cimpy
import xmltodict
import os
import pytest_check as check
import pickle

logging.basicConfig(filename='Test.log', level=logging.INFO, filemode='w')


def test_export():
    test_files = [r".\Test_DiagramLayout.xml",
                  r".\Test_Equipment.xml",
                  r".\Test_StateVariables.xml",
                  r".\Test_Topology.xml", ]

    activeProfileList = ['DI', 'EQ', 'SV', 'TP']

    imported_files, namespaces = cimpy.cim_import(test_files, 'cgmes_v2_4_15')
    cimpy.cim_export(imported_files, namespaces, 'EXPORTED_Test', 'cgmes_v2_4_15', activeProfileList)

    test_dict = {}
    for file in test_files:
        xmlstring = open(file, encoding='utf8').read()
        parsed_export_file = xmltodict.parse(xmlstring, attr_prefix="$", cdata_key="_", dict_constructor=dict)
        test_dict.update(parsed_export_file['rdf:RDF'])

    export_dict = {}
    for file in os.listdir(os.getcwd()):
        if file.endswith(".xml") and 'EXPORTED' in str(file):
            xmlstring = open(file, encoding='utf8').read()
            parsed_export_file = xmltodict.parse(xmlstring, attr_prefix="$", cdata_key="_", dict_constructor=dict)
            export_dict.update(parsed_export_file['rdf:RDF'])

    for key in test_dict.keys():
        if 'cim:' in key:
            if key in export_dict.keys():
                # if key in ['cim:PowerTransformerEnd', 'cim:OperationalLimitType', 'cim:Diagram']:
                #    continue
                for elem in test_dict[key]:
                    check.is_in(elem, export_dict[key])

    for file in os.listdir(os.getcwd()):
        if 'EXPORTED' in str(file):
            os.remove(file)


def test_import():
    test_files = [r".\Test_DiagramLayout.xml",
                  r".\Test_Equipment.xml",
                  r".\Test_StateVariables.xml",
                  r".\Test_Topology.xml", ]

    imported_files, _ = cimpy.cim_import(test_files, 'cgmes_v2_4_15')

    import_resolved = cimpy.cimexport._get_class_attributes_with_references(imported_files, 'cgmes_v2_4_15')

    check_dict_pickle = pickle.load(open('CIGREMV_import.p', 'rb'))

    for elem in import_resolved:
        check.is_in(elem, check_dict_pickle)
