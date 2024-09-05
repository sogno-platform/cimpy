from .Equipment import Equipment


class PowerElectronicsUnit(Equipment):
    """
    A generating unit or battery or aggregation that connects to the AC network using power electronics rather than rotating machines.

    :PowerElectronicsConnection: A power electronics unit has a connection to the AC network. Default: None
    :maxP: Maximum active power limit. This is the maximum (nameplate) limit for the unit. Default: 0.0
    :minP: Minimum active power limit. This is the minimum (nameplate) limit for the unit. Default: 0.0
    """

    cgmesProfile = Equipment.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
        ],
        "PowerElectronicsConnection": [
            cgmesProfile.EQ.value,
        ],
        "maxP": [
            cgmesProfile.EQ.value,
        ],
        "minP": [
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    __doc__ += "\n Documentation of parent class Equipment: \n" + Equipment.__doc__

    def __init__(
        self, PowerElectronicsConnection=None, maxP=0.0, minP=0.0, *args, **kw_args
    ):
        super().__init__(*args, **kw_args)

        self.PowerElectronicsConnection = PowerElectronicsConnection
        self.maxP = maxP
        self.minP = minP

    def __str__(self):
        str = "class=PowerElectronicsUnit\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
