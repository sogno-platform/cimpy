from .Base import Base
from .CGMESProfile import Profile


class Temperature(Base):
    """
    Value of temperature in degrees Celsius.

    :multiplier:  Default: None
    :unit:  Default: None
    :value:  Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, Profile.EQ.value, ],
        "multiplier": [Profile.DY.value, Profile.EQ.value, ],
        "unit": [Profile.DY.value, Profile.EQ.value, ],
        "value": [Profile.DY.value, Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value


    def __init__(self, multiplier = None, unit = None, value = 0.0):

        self.multiplier = multiplier
        self.unit = unit
        self.value = value

    def __str__(self):
        str = "class=Temperature\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str