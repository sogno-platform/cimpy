from .Base import Base
from .CGMESProfile import Profile


class DCPolarityKind(Base):
    """
    Polarity for DC circuits.

    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
    }

    serializationProfile = {}


    def __init__(self):

        pass

    def __str__(self):
        str = "class=DCPolarityKind\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
