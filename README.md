# <img src="documentation/images/cimpy_logo.png" alt="CIMpy" width=120 />

The CIMpy package enables the import, modification and export of grid data in the format of XML/RDF documents based on the Common Information Model (CIM) specified by the IEC61970 standard.

The processing of grid data is based on CIM compatible Python classes. The codebase for the CIM compatible Python classes was generated in an automated way. A separate tool allows for an easy adaption of CIMpy and its underlying codebase.

The focus of CIMpy is on the support of the Common Grid Model Exchange Standard (CGMES) specified by the European Network of Transmission System Operators for Electricity (ENTSO-E). However, the CIMpy package can readily support further as well as new CIM versions if required.

## Documentation

CIMpy's documentation you can find [here](http://sogno-platform.github.io/cimpy/).
The documentation provides instructions on CIMpy's installation, getting started examples and the possibility to browse through the supported CIM class codebases.

## Development

### Developer Installation

```bash
git clone https://github.com/sogno-platform/cimpy.git
cd cimpy
pip install -e .[dev]
```

Run pre-commit checks manually:

```bash
pre-commit run --all-files
```

Install pre-commit hook to run it automatically:

```bash
pre-commit install
```

## License

This project is released under the terms of the [Apache License 2.0](./LICENSE).

## Publications

If you are using CIMpy for your research, please cite the following paper in your publications:

Dinkelbach, J., Razik, L., Mirz, M., Benigni, A., Monti, A.: Template-based generation of programming language specific code for smart grid modelling compliant with CIM and CGMES.
J. Eng. 2023, 1-13 (2022). [https://doi.org/10.1049/tje2.12208](https://doi.org/10.1049/tje2.12208)
