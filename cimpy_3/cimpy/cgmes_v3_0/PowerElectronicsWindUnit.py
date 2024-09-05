from .PowerElectronicsUnit import PowerElectronicsUnit


class PowerElectronicsWindUnit(PowerElectronicsUnit):
    """
    A wind generating unit that connects to the AC network with power electronics rather than rotating machines or an aggregation of such units.

    """

    cgmesProfile = PowerElectronicsUnit.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class PowerElectronicsUnit: \n"
        + PowerElectronicsUnit.__doc__
    )

    def __init__(self, *args, **kw_args):
        super().__init__(*args, **kw_args)

        pass

    def __str__(self):
        str = "class=PowerElectronicsWindUnit\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
