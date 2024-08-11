from .Equipment import Equipment
from .CGMESProfile import Profile


class ConductingEquipment(Equipment):
    """
    The parts of the AC power system that are designed to carry current or that are conductively connected through terminals.

    :BaseVoltage: All conducting equipment with this base voltage.  Use only when there is no voltage level container used and only one base voltage applies.  For example, not used for transformers. Default: None
    :SvStatus: The status state variable associated with this conducting equipment. Default: None
    :Terminals: Conducting equipment have terminals that may be connected to other conducting equipment terminals via connectivity nodes or topological nodes. Default: "list"
    """

    possibleProfileList = {
        "class": [Profile.DY.value, Profile.EQ_BD.value, Profile.EQ.value, Profile.SV.value, Profile.SSH.value, ],
        "BaseVoltage": [Profile.EQ.value, ],
        "SvStatus": [Profile.SV.value, ],
        "Terminals": [Profile.DY.value, Profile.EQ_BD.value, Profile.EQ.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class Equipment:\n" + Equipment.__doc__

    def __init__(self, BaseVoltage = None, SvStatus = None, Terminals = "list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.BaseVoltage = BaseVoltage
        self.SvStatus = SvStatus
        self.Terminals = Terminals

    def __str__(self):
        str = "class=ConductingEquipment\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
