from .Base import Base
from .CGMESProfile import Profile


class ExcST7BOELselectorKind(Base):
    """
    Type of connection for the OEL input used for static excitation systems type 7B.

    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
    }

    serializationProfile = {}


    def __init__(self):

        pass

    def __str__(self):
        str = "class=ExcST7BOELselectorKind\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
