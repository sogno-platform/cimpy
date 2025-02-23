from .Base import Base
from .CGMESProfile import Profile


class ExcST6BOELselectorKind(Base):
    """
    Type of connection for the OEL input used for static excitation systems type 6B.

    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value


    def __init__(self):

        pass

    def __str__(self):
        str = "class=ExcST6BOELselectorKind\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
