from .Base import Base


class RealEnergy(Base):
    """
    Real electrical energy.

    :multiplier:  Default: None
    :unit:  Default: None
    :value:  Default: 0.0
    """

    cgmesProfile = Base.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
        ],
        "multiplier": [
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
        ],
        "unit": [
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
        ],
        "value": [
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    def __init__(
        self,
        multiplier=None,
        unit=None,
        value=0.0,
    ):

        self.multiplier = multiplier
        self.unit = unit
        self.value = value

    def __str__(self):
        str = "class=RealEnergy\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
