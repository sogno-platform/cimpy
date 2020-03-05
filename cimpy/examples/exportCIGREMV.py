import logging
import os
import cimpy


def export_example():
    logging.basicConfig(filename='exportCIGREMV.log', level=logging.INFO, filemode='w')

    cwd = os.getcwd()
    os.chdir(os.path.dirname(__file__))
    xml_files = [r"..\..\examples\sampledata\CIGRE_MV\Rootnet_FULL_NE_24J13h_DI.xml",
                 r"..\..\examples\sampledata\CIGRE_MV\Rootnet_FULL_NE_24J13h_EQ.xml",
                 r"..\..\examples\sampledata\CIGRE_MV\Rootnet_FULL_NE_24J13h_SV.xml",
                 r"..\..\examples\sampledata\CIGRE_MV\Rootnet_FULL_NE_24J13h_TP.xml", ]

    xml_files_abs = []
    for file in xml_files:
        xml_files_abs.append(os.path.abspath(file))


    # res = cimpy.cimread(xml_files)
    import_result = cimpy.cim_import(xml_files_abs, "cgmes_v2_4_15")

    activeProfileList = ['DI', 'EQ', 'SV', 'TP']

    # dicts = cimpy.get_class_attributes_dict(res)
    cimpy.cim_export(import_result, 'CIGREMV_reference_cgmes_v2_4_15', 'cgmes_v2_4_15', activeProfileList)

    os.chdir(cwd)
