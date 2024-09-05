from .PowerSystemResource import PowerSystemResource


class CAESPlant(PowerSystemResource):
    """
    Compressed air energy storage plant.

    :ThermalGeneratingUnit: A thermal generating unit may be a member of a compressed air energy storage plant. Default: None
    """

    cgmesProfile = PowerSystemResource.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.EQ.value,
        ],
        "ThermalGeneratingUnit": [
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class PowerSystemResource: \n"
        + PowerSystemResource.__doc__
    )

    def __init__(self, ThermalGeneratingUnit=None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ThermalGeneratingUnit = ThermalGeneratingUnit

    def __str__(self):
        str = "class=CAESPlant\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
