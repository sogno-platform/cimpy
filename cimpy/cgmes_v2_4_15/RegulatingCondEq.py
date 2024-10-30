from .ConductingEquipment import ConductingEquipment
from .CGMESProfile import Profile


class RegulatingCondEq(ConductingEquipment):
    """
    A type of conducting equipment that can regulate a quantity (i.e. voltage or flow) at a specific point in the network.

    :RegulatingControl: The regulating control scheme in which this equipment participates. Default: None
    :controlEnabled: Specifies the regulation status of the equipment.  True is regulating, false is not regulating. Default: False
    """

    possibleProfileList = {
        "class": [Profile.DY.value, Profile.EQ.value, Profile.SSH.value, ],
        "RegulatingControl": [Profile.EQ.value, ],
        "controlEnabled": [Profile.SSH.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class ConductingEquipment:\n" + ConductingEquipment.__doc__

    def __init__(self, RegulatingControl = None, controlEnabled = False, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.RegulatingControl = RegulatingControl
        self.controlEnabled = controlEnabled

    def __str__(self):
        str = "class=RegulatingCondEq\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
