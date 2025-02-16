from .Base import Base
from .CGMESProfile import Profile


class AsynchronousMachineKind(Base):
    """
    Kind of Asynchronous Machine.

    """

    possibleProfileList = {
        "class": [Profile.SSH.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.SSH.value


    def __init__(self):

        pass

    def __str__(self):
        str = "class=AsynchronousMachineKind\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
