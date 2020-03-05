import logging
import os
import cimpy


logging.basicConfig(filename='importCIGREMV.log', level=logging.INFO, filemode='w')

print(os.getcwd())
xml_files = [r"..\sampledata\CIGRE_MV\Rootnet_FULL_NE_24J13h_DI.xml",
             r"..\sampledata\CIGRE_MV\Rootnet_FULL_NE_24J13h_EQ.xml",
             r"..\sampledata\CIGRE_MV\Rootnet_FULL_NE_24J13h_SV.xml",
             r"..\sampledata\CIGRE_MV\Rootnet_FULL_NE_24J13h_TP.xml", ]

xml_files_abs = []
for file in xml_files:
    xml_files_abs.append(os.path.abspath(file))

# res = cimpy.cimread(xml_files)
import_result = cimpy.cim_import(xml_files_abs, "cgmes_v2_4_15")
print("\n\n")
results = ["ACLineSegment", "PowerTransformer", "EnergyConsumer"]
for key, value in import_result['topology'].items():
    if value.__class__.__name__ in results:
        print(value.__str__())
