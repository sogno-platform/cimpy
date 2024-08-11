from .Base import Base
from .CGMESProfile import Profile


class Validity(Base):
    """
    Validity for MeasurementValue.

    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
    }

    serializationProfile = {}


    def __init__(self):

        pass

    def __str__(self):
        str = "class=Validity\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
