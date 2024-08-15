from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class PhaseTapChangerTable(IdentifiedObject):
    """
    Describes a tabular curve for how the phase angle difference and impedance varies with the tap step.

    :PhaseTapChangerTablePoint: The points of this table. Default: "list"
    :PhaseTapChangerTabular: The phase tap changers to which this phase tap table applies. Default: "list"
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "PhaseTapChangerTablePoint": [Profile.EQ.value, ],
        "PhaseTapChangerTabular": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, PhaseTapChangerTablePoint = "list", PhaseTapChangerTabular = "list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.PhaseTapChangerTablePoint = PhaseTapChangerTablePoint
        self.PhaseTapChangerTabular = PhaseTapChangerTabular

    def __str__(self):
        str = "class=PhaseTapChangerTable\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
