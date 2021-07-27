Getting Started
"""""""""""""""

After installing the package you can run the following examples.

Import Example
--------------

For a quick example for the import just run

.. code-block:: python

    import cimpy

    cimpy.import_example()

This example imports grid data stored in XML/RDF files and prints a subset of the created objects. For deeper insights into the example check the import example documentation:

.. toctree::
    :glob:

    Import

Export Example
--------------

For a quick example for the export just run

.. code-block:: python

    import cimpy

    cimpy.export_example()

This example uses the import result of the import example and exports them back to RDF/XML files. For deeper insights into the example check the export example documentation:

.. toctree::
    :glob:

    Export

Utils
-----
Currently there are two functions in utils.

.. toctree::
    :glob:

    utils


Add External Network injection
______________________________

The function add_external_network_injection adds an external network injection to an existing node. An example for this function can be run with:

.. code-block:: python

    import cimpy

    cimpy.addExternalNetworkInjection_example()

Convert Node-Breaker to Bus-Branch
__________________________________

This function converts grid data in Node-Breaker topology into Bus-Branch topology.

.. code-block:: python

    import cimpy

    cimpy.convertToBusBranch_example()
