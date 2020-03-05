Import Example Documentation
""""""""""""""""""""""""""""

This guide demonstrates the basic usage of the function cim_import. The script can be found `here <https://git.rwth-aachen.de/acs/public/cim/cimpy/blob/master/examples/quickstart/importCIGREMV.py>`_.


First import the CIMpy module and set up the logger. If there is not a file set for the logger the output is printed to the console.

.. code-block:: python

    import cimpy
    import logging
    import os

    logging.basicConfig(filename='importCIGREMV.log', level=logging.INFO, filemode='w')

Next we need the absolute path of the XML/RDF files.

.. code-block:: python

    xml_files = [r"..\sampledata\CIGRE_MV\CIGRE_MV_Rudion_With_LoadFLow_Results\Rootnet_FULL_NE_24J13h_EQ.xml",
                 r"..\sampledata\CIGRE_MV\CIGRE_MV_Rudion_With_LoadFLow_Results\Rootnet_FULL_NE_24J13h_SV.xml",
                 r"..\sampledata\CIGRE_MV\CIGRE_MV_Rudion_With_LoadFLow_Results\Rootnet_FULL_NE_24J13h_TP.xml", ]

    xml_files_abs = []
    for file in xml_files:
        xml_files_abs.append(os.path.abspath(file))

In the next step the files given in xml_files_abs are imported:

.. code-block:: python

    import_result = cimpy.cim_import(xml_files_abs, "cgmes_v2_4_15")

For more information about the function cim_import see `Functions <https://acs.pages.rwth-aachen.de/public/cim/cimpy/Functions.html>`_.

Finally we can print the created objects. In this example only objects of the classes ACLineSegment, PowerTransformer and EnergyConsumer are printed.

.. code-block:: python

    results = ["ACLineSegment", "PowerTransformer", "EnergyConsumer"]
    for key, value in import_result['topology'].items():
        if value.__class__.__name__ in results:
            print(value.__str__())
