from .Base import Base
from .CGMESProfile import Profile


class Decimal(Base):
    """
    Decimal is the base-10 notational system for representing real numbers.

    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
    }

    serializationProfile = {}


    def __init__(self):

        pass

    def __str__(self):
        str = "class=Decimal\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
