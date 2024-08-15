from .Base import Base
from .CGMESProfile import Profile


class ActivePower(Base):
    """
    Product of RMS value of the voltage and the RMS value of the in-phase component of the current.

    :multiplier:  Default: None
    :unit:  Default: None
    :value:  Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, Profile.EQ.value, Profile.SV.value, Profile.SSH.value, ],
        "multiplier": [Profile.DY.value, Profile.EQ.value, Profile.SV.value, Profile.SSH.value, ],
        "unit": [Profile.DY.value, Profile.EQ.value, Profile.SV.value, Profile.SSH.value, ],
        "value": [Profile.DY.value, Profile.EQ.value, Profile.SV.value, Profile.SSH.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value


    def __init__(self, multiplier = None, unit = None, value = 0.0):

        self.multiplier = multiplier
        self.unit = unit
        self.value = value

    def __str__(self):
        str = "class=ActivePower\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
