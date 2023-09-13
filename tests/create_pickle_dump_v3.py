
import pickle
import sys, os
from pathlib import Path
 
sys.path.append(os.getcwd())

import cimpy


example_path = Path(os.path.join(os.path.dirname(__file__),
                                '../cimpy/examples/sampledata/CIM_LV_Simbench_Grid')).resolve()

        
print(example_path)
for file in example_path.glob('*.xml'):
    print("file: ", file)


def create_pickle():

    test_files = []

    for file in example_path.glob('*.xml'):
        print("file: ", file)
        test_files.append(str(file.absolute()))

    imported_result = cimpy.cim_import(test_files, 'cgmes_v3_0_0')

    CGMES_object = cimpy.cimexport._get_class_attributes_with_references(imported_result, 'cgmes_v3_0_0')

    pickle.dump( CGMES_object, open( 'CIM_v3_import_reference.p1', "wb" ) )

create_pickle()
