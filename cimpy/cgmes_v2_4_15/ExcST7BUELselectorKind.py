from .Base import Base
from .CGMESProfile import Profile


class ExcST7BUELselectorKind(Base):
    """
    Type of connection for the UEL input used for static excitation systems type 7B.

    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
    }

    serializationProfile = {}


    def __init__(self):

        pass

    def __str__(self):
        str = "class=ExcST7BUELselectorKind\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
