from .Base import Base
from .CGMESProfile import Profile


class CapacitancePerLength(Base):
    """
    Capacitance per unit of length.

    :denominatorMultiplier:  Default: None
    :denominatorUnit:  Default: None
    :multiplier:  Default: None
    :unit:  Default: None
    :value:  Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "denominatorMultiplier": [Profile.EQ.value, ],
        "denominatorUnit": [Profile.EQ.value, ],
        "multiplier": [Profile.EQ.value, ],
        "unit": [Profile.EQ.value, ],
        "value": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value


    def __init__(self, denominatorMultiplier = None, denominatorUnit = None, multiplier = None, unit = None, value = 0.0):

        self.denominatorMultiplier = denominatorMultiplier
        self.denominatorUnit = denominatorUnit
        self.multiplier = multiplier
        self.unit = unit
        self.value = value

    def __str__(self):
        str = "class=CapacitancePerLength\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
