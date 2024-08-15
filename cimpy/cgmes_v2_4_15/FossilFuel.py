from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class FossilFuel(IdentifiedObject):
    """
    The fossil fuel consumed by the non-nuclear thermal generating unit.   For example, coal, oil, gas, etc.   This a the specific fuels that the generating unit can consume.

    :ThermalGeneratingUnit: A thermal generating unit may have one or more fossil fuels. Default: None
    :fossilFuelType: The type of fossil fuel, such as coal, oil, or gas. Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "ThermalGeneratingUnit": [Profile.EQ.value, ],
        "fossilFuelType": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, ThermalGeneratingUnit = None, fossilFuelType = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ThermalGeneratingUnit = ThermalGeneratingUnit
        self.fossilFuelType = fossilFuelType

    def __str__(self):
        str = "class=FossilFuel\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
