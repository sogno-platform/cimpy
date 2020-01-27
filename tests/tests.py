import logging
import cimpy
import xmltodict
import os
import pytest_check as check
import pickle

logging.basicConfig(filename='Test.log', level=logging.INFO, filemode='w')

short_profile_name = {
    "DiagramLayout": 'DI',
    "Dynamics": "DY",
    "Equipment": "EQ",
    "GeographicalLocation": "GL",
    "StateVariables": "SV",
    "SteadyStateHypothesis": "SSH",
    "Topology": "TP"
}

example_path = os.path.join('..',
                            os.path.join('examples',
                                         os.path.join('sampledata',
                                                      os.path.join('CIGRE_MV',
                                                                   'CIGRE_MV_Rudion_With_LoadFlow_Results'))))


def test_export():
    import_files = [os.path.join(example_path, 'Rootnet_FULL_NE_24J13h_DI.xml'),
                    os.path.join(example_path, 'Rootnet_FULL_NE_24J13h_EQ.xml'),
                    os.path.join(example_path, 'Rootnet_FULL_NE_24J13h_SV.xml'),
                    os.path.join(example_path, 'Rootnet_FULL_NE_24J13h_TP.xml'), ]

    activeProfileList = ['DI', 'EQ', 'SV', 'TP']

    imported_files, namespaces = cimpy.cim_import(import_files, 'cgmes_v2_4_15')
    cimpy.cim_export(imported_files, namespaces, 'EXPORTED_Test', 'cgmes_v2_4_15', activeProfileList)

    test_list = []
    for file in os.listdir(os.getcwd()):
        if '.xml' in file and 'EXPORTED' not in file:
            xmlstring = open(file, encoding='utf8').read()
            parsed_export_file = xmltodict.parse(xmlstring, attr_prefix="$", cdata_key="_", dict_constructor=dict)
            test_list.append(parsed_export_file['rdf:RDF'])

    export_list = []
    for file in os.listdir(os.getcwd()):
        if file.endswith(".xml") and 'EXPORTED' in str(file):
            xmlstring = open(file, encoding='utf8').read()
            parsed_export_file = xmltodict.parse(xmlstring, attr_prefix="$", cdata_key="_", dict_constructor=dict)
            export_list.append(parsed_export_file['rdf:RDF'])

    export_dict = {}
    for export_file in export_list:
        profile = export_file['md:FullModel']['md:Model.profile']
        for key in short_profile_name.keys():
            if key in profile:
                export_dict[key] = export_file

    test_dict = {}
    for elem in test_list:
        profile = elem['md:FullModel']['md:Model.profile']
        for key in short_profile_name.keys():
            if key in profile:
                test_dict[key] = elem

    for profile, current_test_dict in test_dict.items():
        check.is_in(profile, export_dict.keys())
        if profile in export_dict.keys():
            current_export_dict = export_dict[profile]
            for class_key in current_test_dict:
                if 'cim:' not in class_key or 'cim:NameType' in class_key:
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


    # for key in test_dict.keys():
    #     if 'cim:' in key:
    #         if key in export_dict.keys():
    #             # if key in ['cim:PowerTransformerEnd', 'cim:OperationalLimitType', 'cim:Diagram']:
    #             #    continue
    #             for elem in test_dict[key]:
    #                 check.is_in(elem, export_dict[key])

    for file in os.listdir(os.getcwd()):
        if 'EXPORTED' in str(file):
            os.remove(file)


def test_import():
    test_files = [os.path.join(example_path, 'Rootnet_FULL_NE_24J13h_DI.xml'),
                  os.path.join(example_path, 'Rootnet_FULL_NE_24J13h_EQ.xml'),
                  os.path.join(example_path, 'Rootnet_FULL_NE_24J13h_SV.xml'),
                  os.path.join(example_path, 'Rootnet_FULL_NE_24J13h_TP.xml'), ]

    imported_files, _ = cimpy.cim_import(test_files, 'cgmes_v2_4_15')

    import_resolved = cimpy.cimexport._get_class_attributes_with_references(imported_files, 'cgmes_v2_4_15')

    check_dict_pickle = pickle.load(open('CIGREMV_import.p', 'rb'))

    for elem in import_resolved:
        check.is_in(elem, check_dict_pickle)

test_export()