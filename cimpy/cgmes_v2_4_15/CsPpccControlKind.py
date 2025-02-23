from .Base import Base
from .CGMESProfile import Profile


class CsPpccControlKind(Base):
    """
    Active power control modes for HVDC line operating as Current Source Converter.

    """

    possibleProfileList = {
        "class": [Profile.SSH.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.SSH.value


    def __init__(self):

        pass

    def __str__(self):
        str = "class=CsPpccControlKind\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
