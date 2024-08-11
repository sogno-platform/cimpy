from .Base import Base
from .CGMESProfile import Profile


class Currency(Base):
    """
    Monetary currencies. Apologies for this list not being exhaustive.

    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
    }

    serializationProfile = {}


    def __init__(self):

        pass

    def __str__(self):
        str = "class=Currency\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
