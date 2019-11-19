import logging
import os
import cimpy
logging.basicConfig(filename='Convert_to_Bus_Branch.log', level=logging.INFO, filemode='w')

xml_files = [r"..\sampledata\Sample_Grid_Switches\Node-Breaker\20191030T0924Z_XX_YYY_DL_.xml",
             r"..\sampledata\Sample_Grid_Switches\Node-Breaker\20191030T0924Z_XX_YYY_GL_.xml",
             r"..\sampledata\Sample_Grid_Switches\Node-Breaker\20191030T0924Z_XX_YYY_SSH_.xml",
             r"..\sampledata\Sample_Grid_Switches\Node-Breaker\20191030T0924Z_XX_YYY_SV_.xml",
             r"..\sampledata\Sample_Grid_Switches\Node-Breaker\20191030T0924Z_XX_YYY_TP_.xml",
             r"..\sampledata\Sample_Grid_Switches\Node-Breaker\20191030T0924Z_YYY_EQ_.xml",]

xml_files_abs = []
for file in xml_files:
    xml_files_abs.append(os.path.abspath(file))


# res = cimpy.cimread(xml_files)
res, namespaces = cimpy.cim_import(xml_files_abs, "cimgen_v2_4_15")

bus_branch = cimpy.utils.node_breaker_to_bus_branch(res)

# dicts = cimpy.get_class_attributes_dict(res)
cimpy.cim_export(bus_branch, namespaces, 'Bus_Branch_Converted', 'cimgen_v2_4_15')