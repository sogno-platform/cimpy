from enum import Enum

# Mapping between the profiles and their short names
short_profile_name = {
    "DiagramLayout": 'DL',
    "Dynamics": "DY",
    "Equipment": "EQ",
    "GeographicalLocation": "GL",
    "StateVariables": "SV",
    "SteadyStateHypothesis": "SSH",
    "Topology": "TP"
}
long_profile_name = {
    'DL': "DiagramLayout",
    'DI': "DiagramLayout",
    "DY": "Dynamics",
    "EQ": "Equipment",
    "GL": "GeographicalLocation",
    "SV": "StateVariables",
    "SSH": "SteadyStateHypothesis",
    "TP": "Topology",
}


class Profile (Enum):
    """ Enum containing all CGMES profiles and their export priority.
    """
    EQ = 0
    SSH = 1
    TP = 2
    SV = 3
    DY = 4
    GL = 5
    DI = 6
    DL = 7
    TP_BD = 8
    EQ_BD = 9

    def long_name(self):
        """Testdocumentation
        """
        return long_profile_name[self.name]

    @classmethod
    def from_long_name(cls, long_name):
        return cls[short_profile_name[long_name]]


class Base():
    """
    Base Class for CIM
    """

    cgmesProfile = Profile

    def __init__(self, *args, **kw_args):
        pass

    def printxml(self, dict={}):
        return dict
