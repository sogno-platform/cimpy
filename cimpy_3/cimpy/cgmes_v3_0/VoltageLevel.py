from .EquipmentContainer import EquipmentContainer


class VoltageLevel(EquipmentContainer):
    """
    A collection of equipment at one common system voltage forming a switchgear. The equipment typically consists of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.

    :BaseVoltage: The base voltage used for all equipment within the voltage level. Default: None
    :Bays: The bays within this voltage level. Default: "list"
    :Substation: The substation of the voltage level. Default: None
    :highVoltageLimit: The bus bar`s high voltage limit. The limit applies to all equipment and nodes contained in a given VoltageLevel. It is not required that it is exchanged in pair with lowVoltageLimit. It is preferable to use operational VoltageLimit, which prevails, if present. Default: 0.0
    :lowVoltageLimit: The bus bar`s low voltage limit. The limit applies to all equipment and nodes contained in a given VoltageLevel. It is not required that it is exchanged in pair with highVoltageLimit. It is preferable to use operational VoltageLimit, which prevails, if present. Default: 0.0
    """

    cgmesProfile = EquipmentContainer.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.EQ.value,
            cgmesProfile.EQBD.value,
        ],
        "BaseVoltage": [
            cgmesProfile.EQ.value,
            cgmesProfile.EQBD.value,
        ],
        "Bays": [
            cgmesProfile.EQ.value,
            cgmesProfile.EQBD.value,
        ],
        "Substation": [
            cgmesProfile.EQ.value,
            cgmesProfile.EQBD.value,
        ],
        "highVoltageLimit": [
            cgmesProfile.EQ.value,
            cgmesProfile.EQBD.value,
        ],
        "lowVoltageLimit": [
            cgmesProfile.EQ.value,
            cgmesProfile.EQBD.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class EquipmentContainer: \n"
        + EquipmentContainer.__doc__
    )

    def __init__(
        self,
        BaseVoltage=None,
        Bays="list",
        Substation=None,
        highVoltageLimit=0.0,
        lowVoltageLimit=0.0,
        *args,
        **kw_args,
    ):
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
