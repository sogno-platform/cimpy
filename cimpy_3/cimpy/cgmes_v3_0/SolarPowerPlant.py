from .PowerSystemResource import PowerSystemResource


class SolarPowerPlant(PowerSystemResource):
    """
    Solar power plant.

    :SolarGeneratingUnits: A solar generating unit or units may be a member of a solar power plant. Default: "list"
    """

    cgmesProfile = PowerSystemResource.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.EQ.value,
        ],
        "SolarGeneratingUnits": [
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class PowerSystemResource: \n"
        + PowerSystemResource.__doc__
    )

    def __init__(self, SolarGeneratingUnits="list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.SolarGeneratingUnits = SolarGeneratingUnits

    def __str__(self):
        str = "class=SolarPowerPlant\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
