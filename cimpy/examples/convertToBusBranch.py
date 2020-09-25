import logging
import cimpy
from pathlib import Path

logging.basicConfig(filename='Convert_to_Bus_Branch.log', level=logging.INFO, filemode='w')

example = Path(__file__).resolve().parent

# called as cimpy.examples.convertBusBranch() or file run from quickstart directory?
if 'cimexamples.py' in str(__file__):
    sample_folder = example / 'examples' / 'sampledata' / 'Sample_Grid_Switches' / 'Node-Breaker'
else:
    sample_folder = example / 'sampledata' / 'Sample_Grid_Switches' / 'Node-Breaker'

sample_files = sample_folder.glob('*.xml')

xml_files = []
for file in sample_folder.glob('*.xml'):
    xml_files.append(str(file.absolute()))


import_result = cimpy.cim_import(xml_files, "cgmes_v2_4_15")

import_result = cimpy.utils.node_breaker_to_bus_branch(import_result)

activeProfileList = ['DL', 'EQ', 'TP']

cimpy.cim_export(import_result, 'Bus_Branch_Converted', 'cgmes_v2_4_15', activeProfileList)
