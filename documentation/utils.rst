Utils
"""""
This part of the package provides two basic functions to modify the imported CIM data.

Convert Node-Breaker to Bus-Branch
----------------------------------
This function converts as the name suggests a Node-Breaker topology into a Bus-Branch topology.

First we have to import the grid data. For more information see the documentation of the import function.

.. code-block:: python

    import logging
    import cimpy
    from pathlib import Path

    logging.basicConfig(filename='importCIGREMV.log', level=logging.INFO, filemode='w')

    example = Path('.').resolve()
    sample_folder = example / 'examples' / 'sampledata' / 'Sample_Grid_Switches' / 'Bus-Branch'

    sample_files = sample_folder.glob('*.xml')

    xml_files = []
    for file in sample_folder.glob('*.xml'):
        xml_files.append(str(file.absolute()))

    import_result = cimpy.cim_import(xml_files, "cgmes_v2_4_15")

Now we can convert the imported topology into a Bus-Branch topology.

.. code-block:: python

    import_result = cimpy.utils.node_breaker_to_bus_branch(import_result)

The converted grid data is stored in import_result['topology']

Add external network injection
------------------------------

This function adds an external network injection to the imported grid data. First we have to import some grid data. Here we use the same data as the import example. The imported data is stored in import_example.

To add the external network injection we need the mRID of either a Topological Node or a Connectivity Node.

.. code-block:: python

    import_result = cimpy.cim_import(xml_files, "cgmes_v2_4_15")
    import_result = cimpy.utils.add_external_network_injection(import_result, "cgmes_v2_4_15", "N1", 20.0)

Here the the external network injection is added to the node with the mRID "N1" with a voltage set point of 20.0. For this function the CIM version must also be given to the function.

After the injection is added the modified grid data can be exported with cim_export.

.. code-block:: python

    activeProfileList = ['DI', 'EQ', 'SV', 'TP']
    cimpy.cim_export(import_result, 'ExternalInjection', 'cgmes_v2_4_15', activeProfileList)
