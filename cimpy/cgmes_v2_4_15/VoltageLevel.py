from .EquipmentContainer import EquipmentContainer
from .CGMESProfile import Profile


class VoltageLevel(EquipmentContainer):
    """
    A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.

    :BaseVoltage: The base voltage used for all equipment within the voltage level. Default: None
    :Bays: The bays within this voltage level. Default: "list"
    :Substation: The substation of the voltage level. Default: None
    :highVoltageLimit: The bus bar`s high voltage limit Default: 0.0
    :lowVoltageLimit: The bus bar`s low voltage limit Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "BaseVoltage": [Profile.EQ.value, ],
        "Bays": [Profile.EQ.value, ],
        "Substation": [Profile.EQ.value, ],
        "highVoltageLimit": [Profile.EQ.value, ],
        "lowVoltageLimit": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class EquipmentContainer:\n" + EquipmentContainer.__doc__

    def __init__(self, BaseVoltage = None, Bays = "list", Substation = None, highVoltageLimit = 0.0, lowVoltageLimit = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.BaseVoltage = BaseVoltage
        self.Bays = Bays
        self.Substation = Substation
        self.highVoltageLimit = highVoltageLimit
        self.lowVoltageLimit = lowVoltageLimit

    def __str__(self):
        str = "class=VoltageLevel\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
