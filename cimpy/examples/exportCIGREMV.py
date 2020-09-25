import logging
from pathlib import Path
import cimpy
logging.basicConfig(filename='exportCIGREMV.log', level=logging.INFO, filemode='w')

example = Path(__file__).resolve().parent

# called as cimpy.examples.import_example() or file run from quickstart directory?
if 'cimexamples.py' in str(__file__):
    sample_folder = example / 'examples' / 'sampledata' / 'CIGRE_MV'
else:
    sample_folder = example / 'sampledata' / 'CIGRE_MV'

sample_files = sample_folder.glob('*.xml')

xml_files = []
for file in sample_folder.glob('*.xml'):
    xml_files.append(str(file.absolute()))

import_result = cimpy.cim_import(xml_files, "cgmes_v2_4_15")

activeProfileList = ['DL', 'EQ', 'SV', 'TP']

cimpy.cim_export(import_result, 'CIGREMV_reference_cgmes_v2_4_15', 'cgmes_v2_4_15', activeProfileList)
