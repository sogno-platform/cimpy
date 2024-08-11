from .TapChangerTablePoint import TapChangerTablePoint
from .CGMESProfile import Profile


class PhaseTapChangerTablePoint(TapChangerTablePoint):
    """
    Describes each tap step in the phase tap changer tabular curve.

    :PhaseTapChangerTable: The table of this point. Default: None
    :angle: The angle difference in degrees. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "PhaseTapChangerTable": [Profile.EQ.value, ],
        "angle": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class TapChangerTablePoint:\n" + TapChangerTablePoint.__doc__

    def __init__(self, PhaseTapChangerTable = None, angle = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.PhaseTapChangerTable = PhaseTapChangerTable
        self.angle = angle

    def __str__(self):
        str = "class=PhaseTapChangerTablePoint\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
