from .Base import Base
from .CGMESProfile import Profile


class VsPpccControlKind(Base):
    """
    Types applicable to the control of real power and/or DC voltage by voltage source converter.

    """

    possibleProfileList = {
        "class": [Profile.SSH.value, ],
    }

    serializationProfile = {}


    def __init__(self):

        pass

    def __str__(self):
        str = "class=VsPpccControlKind\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
