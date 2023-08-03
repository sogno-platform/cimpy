from enum import Enum

short_profile_name = {
    "DiagramLayout": 'DL',
    "Dynamics": "DY",
    "Equipment": "EQ",
    "GeographicalLocation": "GL",
    "StateVariables": "SV",
    "SteadyStateHypothesis": "SSH",
    "Topology": "TP"
}


class Base():
    """
    Base Class for CIM
    """

    cgmesProfile = Enum("cgmesProfile", {"EQ": 0, "SSH": 1, "TP": 2, "SV": 3, "DY": 4, "GL": 5, "DL": 6, "TP_BD": 7, "EQ_BD": 8, "OP": 9, "SC": 10, "EQBD": 11})

    def __init__(self, *args, **kw_args):
        pass

    def printxml(self, dict={}):
        return dict
