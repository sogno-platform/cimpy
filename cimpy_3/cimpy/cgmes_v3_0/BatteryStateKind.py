from .Base import Base


class BatteryStateKind(Base):
    """
    The state of the battery unit.

    """

    cgmesProfile = Base.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.SSH.value,
        ],
    }

    serializationProfile = {}

    def __init__(
        self,
    ):

        pass

    def __str__(self):
        str = "class=BatteryStateKind\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
