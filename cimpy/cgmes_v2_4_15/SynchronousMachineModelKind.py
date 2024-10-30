from .Base import Base
from .CGMESProfile import Profile


class SynchronousMachineModelKind(Base):
    """
    Type of synchronous machine model used in Dynamic simulation applications.

    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value


    def __init__(self):

        pass

    def __str__(self):
        str = "class=SynchronousMachineModelKind\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
