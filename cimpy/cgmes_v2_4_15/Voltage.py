from .Base import Base
from .CGMESProfile import Profile


class Voltage(Base):
    """
    Electrical voltage, can be both AC and DC.

    :multiplier:  Default: None
    :unit:  Default: None
    :value:  Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ_BD.value, Profile.EQ.value, Profile.SV.value, Profile.SSH.value, ],
        "multiplier": [Profile.EQ_BD.value, Profile.EQ.value, Profile.SV.value, Profile.SSH.value, ],
        "unit": [Profile.EQ_BD.value, Profile.EQ.value, Profile.SV.value, Profile.SSH.value, ],
        "value": [Profile.EQ_BD.value, Profile.EQ.value, Profile.SV.value, Profile.SSH.value, ],
    }

    serializationProfile = {}


    def __init__(self, multiplier = None, unit = None, value = 0.0):

        self.multiplier = multiplier
        self.unit = unit
        self.value = value

    def __str__(self):
        str = "class=Voltage\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
