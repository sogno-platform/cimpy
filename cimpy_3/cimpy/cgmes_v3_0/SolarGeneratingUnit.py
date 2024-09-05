from .GeneratingUnit import GeneratingUnit


class SolarGeneratingUnit(GeneratingUnit):
    """
    A solar thermal generating unit, connected to the grid by means of a rotating machine.  This class does not represent photovoltaic (PV) generation.

    :SolarPowerPlant: A solar power plant may have solar generating units. Default: None
    """

    cgmesProfile = GeneratingUnit.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
        ],
        "SolarPowerPlant": [
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class GeneratingUnit: \n" + GeneratingUnit.__doc__
    )

    def __init__(self, SolarPowerPlant=None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.SolarPowerPlant = SolarPowerPlant

    def __str__(self):
        str = "class=SolarGeneratingUnit\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
