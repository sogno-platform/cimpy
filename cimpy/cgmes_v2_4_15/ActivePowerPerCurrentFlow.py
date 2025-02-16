from .Base import Base
from .CGMESProfile import Profile


class ActivePowerPerCurrentFlow(Base):
    """
    

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
        str = "class=ActivePowerPerCurrentFlow\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
