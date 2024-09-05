from .Base import Base


class ActivePower(Base):
    """
    Product of RMS value of the voltage and the RMS value of the in-phase component of the current.

    :value:  Default: 0.0
    :multiplier:  Default: None
    :unit:  Default: None
    """

    cgmesProfile = Base.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
            cgmesProfile.SC.value,
            cgmesProfile.SV.value,
        ],
        "value": [
            cgmesProfile.DY.value,
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
            cgmesProfile.SC.value,
            cgmesProfile.SV.value,
        ],
        "multiplier": [
            cgmesProfile.DY.value,
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
            cgmesProfile.SC.value,
            cgmesProfile.SV.value,
        ],
        "unit": [
            cgmesProfile.DY.value,
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
            cgmesProfile.SC.value,
            cgmesProfile.SV.value,
        ],
    }

    serializationProfile = {}

    def __init__(
        self,
        value=0.0,
        multiplier=None,
        unit=None,
    ):

        self.value = value
        self.multiplier = multiplier
        self.unit = unit

    def __str__(self):
        str = "class=ActivePower\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
