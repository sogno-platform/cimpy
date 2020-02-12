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
    :import_result:  A dictionary containing the topology and meta information. The topology can be extracted via
    import_result['topology']. The topology dictionary contains all CIMpy objects accessible via their mRID. The meta
    information can be extracted via import_result['meta_info']. The meta_info dictionary contains a new dictionary with
    the keys: 'author', 'namespaces' and 'urls'. The last two are also dictionaries. 'urls' contains a mapping
    between references to URLs and the extracted value of the URL, e.g. 'absoluteValue':
    'http://iec.ch/TC57/2012/CIM-schema-cim16#OperationalLimitDirectionKind.absoluteValue' These mappings are accessible
    via the name of the attribute, e.g. import_result['meta_info']['urls'}[attr_name] = {mapping like example above}.
    'namespaces' is a dictionary containing all RDF namespaces used in the imported xml files.

`Example for CIM Import <https://git.rwth-aachen.de/acs/public/cim/cimpy/blob/master/examples/quickstart/importCIGREMV.py>`_

CIM Export
""""""""""

Function for serialization of CIMpy objects to XML files.

.. code-block::

   cimpy.cim_export(import_result, file_name, version, acitiveProfileList):

Arguments:
   :import_result:      A dictionary containing the topology and meta information. The topology can be extracted via
    import_result['topology']. The topology dictionary contains all CIMpy objects accessible via their mRID. The meta
    information can be extracted via import_result['meta_info']. The meta_info dictionary contains a new dictionary with
    the keys: 'author', 'namespaces' and 'urls'. The last two are also dictionaries. 'urls' contains a mapping
    between references to URLs and the extracted value of the URL, e.g. 'absoluteValue':
    'http://iec.ch/TC57/2012/CIM-schema-cim16#OperationalLimitDirectionKind.absoluteValue' These mappings are accessible
    via the name of the attribute, e.g. import_result['meta_info']['urls'}[attr_name] = {mapping like example above}.
    'namespaces' is a dictionary containing all RDF namespaces used in the imported xml files.
   :file_name:          String containing the name for the XML files.
   :version:            String containing the CGMES version
   :activeProfileList:  A list containing all profiles which are active for the export

Output:
    One XML file for each package in the CGMES version. The package name is added to the file name like [file_name]_[package].xml


`Example for CIM Generate <https://git.rwth-aachen.de/acs/public/cim/cimpy/blob/master/examples/quickstart/exportCIGREMV.py>`_
