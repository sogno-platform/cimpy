from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class RatioTapChangerTable(IdentifiedObject):
    """
    Describes a curve for how the voltage magnitude and impedance varies with the tap step.

    :RatioTapChanger: The tap ratio table for this ratio  tap changer. Default: "list"
    :RatioTapChangerTablePoint: Table of this point. Default: "list"
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "RatioTapChanger": [Profile.EQ.value, ],
        "RatioTapChangerTablePoint": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, RatioTapChanger = "list", RatioTapChangerTablePoint = "list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.RatioTapChanger = RatioTapChanger
        self.RatioTapChangerTablePoint = RatioTapChangerTablePoint

    def __str__(self):
        str = "class=RatioTapChangerTable\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
