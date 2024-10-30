from .Base import Base
from .CGMESProfile import Profile


class Area(Base):
    """
    Area.

    :multiplier:  Default: None
    :unit:  Default: None
    :value:  Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "multiplier": [Profile.DY.value, ],
        "unit": [Profile.DY.value, ],
        "value": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value


    def __init__(self, multiplier = None, unit = None, value = 0.0):

        self.multiplier = multiplier
        self.unit = unit
        self.value = value

    def __str__(self):
        str = "class=Area\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
