import logging
import os, sys
import glob
import pytest_check as check
import pickle
from pathlib import Path
 
sys.path.append(os.getcwd())
import cimpy
from cimpy.cgmes_v3_0_0.Base import short_profile_name

logging.basicConfig(filename='Test_import.log',
                    level=logging.INFO, filemode='w')

example_dir = Path(os.path.join(os.path.dirname(__file__),
                                '../cimpy/examples/sampledata/CIM_LV_Simbench_Grid')).resolve()


def test_import():
    """ This function tests the import functionality by importing files and comparing them to previously imported and pickled files.
    """

    global example_dir
    test_files = []
    for file in example_dir.glob('*.xml'):
        test_files.append(str(file.absolute()))

    imported_result = cimpy.cim_import(test_files, 'cgmes_v3_0_0')

    import_resolved = cimpy.cimexport._get_class_attributes_with_references(
        imported_result, 'cgmes_v3_0_0')

    ref_dict_path = Path(os.path.join(os.path.dirname(
        __file__), 'CIM_v3_import_reference.p1'))
    check_dict_pickle = pickle.load(open(ref_dict_path, 'rb'))

    for elem in import_resolved:
        check.is_in(elem, check_dict_pickle)
