from .Base import Base
from .CGMESProfile import Profile


class ReactivePower(Base):
    """
    Product of RMS value of the voltage and the RMS value of the quadrature component of the current.

    :multiplier:  Default: None
    :unit:  Default: None
    :value:  Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, Profile.SV.value, Profile.SSH.value, ],
        "multiplier": [Profile.EQ.value, Profile.SV.value, Profile.SSH.value, ],
        "unit": [Profile.EQ.value, Profile.SV.value, Profile.SSH.value, ],
        "value": [Profile.EQ.value, Profile.SV.value, Profile.SSH.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value


    def __init__(self, multiplier = None, unit = None, value = 0.0):

        self.multiplier = multiplier
        self.unit = unit
        self.value = value

    def __str__(self):
        str = "class=ReactivePower\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
