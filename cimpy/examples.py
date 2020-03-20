from pathlib import Path


def import_example():
    base = Path(__file__).resolve().parent.parent
    example = base / 'examples' / 'quickstart' / 'importCIGREMV.py'
    exec(open(example).read())


def export_example():
    base = Path(__file__).resolve().parent.parent
    example = base / 'examples' / 'quickstart' / 'exportCIGREMV.py'
    exec(open(example).read())


def convertToBusBranch_example():
    base = Path(__file__).resolve().parent.parent
    example = base / 'examples' / 'quickstart' / 'convertToBusBranch.py'
    exec(open(example).read())


def addExternalNetworkInjection_example():
    base = Path(__file__).resolve().parent.parent
    example = base / 'examples' / 'quickstart' / 'addExternalNetworkInjection.py'
    exec(open(example).read())
