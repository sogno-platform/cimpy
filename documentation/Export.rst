Export Example Documentation
""""""""""""""""""""""""""""

This guide demonstrates the basic usage of the function cim_export. The whole script can be found `in gitlab <https://git.rwth-aachen.de/acs/public/cim/cimpy/blob/master/examples/quickstart/exportCIGREMV.py>`_.

For this export example we use the result from the import example. The whole explanation of the import procedure can be found `in the import documentation <https://acs.pages.rwth-aachen.de/public/cim/cimpy/Import.html>`_.

.. code-block:: python

    import_result = cimpy.cim_import(xml_files, "cgmes_v2_4_15")

For the function cim_export a list containing all profiles which should be used for the export is needed. For more information about the arguments of the cim_export function see `Functions <https://acs.pages.rwth-aachen.de/public/cim/cimpy/Functions.html>`_.

.. code-block:: python

    activeProfileList = ['DI', 'EQ', 'SV', 'TP']

In the next step the objects stored in import_result are exported to XML/RDF files.

.. code-block:: python

    cimpy.cim_export(import_result, 'CIGREMV_reference_cgmes_v2_4_15', 'cgmes_v2_4_15', activeProfileList)

The XML/RDF files are generated inside the folder from which the function was called.
