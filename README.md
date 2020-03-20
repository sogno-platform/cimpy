# CIMpy
The CIMpy package enables the import, modification and export of grid data in the format of XML/RDF documents based on the Common Information Model (CIM) specified by the IEC61970 standard.

The processing of grid data is based on CIM compatible Python classes. The codebase for the CIM compatible Python classes was generated in an automated way. A separate tool allows for an easy adaption of CIMpy and its underlying codebase.

The focus of CIMpy is on the support of the Common Grid Model Exchange Standard (CGMES) specified by the European Network of Transmission System Operators for Electricity (ENTSO-E). However, the CIMpy package can readily support further as well as new CIM versions if required.


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
cimpy.cim_import(xml_files, cgmes_version, start_dict=None)

Arguments:
    xml_files:          List of CIM RDF/XML files
    cgmes_version:      String containing the CGMES version

Optional Arguments:
    start_dict:         List of CIM classes which should be read, default: read all classes

Output:
    import_result:      A dictionary containing the topology and meta information. The topology can be extracted via
                        import_result['topology']. The topology dictionary contains all objects accessible via their mRID. The meta
                        information can be extracted via import_result['meta_info']. The meta_info dictionary contains a new dictionary with
                        the keys: 'author', 'namespaces' and 'urls'. The last two are also dictionaries. 'urls' contains a mapping
                        between references to URLs and the extracted value of the URL, e.g. 'absoluteValue':
                        'http://iec.ch/TC57/2012/CIM-schema-cim16#OperationalLimitDirectionKind.absoluteValue' These mappings are accessible
                        via the name of the attribute, e.g. import_result['meta_info']['urls'}[attr_name] = {mapping like example above}.
                        'namespaces' is a dictionary containing all RDF namespaces used in the imported xml files.
```

[Example for CIM Import](https://git.rwth-aachen.de/acs/public/cim/cimpy/blob/master/examples/quickstart/importCIGREMV.py)

## CIM Export
Function for serialization of CIMpy objects to XML files.
```
cimpy.cim_export(import_result, file_name, version, activeProfileList):

Arguments:
   import_result:       A dictionary containing the topology and meta information. For more information see the documentation for cim_import.
   file_name:           String containing the name for the XML files.
   version:             String containing the CGMES version
   activeProfileList:   A list containing all profiles which are active for the export.

Output:
    One XML file for each package in the CGMES version. The package name is added to the file name like [file_name]_[package].xml
```

[Example for CIM Export](https://git.rwth-aachen.de/acs/public/cim/cimpy/blob/master/examples/quickstart/exportCIGREMV.py)