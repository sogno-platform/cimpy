import logging
from pathlib import Path
import cimpy
logging.basicConfig(filename='exportCIGREMV.log', level=logging.INFO, filemode='w')

example = Path('.').resolve()
sample_folder = example / 'examples' / 'sampledata' / 'CIGRE_MV'

sample_files = sample_folder.glob('*.xml')

xml_files = []
for file in sample_folder.glob('*.xml'):
    xml_files.append(str(file.absolute()))

import_result = cimpy.cim_import(xml_files, "cgmes_v2_4_15")

activeProfileList = ['DI', 'EQ', 'SV', 'TP']

cimpy.cim_export(import_result, 'CIGREMV_reference_cgmes_v2_4_15', 'cgmes_v2_4_15', activeProfileList)
