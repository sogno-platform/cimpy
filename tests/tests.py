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


# test export with imported files
# test cimpy export with exported files
def test_export_with_exported_files():
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

    for file in os.listdir(os.getcwd()):
        if 'EXPORTED' in str(file):
            os.remove(file)


# def test_export_with_imported_files():
#     import_files = [os.path.join(example_path, 'Rootnet_FULL_NE_24J13h_DI.xml'),
#                     os.path.join(example_path, 'Rootnet_FULL_NE_24J13h_EQ.xml'),
#                     os.path.join(example_path, 'Rootnet_FULL_NE_24J13h_SV.xml'),
#                     os.path.join(example_path, 'Rootnet_FULL_NE_24J13h_TP.xml'), ]
#
#     activeProfileList = ['DI', 'EQ', 'SV', 'TP']
#
#     imported_files, namespaces = cimpy.cim_import(import_files, 'cgmes_v2_4_15')
#     cimpy.cim_export(imported_files, namespaces, 'EXPORTED_Test', 'cgmes_v2_4_15', activeProfileList)
#
#     test_list = []
#     for file in import_files:
#         xmlstring = open(file, encoding='utf8').read()
#         parsed_export_file = xmltodict.parse(xmlstring, attr_prefix="$", cdata_key="_", dict_constructor=dict)
#         test_list.append(parsed_export_file['rdf:RDF'])
#
#     export_list = []
#     for file in os.listdir(os.getcwd()):
#         if file.endswith(".xml") and 'EXPORTED' in str(file):
#             xmlstring = open(file, encoding='utf8').read()
#             parsed_export_file = xmltodict.parse(xmlstring, attr_prefix="$", cdata_key="_", dict_constructor=dict)
#             export_list.append(parsed_export_file['rdf:RDF'])
#
#     export_dict = {}
#     for export_file in export_list:
#         profile = export_file['md:FullModel']['md:Model.profile']
#         for key in short_profile_name.keys():
#             if key in profile:
#                 export_dict[key] = export_file
#
#     test_dict = {}
#     for elem in test_list:
#         profile = elem['md:FullModel']['md:Model.profile']
#         for key in short_profile_name.keys():
#             if key in profile:
#                 test_dict[key] = elem
#
#     for profile, current_test_dict in test_dict.items():
#         check.is_in(profile, export_dict.keys())
#         if profile in export_dict.keys():
#             current_export_dict = export_dict[profile]
#             for class_key in current_test_dict:
#                 if 'cim:' not in class_key or 'cim:NameType' in class_key:
#                     continue
#                 check.is_in(class_key, current_export_dict.keys())
#                 if class_key in current_export_dict.keys():
#                     current_export_class = current_export_dict[class_key]
#                     current_test_class = current_test_dict[class_key]
#                     test_mRIDs = []
#                     test_class_dict = {}
#                     if isinstance(current_test_class, list):
#                         for obj in current_test_class:
#                             test_mRIDs.append(obj['$rdf:ID'])
#                             test_class_dict[obj['$rdf:ID']] = obj
#                     else:
#                         test_mRIDs.append(current_test_class['$rdf:ID'])
#                         test_class_dict[current_test_class['$rdf:ID']] = current_test_class
#
#                     export_mRIDs = []
#                     export_class_dict = {}
#                     if isinstance(current_export_class, list):
#                         for obj in current_export_class:
#                             export_mRIDs.append(obj['$rdf:ID'])
#                             export_class_dict[obj['$rdf:ID']] = obj
#                     else:
#                         export_mRIDs.append(current_export_class['$rdf:ID'])
#                         export_class_dict[current_export_class['$rdf:ID']] = current_export_class
#
#                     for mRID in test_mRIDs:
#                         check.is_in(mRID, export_mRIDs)
#                         if mRID in export_mRIDs:
#                             test_attr = test_class_dict[mRID].items()
#                             export_attr = export_class_dict[mRID].items()
#                             for item in test_attr:
#                                 if item[0] is 'cim:NameType':
#                                     continue
#                                 if item[1] in ['0', '0e+000', '0.0', '', 'false', 'None', 'list']:
#                                     continue
#                                 if isinstance(item[1], dict):
#                                     test_item = item
#                                 elif len(item[1].split('.')) > 1:
#                                     try:
#                                         test_item = (item[0], str(float(item[1])))
#                                     except ValueError:
#                                         continue
#                                     except TypeError:
#                                         pass
#                                 else:
#                                     test_item = item
#
#                                 check.is_in(test_item, export_attr)
#
#
#     for file in os.listdir(os.getcwd()):
#         if 'EXPORTED' in str(file):
#             os.remove(file)


def test_import():
    test_files = [os.path.join(example_path, 'Rootnet_FULL_NE_24J13h_DI.xml'),
                  os.path.join(example_path, 'Rootnet_FULL_NE_24J13h_EQ.xml'),
                  os.path.join(example_path, 'Rootnet_FULL_NE_24J13h_SV.xml'),
                  os.path.join(example_path, 'Rootnet_FULL_NE_24J13h_TP.xml'), ]

    imported_files, _ = cimpy.cim_import(test_files, 'cgmes_v2_4_15')

    import_resolved = cimpy.cimexport._get_class_attributes_with_references(imported_files, 'cgmes_v2_4_15')

    check_dict_pickle = pickle.load(open('CIGREMV_import_reference_cgmes_v2_4_15.p', 'rb'))

    for elem in import_resolved:
        check.is_in(elem, check_dict_pickle)
