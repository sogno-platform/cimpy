from .TapChangerTablePoint import TapChangerTablePoint
from .CGMESProfile import Profile


class RatioTapChangerTablePoint(TapChangerTablePoint):
    """
    Describes each tap step in the ratio tap changer tabular curve.

    :RatioTapChangerTable: Points of this table. Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "RatioTapChangerTable": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class TapChangerTablePoint:\n" + TapChangerTablePoint.__doc__

    def __init__(self, RatioTapChangerTable = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.RatioTapChangerTable = RatioTapChangerTable

    def __str__(self):
        str = "class=RatioTapChangerTablePoint\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
