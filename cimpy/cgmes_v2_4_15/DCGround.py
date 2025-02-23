from .DCConductingEquipment import DCConductingEquipment
from .CGMESProfile import Profile


class DCGround(DCConductingEquipment):
    """
    A ground within a DC system.

    :inductance: Inductance to ground. Default: 0.0
    :r: Resistance to ground. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "inductance": [Profile.EQ.value, ],
        "r": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class DCConductingEquipment:\n" + DCConductingEquipment.__doc__

    def __init__(self, inductance = 0.0, r = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.inductance = inductance
        self.r = r

    def __str__(self):
        str = "class=DCGround\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
