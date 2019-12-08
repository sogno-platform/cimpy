Welcome to cimpy's documentation!
==================================

Cimpy is a tool for generation of CIM data.

Package Content
===============

An overview with all classes sorted by class name can be found in the :ref:`genindex` and one sorted by version can be found in the :ref:`modindex`. You can also use the search bar on the left.

.. toctree::
   :maxdepth: 1

   cimpy


Installation
============

.. code-block:: bash

   $ git clone https://git.rwth-aachen.de/acs/public/cim/cimpy
   $ cd cimpy
   $ python setup.py develop

Usage
=====

CIM Import
""""""""""

Function for creating CIMpy objects out of a CIM topology.

.. code-block::

   cimpy.cim_import(xml_files, cim_version, start_dict=None)

Arguments:
    :xml_files:      List of CIM RDF/XML files
    :cim_version:    String containing the CGMES version

Optional Arguments:
    :start_dict:     List of CIM classes which should be read, default: read all classes

Output:
    :res:            A map containing the CIMpy objects with the UUID as map key

`Example for CIM Import <https://git.rwth-aachen.de/acs/public/cim/cimpy/blob/master/examples/quickstart/readCIGREMV.py>`_

CIM Export
""""""""""

Function for serialization of CIMpy objects to XML files.

.. code-block::

   cimpy.cim_export(res, namespaces_dict, file_name, version, acitiveProfileList):

Arguments:
   :res:                A dictionary containing all CIMpy objects accessible via the UUID
   :namespaces_dict:    A dictionary containing the namespaces of the original XML files
   :file_name:          String containing the name for the XML files.
   :version:            String containing the CGMES version
   :activeProfileList:  A list containing all profiles which are active for the export

Output:
    One XML file for each package in the CGMES version. The package name is added to the file name like [file_name]_[package].xml


`Example for CIM Generate <https://git.rwth-aachen.de/acs/public/cim/cimpy/blob/master/examples/quickstart/exportCIGREMV.py>`_
