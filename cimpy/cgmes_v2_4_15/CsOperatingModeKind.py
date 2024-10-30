from .Base import Base
from .CGMESProfile import Profile


class CsOperatingModeKind(Base):
    """
    Operating mode for HVDC line operating as Current Source Converter.

    """

    possibleProfileList = {
        "class": [Profile.SSH.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.SSH.value


    def __init__(self):

        pass

    def __str__(self):
        str = "class=CsOperatingModeKind\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
