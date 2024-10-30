from .Base import Base
from .CGMESProfile import Profile


class GeneratorControlSource(Base):
    """
    The source of controls for a generating unit.

    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value


    def __init__(self):

        pass

    def __str__(self):
        str = "class=GeneratorControlSource\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
