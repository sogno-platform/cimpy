import pickle
from pathlib import Path
import cimpy

tests = Path(".").resolve().parent
example_path = tests / "examples" / "sampledata" / "CIGRE_MV"


def create_pickle():

    test_files = []

    for file in example_path.glob("*.xml"):
        print("file: ", file)
        test_files.append(str(file.absolute()))

    imported_result = cimpy.cim_import(test_files, "cgmes_v2_4_15")

    CGMES_object = cimpy.cimexport._get_class_attributes_with_references(imported_result, "cgmes_v2_4_15")

    pickle.dump(CGMES_object, open("CIGREMV_import_reference_cgmes_v2_4_15.p1", "wb"))


create_pickle()
