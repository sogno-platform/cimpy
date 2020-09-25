from pathlib import Path


def import_example():
    """TODO: Add documentation
    """
    base = Path(__file__).resolve().parent
    example = base / 'examples' / 'importCIGREMV.py'
    exec(open(example).read())


def export_example():
    """TODO: Add documentation
    """
    base = Path(__file__).resolve().parent
    example = base / 'examples' / 'exportCIGREMV.py'
    exec(open(example).read())


def convertToBusBranch_example():
    """TODO: Add documentation
    """
    base = Path(__file__).resolve().parent
    example = base / 'examples' / 'convertToBusBranch.py'
    exec(open(example).read())


def addExternalNetworkInjection_example():
    """TODO: Add documentation
    """
    base = Path(__file__).resolve().parent
    example = base / 'examples' / 'addExternalNetworkInjection.py'
    exec(open(example).read())
