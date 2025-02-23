from .VoltageCompensatorDynamics import VoltageCompensatorDynamics
from .CGMESProfile import Profile


class VCompIEEEType2(VoltageCompensatorDynamics):
    """
    

    :GenICompensationForGenJ: Compensation of this voltage compensator`s generator for current flow out of another generator. Default: "list"
    :tr:  Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "GenICompensationForGenJ": [Profile.DY.value, ],
        "tr": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class VoltageCompensatorDynamics:\n" + VoltageCompensatorDynamics.__doc__

    def __init__(self, GenICompensationForGenJ = "list", tr = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.GenICompensationForGenJ = GenICompensationForGenJ
        self.tr = tr

    def __str__(self):
        str = "class=VCompIEEEType2\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
