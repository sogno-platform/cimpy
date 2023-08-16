from enum import Enum

short_profile_name = {
    "Equipment": "EQ",
    "SteadyStateHypothesis": "SSH",
    "Topology": "TP",
    "StateVariables": "SV",
    "Dynamics": "DY",
    "GeographicalLocation": "GL",
    "DiagramLayout": 'DL',
    "Operation": 'OP',
    "ShortCircuit": 'SC',
    "EquipmentBoundary": 'EQBD'
}


class Base():
    """
    Base Class for CIM
    """

    cgmesProfile = Enum("cgmesProfile", {"EQ": 0, "SSH": 1, "TP": 2, "SV": 3, "DY": 4, "GL": 5, "DL": 6, "OP": 7, "SC": 8, "EQBD": 9})

    def __init__(self, *args, **kw_args):
        pass

    def printxml(self, dict={}):
        return dict
