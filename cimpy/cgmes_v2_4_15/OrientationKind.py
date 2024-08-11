from .Base import Base
from .CGMESProfile import Profile


class OrientationKind(Base):
    """
    The orientation of the coordinate system with respect to top, left, and the coordinate number system.

    """

    possibleProfileList = {
        "class": [Profile.DL.value, ],
    }

    serializationProfile = {}


    def __init__(self):

        pass

    def __str__(self):
        str = "class=OrientationKind\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
