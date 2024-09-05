from enum import Enum

short_profile_name = {
    "Equipment": "EQ",
    "SteadyStateHypothesis": "SSH",
    "Topology": "TP",
    "StateVariables": "SV",
    "Dynamics": "DY",
    "GeographicalLocation": "GL",
    "DiagramLayout": "DL",
    "Operation": "OP",
    "ShortCircuit": "SC",
    "EquipmentBoundary": "EQBD",
}

long_profile_name = {
    "EQ": "Equipment",
    "SSH": "SteadyStateHypothesis",
    "TP": "Topology",
    "SV": "StateVariables",
    "DY": "Dynamics",
    "GL": "GeographicalLocation",
    "DL": "DiagramLayout",
    "OP": "Operation",
    "SC": "ShortCircuit",
    "EQBD": "EquipmentBoundary",
}


class Profile(Enum):
    """Enum containing all CGMES profiles and their export priority."""

    EQ = 0
    SSH = 1
    TP = 2
    SV = 3
    DY = 4
    GL = 5
    DL = 6
    OP = 7
    SC = 8
    EQBD = 9

    def long_name(self):
        """Testdocumentation"""
        return long_profile_name[self.name]

    @classmethod
    def from_long_name(cls, long_name):
        return cls[short_profile_name[long_name]]


class Base:
    """
    Base Class for CIM
    """

    cgmesProfile = Enum(
        "cgmesProfile",
        {
            "EQ": 0,
            "SSH": 1,
            "TP": 2,
            "SV": 3,
            "DY": 4,
            "GL": 5,
            "DL": 6,
            "OP": 7,
            "SC": 8,
            "EQBD": 9,
        },
    )

    def __init__(self, *args, **kw_args):
        pass

    def printxml(self, dict={}):
        return dict
