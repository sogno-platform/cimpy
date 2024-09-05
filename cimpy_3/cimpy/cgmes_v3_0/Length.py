from .Base import Base


class Length(Base):
    """
    Unit of length. It shall be a positive value or zero.

    :value:  Default: 0.0
    :unit:  Default: None
    :multiplier:  Default: None
    """

    cgmesProfile = Base.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
            cgmesProfile.EQ.value,
            cgmesProfile.SC.value,
        ],
        "value": [
            cgmesProfile.DY.value,
            cgmesProfile.EQ.value,
            cgmesProfile.SC.value,
        ],
        "unit": [
            cgmesProfile.DY.value,
            cgmesProfile.EQ.value,
            cgmesProfile.SC.value,
        ],
        "multiplier": [
            cgmesProfile.DY.value,
            cgmesProfile.EQ.value,
            cgmesProfile.SC.value,
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
        str = "class=Length\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
