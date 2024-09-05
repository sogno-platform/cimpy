from .Base import Base


class WindUVRTQcontrolModeKind(Base):
    """
    UVRT Q control modes <i>M</i><i><sub>qUVRT</sub></i><i>.</i>

    """

    cgmesProfile = Base.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    def __init__(
        self,
    ):

        pass

    def __str__(self):
        str = "class=WindUVRTQcontrolModeKind\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
