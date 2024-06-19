import logging
import cimpy
from pathlib import Path

logging.basicConfig(filename="importCIGREMV.log", level=logging.INFO, filemode="w")

example = Path(__file__).resolve().parent

# Called as cimpy.examples.import_example() or file run from quickstart directory?
if "cimexamples.py" in str(__file__):
    sample_folder = example / "examples" / "sampledata" / "CIGRE_MV"
else:
    sample_folder = example / "sampledata" / "CIGRE_MV"
print(sample_folder)
sample_files = sample_folder.glob("*.xml")
print(sample_files)
xml_files = []
for file in sample_folder.glob("*.xml"):
    xml_files.append(str(file.absolute()))

import_result = cimpy.cim_import(xml_files, "cgmes_v2_4_15")
print("\n\n")
results = ["ACLineSegment", "PowerTransformer", "EnergyConsumer"]
for key, value in import_result["topology"].items():
    if value.__class__.__name__ in results:
        print(value.__str__())
