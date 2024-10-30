from .Base import Base
from .CGMESProfile import Profile


class PerCent(Base):
    """
    Percentage on a defined base.   For example, specify as 100 to indicate at the defined base.

    :multiplier:  Default: None
    :unit:  Default: None
    :value: Normally 0 - 100 on a defined base Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, Profile.SSH.value, ],
        "multiplier": [Profile.EQ.value, Profile.SSH.value, ],
        "unit": [Profile.EQ.value, Profile.SSH.value, ],
        "value": [Profile.EQ.value, Profile.SSH.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value


    def __init__(self, multiplier = None, unit = None, value = 0.0):

        self.multiplier = multiplier
        self.unit = unit
        self.value = value

    def __str__(self):
        str = "class=PerCent\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
