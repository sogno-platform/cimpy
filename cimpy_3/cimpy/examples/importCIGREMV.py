import logging
import cimpy
from pathlib import Path

logging.basicConfig(filename="importCIGREMV.log", level=logging.INFO, filemode="w")

example = Path(__file__).resolve().parent

# called as cimpy.examples.import_example() or file run from quickstart directory?
if "cimexamples.py" in str(__file__):
    sample_folder = example / "examples" / "sampledata" / "LV_SIMBENCH_3_0"
else:
    sample_folder = example / "sampledata" / "LV_SIMBENCH_3_0"
print(sample_folder)
sample_files = sample_folder.glob("*.xml")
print(sample_files)
xml_files = []
for file in sample_folder.glob("*.xml"):
    xml_files.append(str(file.absolute()))

import_result = cimpy.cim_import(xml_files, "cgmes_v3_0")
print("\n\n")
