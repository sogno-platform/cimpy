from .Base import Base


class AngleDegrees(Base):
    """
    Measurement of angle in degrees.

    :value:  Default: 0.0
    :unit:  Default: None
    :multiplier:  Default: None
    """

    cgmesProfile = Base.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
            cgmesProfile.SSH.value,
            cgmesProfile.DL.value,
            cgmesProfile.EQ.value,
            cgmesProfile.SC.value,
            cgmesProfile.SV.value,
        ],
        "value": [
            cgmesProfile.DY.value,
            cgmesProfile.SSH.value,
            cgmesProfile.DL.value,
            cgmesProfile.EQ.value,
            cgmesProfile.SC.value,
            cgmesProfile.SV.value,
        ],
        "unit": [
            cgmesProfile.DY.value,
            cgmesProfile.SSH.value,
            cgmesProfile.DL.value,
            cgmesProfile.EQ.value,
            cgmesProfile.SC.value,
            cgmesProfile.SV.value,
        ],
        "multiplier": [
            cgmesProfile.DY.value,
            cgmesProfile.SSH.value,
            cgmesProfile.DL.value,
            cgmesProfile.EQ.value,
            cgmesProfile.SC.value,
            cgmesProfile.SV.value,
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
        str = "class=AngleDegrees\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
