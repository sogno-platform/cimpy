from .Base import Base


class PerCent(Base):
    """
    Percentage on a defined base.   For example, specify as 100 to indicate at the defined base.

    :value: Normally 0 to 100 on a defined base. Default: 0.0
    :unit:  Default: None
    :multiplier:  Default: None
    """

    cgmesProfile = Base.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.SSH.value,
            cgmesProfile.OP.value,
            cgmesProfile.EQ.value,
            cgmesProfile.SC.value,
        ],
        "value": [
            cgmesProfile.SSH.value,
            cgmesProfile.OP.value,
            cgmesProfile.EQ.value,
            cgmesProfile.SC.value,
        ],
        "unit": [
            cgmesProfile.SSH.value,
            cgmesProfile.OP.value,
            cgmesProfile.EQ.value,
            cgmesProfile.SC.value,
        ],
        "multiplier": [
            cgmesProfile.SSH.value,
            cgmesProfile.OP.value,
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
        str = "class=PerCent\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
