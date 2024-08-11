from .Base import Base
from .CGMESProfile import Profile


class Integer(Base):
    """
    An integer number. The range is unspecified and not limited.

    """

    possibleProfileList = {
        "class": [Profile.DL.value, Profile.DY.value, Profile.EQ.value, Profile.GL.value, Profile.SSH.value, ],
    }

    serializationProfile = {}


    def __init__(self):

        pass

    def __str__(self):
        str = "class=Integer\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
