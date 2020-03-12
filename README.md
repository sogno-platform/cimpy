# <img src="documentation/images/cimpy_logo.png" alt="CIMpy" width=120 />

Python package for import, modification and export of grid data in the format of XML/RDF documents based on the Common Information Model (CIM).

## Installation

To install the package in development mode, run:
```
$ git clone git@git.rwth-aachen.de:acs/public/cim/cimpy.git
$ cd cimpy
$ python setup.py develop
```
To uninstall the package:
```
$ python setup.py develop --uninstall
```
The package can be installed on user level only:
```
$ python setup.py develop --user
```

## Usage
### CIM Import
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

### CIM Export
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

## Copyright

2019, Institute for Automation of Complex Power Systems, EONERC, RWTH Aachen University

## License

This project is released under the terms of the [Mozilla Public License Version 2.0](./LICENSE).

## Contact

[![EONERC ACS Logo](https://www.fein-aachen.org/img/logos/eonerc.png)](http://www.acs.eonerc.rwth-aachen.de)

- Jan Dinkelbach <jdinkelbach@eonerc.rwth-aachen.de>

[Institute for Automation of Complex Power Systems (ACS)](http://www.acs.eonerc.rwth-aachen.de)  
[EON Energy Research Center (EONERC)](http://www.eonerc.rwth-aachen.de)  
[RWTH University Aachen, Germany](http://www.rwth-aachen.de)  