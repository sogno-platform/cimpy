from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class EnergyArea(IdentifiedObject):
    """
    Describes an area having energy production or consumption.  Specializations are intended to support the load allocation function as typically required in energy management systems or planning studies to allocate hypothesized load levels to individual load points for power flow analysis.  Often the energy area can be linked to both measured and forecast load levels.

    :ControlArea: The control area specification that is used for the load forecast. Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "ControlArea": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, ControlArea = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ControlArea = ControlArea

    def __str__(self):
        str = "class=EnergyArea\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
