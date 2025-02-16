from .DCConductingEquipment import DCConductingEquipment
from .CGMESProfile import Profile


class DCLineSegment(DCConductingEquipment):
    """
    A wire or combination of wires not insulated from one another, with consistent electrical characteristics, used to carry direct current between points in the DC region of the power system.

    :PerLengthParameter: Set of per-length parameters for this line segment. Default: None
    :capacitance: Capacitance of the DC line segment. Significant for cables only. Default: 0.0
    :inductance: Inductance of the DC line segment. Neglectable compared with DCSeriesDevice used for smoothing. Default: 0.0
    :length: Segment length for calculating line section capabilities. Default: 0.0
    :resistance: Resistance of the DC line segment. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "PerLengthParameter": [Profile.EQ.value, ],
        "capacitance": [Profile.EQ.value, ],
        "inductance": [Profile.EQ.value, ],
        "length": [Profile.EQ.value, ],
        "resistance": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class DCConductingEquipment:\n" + DCConductingEquipment.__doc__

    def __init__(self, PerLengthParameter = None, capacitance = 0.0, inductance = 0.0, length = 0.0, resistance = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.PerLengthParameter = PerLengthParameter
        self.capacitance = capacitance
        self.inductance = inductance
        self.length = length
        self.resistance = resistance

    def __str__(self):
        str = "class=DCLineSegment\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
