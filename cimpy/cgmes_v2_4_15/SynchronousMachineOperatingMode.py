from .Base import Base
from .CGMESProfile import Profile


class SynchronousMachineOperatingMode(Base):
    """
    Synchronous machine operating mode.

    """

    possibleProfileList = {
        "class": [Profile.SSH.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.SSH.value


    def __init__(self):

        pass

    def __str__(self):
        str = "class=SynchronousMachineOperatingMode\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
