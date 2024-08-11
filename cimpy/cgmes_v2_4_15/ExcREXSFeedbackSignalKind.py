from .Base import Base
from .CGMESProfile import Profile


class ExcREXSFeedbackSignalKind(Base):
    """
    Type of rate feedback signals.

    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
    }

    serializationProfile = {}


    def __init__(self):

        pass

    def __str__(self):
        str = "class=ExcREXSFeedbackSignalKind\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
