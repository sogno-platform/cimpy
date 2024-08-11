from .GeneratingUnit import GeneratingUnit
from .CGMESProfile import Profile


class HydroGeneratingUnit(GeneratingUnit):
    """
    A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan).

    :HydroPowerPlant: The hydro generating unit belongs to a hydro power plant. Default: None
    :energyConversionCapability: Energy conversion capability for generating. Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, Profile.SSH.value, ],
        "HydroPowerPlant": [Profile.EQ.value, ],
        "energyConversionCapability": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class GeneratingUnit:\n" + GeneratingUnit.__doc__

    def __init__(self, HydroPowerPlant = None, energyConversionCapability = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.HydroPowerPlant = HydroPowerPlant
        self.energyConversionCapability = energyConversionCapability

    def __str__(self):
        str = "class=HydroGeneratingUnit\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
