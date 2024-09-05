from .GeneratingUnit import GeneratingUnit


class WindGeneratingUnit(GeneratingUnit):
    """
    A wind driven generating unit, connected to the grid by means of a rotating machine.  May be used to represent a single turbine or an aggregation.

    :windGenUnitType: The kind of wind generating unit. Default: None
    :WindPowerPlant: A wind power plant may have wind generating units. Default: None
    """

    cgmesProfile = GeneratingUnit.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
        ],
        "windGenUnitType": [
            cgmesProfile.EQ.value,
        ],
        "WindPowerPlant": [
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class GeneratingUnit: \n" + GeneratingUnit.__doc__
    )

    def __init__(self, windGenUnitType=None, WindPowerPlant=None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.windGenUnitType = windGenUnitType
        self.WindPowerPlant = WindPowerPlant

    def __str__(self):
        str = "class=WindGeneratingUnit\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
