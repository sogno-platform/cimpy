from .VoltageAdjusterDynamics import VoltageAdjusterDynamics
from .CGMESProfile import Profile


class VAdjIEEE(VoltageAdjusterDynamics):
    """
    The class represents IEEE Voltage Adjuster which is used to represent the voltage adjuster in either a power factor or var control system.  Reference: IEEE Standard 421.5-2005 Section 11.1.

    :adjslew: Rate at which output of adjuster changes ().  Unit = sec./PU.  Typical Value = 300. Default: 0.0
    :taoff: Time that adjuster pulses are off ().  Typical Value = 0.5. Default: 0.0
    :taon: Time that adjuster pulses are on ().  Typical Value = 0.1. Default: 0.0
    :vadjf: Set high to provide a continuous raise or lower (). Default: 0.0
    :vadjmax: Maximum output of the adjuster ().  Typical Value = 1.1. Default: 0.0
    :vadjmin: Minimum output of the adjuster ().  Typical Value = 0.9. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "adjslew": [Profile.DY.value, ],
        "taoff": [Profile.DY.value, ],
        "taon": [Profile.DY.value, ],
        "vadjf": [Profile.DY.value, ],
        "vadjmax": [Profile.DY.value, ],
        "vadjmin": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class VoltageAdjusterDynamics:\n" + VoltageAdjusterDynamics.__doc__

    def __init__(self, adjslew = 0.0, taoff = 0.0, taon = 0.0, vadjf = 0.0, vadjmax = 0.0, vadjmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.adjslew = adjslew
        self.taoff = taoff
        self.taon = taon
        self.vadjf = vadjf
        self.vadjmax = vadjmax
        self.vadjmin = vadjmin

    def __str__(self):
        str = "class=VAdjIEEE\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
