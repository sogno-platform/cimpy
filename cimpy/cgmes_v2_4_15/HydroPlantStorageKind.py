from .Base import Base
from .CGMESProfile import Profile


class HydroPlantStorageKind(Base):
    """
    The type of hydro power plant.

    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value


    def __init__(self):

        pass

    def __str__(self):
        str = "class=HydroPlantStorageKind\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
