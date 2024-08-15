from .Base import Base
from .CGMESProfile import Profile


class Boolean(Base):
    """
    A type with the value space "true" and "false".

    """

    possibleProfileList = {
        "class": [Profile.DL.value, Profile.DY.value, Profile.EQ_BD.value, Profile.EQ.value, Profile.SV.value, Profile.SSH.value, Profile.TP_BD.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value


    def __init__(self):

        pass

    def __str__(self):
        str = "class=Boolean\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
