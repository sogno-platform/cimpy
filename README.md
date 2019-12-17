# CIMgen
Python tool for generation and modification of CIM data

# Installation
```
$ git clone git@git.rwth-aachen.de:acs/public/cim/cimpy.git
$ cd cimpy
$ python setup.py develop
```

# Usage
## CIM Import
Function for creating CIMpy objects out of a CIM topology.
```
cimpy.cim_import(xml_files, cim_version, start_dict=None)

Arguments:
    xml_files:          List of CIM RDF/XML files
    cim_version:        String containing the CIM version

Optional Arguments:
    start_dict:         List of CIM classes which should be read, default: read all classes

Output:
    res:                A map containing the CIMpy objects with the UUID as map key
```

[Example for CIM Import](https://git.rwth-aachen.de/acs/public/cim/cimpy/blob/master/examples/quickstart/importCIGREMV.py)

## CIM Export
Function for serialization of CIMpy objects to XML files.
```
cimpy.cim_export(res, namespaces_dict, file_name, version):

Arguments:
   res:                 A dictionary containing all CIMpy objects accessible via the UUID
   namespaces_dict:     A dictionary containing the namespaces of the original XML files
   file_name:           String containing the name for the XML files.
   version:             String containing the CGMES version

Output:
    One XML file for each package in the CGMES version. The package name is added to the file name like [file_name]_[package].xml
```

[Example for CIM Export](https://git.rwth-aachen.de/acs/public/cim/cimpy/blob/master/examples/quickstart/exportCIGREMV.py)