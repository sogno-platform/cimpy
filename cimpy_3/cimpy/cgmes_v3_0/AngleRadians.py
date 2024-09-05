from .Base import Base


class AngleRadians(Base):
    """
    Phase angle in radians.

    :value:  Default: 0.0
    :unit:  Default: None
    :multiplier:  Default: None
    """

    cgmesProfile = Base.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.SSH.value,
        ],
        "value": [
            cgmesProfile.SSH.value,
        ],
        "unit": [
            cgmesProfile.SSH.value,
        ],
        "multiplier": [
            cgmesProfile.SSH.value,
        ],
    }

    serializationProfile = {}

    def __init__(
        self,
        value=0.0,
        unit=None,
        multiplier=None,
    ):

        self.value = value
        self.unit = unit
        self.multiplier = multiplier

    def __str__(self):
        str = "class=AngleRadians\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
