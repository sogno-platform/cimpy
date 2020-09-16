from enum import Enum

#TODO: this is duplicate to cgmes_v2_4_15.Base but this one is nicer

# Mapping between the profiles and their short names
short_profile_name = {
    "DiagramLayout": 'DI',
    "Dynamics": "DY",
    "Equipment": "EQ",
    "GeographicalLocation": "GL",
    "StateVariables": "SV",
    "SteadyStateHypothesis": "SSH",
    "Topology": "TP"
}
long_profile_name = {
    'DI': "DiagramLayout",
    "DY": "Dynamics",
    "EQ": "Equipment",
    "GL": "GeographicalLocation",
    "SV": "StateVariables",
    "SSH": "SteadyStateHypothesis",
    "TP": "Topology",
}


class Profile (Enum):
    """ Enum containing all CGMES profiles and their export priority
    """
    EQ = 0
    SSH = 1
    TP = 2
    SV = 3
    DY = 4
    GL = 5
    DI = 6

    def long_name(self):
        return long_profile_name[self.name]

    @classmethod
    def from_long_name(cls, long_name):
        return cls[short_profile_name[long_name]]
