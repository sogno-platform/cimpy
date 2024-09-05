from .EnergyConnection import EnergyConnection


class RegulatingCondEq(EnergyConnection):
    """
    A type of conducting equipment that can regulate a quantity (i.e. voltage or flow) at a specific point in the network.

    :controlEnabled: Specifies the regulation status of the equipment.  True is regulating, false is not regulating. Default: False
    :RegulatingControl: The regulating control scheme in which this equipment participates. Default: None
    """

    cgmesProfile = EnergyConnection.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
            cgmesProfile.SC.value,
        ],
        "controlEnabled": [
            cgmesProfile.SSH.value,
        ],
        "RegulatingControl": [
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class EnergyConnection: \n"
        + EnergyConnection.__doc__
    )

    def __init__(self, controlEnabled=False, RegulatingControl=None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.controlEnabled = controlEnabled
        self.RegulatingControl = RegulatingControl

    def __str__(self):
        str = "class=RegulatingCondEq\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
