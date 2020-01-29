import logging
import cimpy
import os
import pytest_check as check
import pickle

logging.basicConfig(filename='Test_import.log', level=logging.INFO, filemode='w')

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


# This function tests the import functionality by importing files and comparing them to previously imported and pickled
# files.
def test_import():
    test_files = [os.path.join(example_path, 'Rootnet_FULL_NE_24J13h_DI.xml'),
                  os.path.join(example_path, 'Rootnet_FULL_NE_24J13h_EQ.xml'),
                  os.path.join(example_path, 'Rootnet_FULL_NE_24J13h_SV.xml'),
                  os.path.join(example_path, 'Rootnet_FULL_NE_24J13h_TP.xml'), ]

    imported_files, _, url_reference_dict = cimpy.cim_import(test_files, 'cgmes_v2_4_15')

    import_resolved = cimpy.cimexport._get_class_attributes_with_references(imported_files,
                                                                            'cgmes_v2_4_15', url_reference_dict)

    check_dict_pickle = pickle.load(open('CIGREMV_import_reference_cgmes_v2_4_15.p', 'rb'))

    for elem in import_resolved:
        check.is_in(elem, check_dict_pickle)