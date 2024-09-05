from .GeneratingUnit import GeneratingUnit


class HydroGeneratingUnit(GeneratingUnit):
    """
    A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan).

    :energyConversionCapability: Energy conversion capability for generating. Default: None
    :dropHeight: The height water drops from the reservoir mid-point to the turbine. Default: 0.0
    :turbineType: Type of turbine. Default: None
    :HydroPowerPlant: The hydro generating unit belongs to a hydro power plant. Default: None
    """

    cgmesProfile = GeneratingUnit.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
        ],
        "energyConversionCapability": [
            cgmesProfile.EQ.value,
        ],
        "dropHeight": [
            cgmesProfile.EQ.value,
        ],
        "turbineType": [
            cgmesProfile.EQ.value,
        ],
        "HydroPowerPlant": [
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class GeneratingUnit: \n" + GeneratingUnit.__doc__
    )

    def __init__(
        self,
        energyConversionCapability=None,
        dropHeight=0.0,
        turbineType=None,
        HydroPowerPlant=None,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.energyConversionCapability = energyConversionCapability
        self.dropHeight = dropHeight
        self.turbineType = turbineType
        self.HydroPowerPlant = HydroPowerPlant

    def __str__(self):
        str = "class=HydroGeneratingUnit\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
