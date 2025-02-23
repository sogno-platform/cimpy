from .Base import Base
from .CGMESProfile import Profile


class ExcIEEEST1AUELselectorKind(Base):
    """
    Type of connection for the UEL input used in ExcIEEEST1A.

    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value


    def __init__(self):

        pass

    def __str__(self):
        str = "class=ExcIEEEST1AUELselectorKind\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
