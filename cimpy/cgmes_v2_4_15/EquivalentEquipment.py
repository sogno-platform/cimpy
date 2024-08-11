from .ConductingEquipment import ConductingEquipment
from .CGMESProfile import Profile


class EquivalentEquipment(ConductingEquipment):
    """
    The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of different types.

    :EquivalentNetwork: The associated reduced equivalents. Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, Profile.SSH.value, ],
        "EquivalentNetwork": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class ConductingEquipment:\n" + ConductingEquipment.__doc__

    def __init__(self, EquivalentNetwork = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.EquivalentNetwork = EquivalentNetwork

    def __str__(self):
        str = "class=EquivalentEquipment\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
