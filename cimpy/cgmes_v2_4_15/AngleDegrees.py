from .Base import Base
from .CGMESProfile import Profile


class AngleDegrees(Base):
    """
    Measurement of angle in degrees.

    :multiplier:  Default: None
    :unit:  Default: None
    :value:  Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DL.value, Profile.DY.value, Profile.EQ.value, Profile.SV.value, Profile.SSH.value, ],
        "multiplier": [Profile.DL.value, Profile.DY.value, Profile.EQ.value, Profile.SV.value, Profile.SSH.value, ],
        "unit": [Profile.DL.value, Profile.DY.value, Profile.EQ.value, Profile.SV.value, Profile.SSH.value, ],
        "value": [Profile.DL.value, Profile.DY.value, Profile.EQ.value, Profile.SV.value, Profile.SSH.value, ],
    }

    serializationProfile = {}


    def __init__(self, multiplier = None, unit = None, value = 0.0):

        self.multiplier = multiplier
        self.unit = unit
        self.value = value

    def __str__(self):
        str = "class=AngleDegrees\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
