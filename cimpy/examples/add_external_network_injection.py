import logging
import cimpy
from pathlib import Path

logging.basicConfig(filename="importCIGREMV.log", level=logging.INFO, filemode="w")

example = Path(__file__).resolve().parent

# Called as cimpy.examples.convert_to_bus_branch() or file run from quickstart directory?
if "cimexamples.py" in str(__file__):
    sample_folder = example / "examples" / "sampledata" / "CIGRE_MV"
else:
    sample_folder = example / "sampledata" / "CIGRE_MV"

sample_files = sample_folder.glob("*.xml")

xml_files = []
for file in sample_folder.glob("*.xml"):
    xml_files.append(str(file.absolute()))

import_result = cimpy.cim_import(xml_files, "cgmes_v2_4_15")

import_result = cimpy.utils.add_external_network_injection(import_result, "cgmes_v2_4_15", "N1", 20.0)

active_profile_list = ["DL", "EQ", "SV", "TP"]

cimpy.cim_export(import_result, "ExternalInjection", "cgmes_v2_4_15", active_profile_list)
