from .Base import Base
from .CGMESProfile import Profile


class Source(Base):
    """
    Source gives information related to the origin of a value.

    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value


    def __init__(self):

        pass

    def __str__(self):
        str = "class=Source\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
