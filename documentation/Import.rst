Import Example Documentation
""""""""""""""""""""""""""""

This guide demonstrates the basic usage of the function cim_import. The script can be found `here <https://git.rwth-aachen.de/acs/public/cim/cimpy/blob/master/examples/quickstart/importCIGREMV.py>`_.


First import the CIMpy module and set up the logger. If there is not a file set for the logger the output is printed to the console.

.. code-block:: python

    import logging
    import cimpy
    from pathlib import Path

    logging.basicConfig(filename='importCIGREMV.log', level=logging.INFO, filemode='w')

Next we need the absolute path of the XML/RDF files.

.. code-block:: python

    example = Path('.').resolve()
    sample_folder = example / 'examples' / 'sampledata' / 'CIGRE_MV'

    sample_files = sample_folder.glob('*.xml')

    xml_files = []
    for file in sample_folder.glob('*.xml'):
        xml_files.append(str(file.absolute()))

In the next step the files given in xml_files_abs are imported:

.. code-block:: python

    import_result = cimpy.cim_import(xml_files, "cgmes_v2_4_15")

For more information about the function cim_import see `Functions <https://acs.pages.rwth-aachen.de/public/cim/cimpy/Functions.html>`_.

Finally we can print the created objects. In this example only objects of the classes ACLineSegment, PowerTransformer and EnergyConsumer are printed.

.. code-block:: python

    results = ["ACLineSegment", "PowerTransformer", "EnergyConsumer"]
    for key, value in import_result['topology'].items():
        if value.__class__.__name__ in results:
            print(value.__str__())
