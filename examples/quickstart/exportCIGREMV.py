import logging
import os
import cimpy
logging.basicConfig(filename='exportCIGREMV.log', level=logging.INFO, filemode='w')

xml_files = [r"..\sampledata\CIGRE_MV\Rootnet_FULL_NE_24J13h_DI.xml",
             r"..\sampledata\CIGRE_MV\Rootnet_FULL_NE_24J13h_EQ.xml",
             r"..\sampledata\CIGRE_MV\Rootnet_FULL_NE_24J13h_SV.xml",
             r"..\sampledata\CIGRE_MV\Rootnet_FULL_NE_24J13h_TP.xml", ]


xml_files_abs = []
for file in xml_files:
    xml_files_abs.append(os.path.abspath(file))


# res = cimpy.cimread(xml_files)
import_result = cimpy.cim_import(xml_files_abs, "cgmes_v2_4_15")

activeProfileList = ['DI', 'EQ', 'SV', 'TP']

# dicts = cimpy.get_class_attributes_dict(res)
cimpy.cim_export(import_result, 'CIGREMV_reference_cgmes_v2_4_15', 'cgmes_v2_4_15', activeProfileList)
