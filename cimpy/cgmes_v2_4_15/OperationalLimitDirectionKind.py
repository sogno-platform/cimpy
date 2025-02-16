from .Base import Base
from .CGMESProfile import Profile


class OperationalLimitDirectionKind(Base):
    """
    The direction attribute describes the side of  a limit that is a violation.

    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value


    def __init__(self):

        pass

    def __str__(self):
        str = "class=OperationalLimitDirectionKind\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
