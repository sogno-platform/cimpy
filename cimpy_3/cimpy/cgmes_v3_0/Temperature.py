from .Base import Base


class Temperature(Base):
    """
    Value of temperature in degrees Celsius.

    :multiplier:  Default: None
    :unit:  Default: None
    :value:  Default: 0.0
    """

    cgmesProfile = Base.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
            cgmesProfile.SC.value,
        ],
        "multiplier": [
            cgmesProfile.DY.value,
            cgmesProfile.SC.value,
        ],
        "unit": [
            cgmesProfile.DY.value,
            cgmesProfile.SC.value,
        ],
        "value": [
            cgmesProfile.DY.value,
            cgmesProfile.SC.value,
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
        str = "class=Temperature\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
