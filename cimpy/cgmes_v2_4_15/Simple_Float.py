from .Base import Base
from .CGMESProfile import Profile


class Simple_Float(Base):
    """
    A floating point number. The range is unspecified and not limited.

    :value:  Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DL.value, Profile.DY.value, Profile.EQ.value, Profile.SV.value, Profile.SSH.value, ],
        "value": [Profile.DL.value, Profile.DY.value, Profile.EQ.value, Profile.SV.value, Profile.SSH.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value


    def __init__(self, value = 0.0):

        self.value = value

    def __str__(self):
        str = "class=Simple_Float\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
