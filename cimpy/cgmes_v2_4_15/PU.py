from .Base import Base
from .CGMESProfile import Profile


class PU(Base):
    """
    Per Unit - a positive or negative value referred to a defined base. Values typically range from -10 to +10.

    :multiplier:  Default: None
    :unit:  Default: None
    :value:  Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, Profile.EQ.value, Profile.SSH.value, ],
        "multiplier": [Profile.DY.value, Profile.EQ.value, Profile.SSH.value, ],
        "unit": [Profile.DY.value, Profile.EQ.value, Profile.SSH.value, ],
        "value": [Profile.DY.value, Profile.EQ.value, Profile.SSH.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value


    def __init__(self, multiplier = None, unit = None, value = 0.0):

        self.multiplier = multiplier
        self.unit = unit
        self.value = value

    def __str__(self):
        str = "class=PU\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
