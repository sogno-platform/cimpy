from .Base import Base
from .CGMESProfile import Profile


class GenericNonLinearLoadModelKind(Base):
    """
    Type of generic non-linear load model.

    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value


    def __init__(self):

        pass

    def __str__(self):
        str = "class=GenericNonLinearLoadModelKind\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
