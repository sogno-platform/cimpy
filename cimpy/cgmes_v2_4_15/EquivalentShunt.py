from .EquivalentEquipment import EquivalentEquipment
from .CGMESProfile import Profile


class EquivalentShunt(EquivalentEquipment):
    """
    The class represents equivalent shunts.

    :b: Positive sequence shunt susceptance. Default: 0.0
    :g: Positive sequence shunt conductance. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "b": [Profile.EQ.value, ],
        "g": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class EquivalentEquipment:\n" + EquivalentEquipment.__doc__

    def __init__(self, b = 0.0, g = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.b = b
        self.g = g

    def __str__(self):
        str = "class=EquivalentShunt\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
