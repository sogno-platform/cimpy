CIMpy
=====

CIM++ is a software project around a deserialiser library (libcimpp) for C++ objects from XML/RDF documents based on the Common Information Model (CIM) standards (i.e. IEC61970/61968/62325) for the energy sector.

The increasing complexity of ICT systems in smart grids requires a standardized data model to improve interoperability. To this aim, IEC 61970/61968/62235 specify the CIM, which defines data structures for many power system components and the relations between them. This means that CIM based software such as the CIM-to-X translators must be kept up-to date as well. First, the CIM-to-X translator has to deserialize the CIM data in the form of RDF/XML documents and present it in the form of objects, C++ objects in our specific case. To enable this with our toolchain, a CIM based data model, specified by a visual Unified Modeling Language (UML) editor, can be mapped to a compilable CIM C++ codebase. This codebase is used for the automated generation of a C++ objects deserializer library for RDF/XML documents following the UML specification. The toolchain and deserializer are implemented in the open-source project called CIM++. The deserialized C++ objects can be processed directly by another C++ program or they can be used as input to a serializer, which converts them into another data format.

It includes a toolchain for an automated generation of the CIM++ Deserializer from ontologies specified by CIM UML. Currently the CIM++ Deserializer is distributed via GitHub and the generation toolchain will follow.

Installation
-------------
For the installation of CIMpy take a look at the `installation instructions <https://acs.pages.rwth-aachen.de/public/cim/cimpy/Install.html>`__.


Getting Started
---------------
A quickstart guide with examples and explanations of the functions inside this package can be found `here <https://acs.pages.rwth-aachen.de/public/cim/cimpy/Usage.html>`__.


Contact
-------------

- `Jan Dinkelbach <jdinkelbach@eonerc.rwth-aachen.de>`__

.. toctree::
   :maxdepth: 2
   :hidden:

   Install
   Started
   Versions