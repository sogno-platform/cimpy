from .Base import Base
from .CGMESProfile import Profile


class UnitSymbol(Base):
    """
    The units defined for usage in the CIM.

    """

    possibleProfileList = {
        "class": [Profile.DL.value, Profile.DY.value, Profile.EQ_BD.value, Profile.EQ.value, Profile.SV.value, Profile.SSH.value, ],
    }

    serializationProfile = {}


    def __init__(self):

        pass

    def __str__(self):
        str = "class=UnitSymbol\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
