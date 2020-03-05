from pathlib import Path


def import_example():
    base = Path(__file__).resolve().parent.parent
    example = base / 'examples' / 'quickstart' / 'importCIGREMV.py'
    exec(open(example).read())


def export_example():
    base = Path(__file__).resolve().parent.parent
    example = base / 'examples' / 'quickstart' / 'exportCIGREMV.py'
    exec(open(example).read())