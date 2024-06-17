from pathlib import Path


def import_example():
    """TODO: Add documentation"""
    base = Path(__file__).resolve().parent
    example = base / "examples" / "import_cigre_mv.py"
    exec(open(example).read())


def export_example():
    """TODO: Add documentation"""
    base = Path(__file__).resolve().parent
    example = base / "examples" / "export_cigre_mv.py"
    exec(open(example).read())


def convert_to_bus_branch_example():
    """TODO: Add documentation"""
    base = Path(__file__).resolve().parent
    example = base / "examples" / "convert_to_bus_branch.py"
    exec(open(example).read())


def add_external_network_injection_example():
    """TODO: Add documentation"""
    base = Path(__file__).resolve().parent
    example = base / "examples" / "add_external_network_injection.py"
    exec(open(example).read())
