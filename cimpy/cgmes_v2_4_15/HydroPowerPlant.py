from .PowerSystemResource import PowerSystemResource
from .CGMESProfile import Profile


class HydroPowerPlant(PowerSystemResource):
    """
    A hydro power station which can generate or pump. When generating, the generator turbines receive water from an upper reservoir. When pumping, the pumps receive their water from a lower reservoir.

    :HydroGeneratingUnits: The hydro generating unit belongs to a hydro power plant. Default: "list"
    :HydroPumps: The hydro pump may be a member of a pumped storage plant or a pump for distributing water. Default: "list"
    :hydroPlantStorageType: The type of hydro power plant water storage. Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "HydroGeneratingUnits": [Profile.EQ.value, ],
        "HydroPumps": [Profile.EQ.value, ],
        "hydroPlantStorageType": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class PowerSystemResource:\n" + PowerSystemResource.__doc__

    def __init__(self, HydroGeneratingUnits = "list", HydroPumps = "list", hydroPlantStorageType = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.HydroGeneratingUnits = HydroGeneratingUnits
        self.HydroPumps = HydroPumps
        self.hydroPlantStorageType = hydroPlantStorageType

    def __str__(self):
        str = "class=HydroPowerPlant\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
