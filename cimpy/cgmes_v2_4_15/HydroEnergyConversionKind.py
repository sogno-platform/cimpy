from .Base import Base
from .CGMESProfile import Profile


class HydroEnergyConversionKind(Base):
    """
    Specifies the capability of the hydro generating unit to convert energy as a generator or pump.

    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
    }

    serializationProfile = {}


    def __init__(self):

        pass

    def __str__(self):
        str = "class=HydroEnergyConversionKind\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
