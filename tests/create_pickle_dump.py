import os
import pickle
from pathlib import Path
import cimpy

example_path = Path(os.path.join(os.path.dirname(__file__), "../cimpy/examples/sampledata/CIGRE_MV")).resolve()


def create_pickle():

    test_files = []

    for file in example_path.glob("*.xml"):
        print("file: ", file)
        test_files.append(str(file.absolute()))

    imported_result = cimpy.cim_import(test_files, "cgmes_v2_4_15")

    cgmes_object = cimpy.cimexport._get_class_attributes_with_references(imported_result, "cgmes_v2_4_15")

    pickle.dump(cgmes_object, open("CIGREMV_import_reference_cgmes_v2_4_15.p1", "wb"))


create_pickle()
