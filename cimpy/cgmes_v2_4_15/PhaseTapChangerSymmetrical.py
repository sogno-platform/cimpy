from .PhaseTapChangerNonLinear import PhaseTapChangerNonLinear
from .CGMESProfile import Profile


class PhaseTapChangerSymmetrical(PhaseTapChangerNonLinear):
    """
    Describes a symmetrical phase shifting transformer tap model in which the secondary side voltage magnitude is the same as at the primary side. The difference voltage magnitude is the base in an equal-sided triangle where the sides corresponds to the primary and secondary voltages. The phase angle difference corresponds to the top angle and can be expressed as twice the arctangent of half the total difference voltage.

    """

    possibleProfileList = {
        "class": [Profile.EQ.value, Profile.SSH.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class PhaseTapChangerNonLinear:\n" + PhaseTapChangerNonLinear.__doc__

    def __init__(self, *args, **kw_args):
        super().__init__(*args, **kw_args)

        pass

    def __str__(self):
        str = "class=PhaseTapChangerSymmetrical\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
