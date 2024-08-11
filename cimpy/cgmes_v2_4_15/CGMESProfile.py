from enum import Enum


# Mapping between the profiles and their short names
short_profile_name = {
    "Equipment": "EQ",
    "DiagramLayout": "DL",
    "Dynamics": "DY",
    "EquipmentBoundary": "EQ_BD",
    "GeographicalLocation": "GL",
    "SteadyStateHypothesis": "SSH",
    "StateVariables": "SV",
    "Topology": "TP",
    "TopologyBoundary": "TP_BD",
}
long_profile_name = {
    "EQ": "Equipment",
    "DL": "DiagramLayout",
    "DY": "Dynamics",
    "EQ_BD": "EquipmentBoundary",
    "GL": "GeographicalLocation",
    "SSH": "SteadyStateHypothesis",
    "SV": "StateVariables",
    "TP": "Topology",
    "TP_BD": "TopologyBoundary",
}
profile_uris = {
    "EQ": [
        "http://entsoe.eu/CIM/EquipmentCore/3/1",
        "http://entsoe.eu/CIM/EquipmentOperation/3/1",
        "http://entsoe.eu/CIM/EquipmentShortCircuit/3/1",
    ],
    "DL": [
        "http://entsoe.eu/CIM/DiagramLayout/3/1",
    ],
    "DY": [
        "http://entsoe.eu/CIM/Dynamics/3/1",
    ],
    "EQ_BD": [
        "http://entsoe.eu/CIM/EquipmentBoundary/3/1",
        "http://entsoe.eu/CIM/EquipmentBoundaryOperation/3/1",
    ],
    "GL": [
        "http://entsoe.eu/CIM/GeographicalLocation/2/1",
    ],
    "SSH": [
        "http://entsoe.eu/CIM/SteadyStateHypothesis/1/1",
    ],
    "SV": [
        "http://entsoe.eu/CIM/StateVariables/4/1",
    ],
    "TP": [
        "http://entsoe.eu/CIM/Topology/4/1",
    ],
    "TP_BD": [
        "http://entsoe.eu/CIM/TopologyBoundary/3/1",
    ],
}


class Profile(Enum):
    """Enum containing all CGMES profiles and their export priority."""

    EQ = 0
    DL = 1
    DY = 2
    EQ_BD = 3
    GL = 4
    SSH = 5
    SV = 6
    TP = 7
    TP_BD = 8

    def long_name(self):
        return long_profile_name[self.name]

    @classmethod
    def from_long_name(cls, long_name):
        return cls[short_profile_name[long_name]]


cim_namespace = "http://iec.ch/TC57/2013/CIM-schema-cim16#"
