from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcIEEEAC4A(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type AC4A model. The model represents type AC4A alternator-supplied controlled-rectifier excitation system which is quite different from the other type ac systems. This high initial response excitation system utilizes a full thyristor bridge in the exciter output circuit.  The voltage regulator controls the firing of the thyristor bridges. The exciter alternator uses an independent voltage regulator to control its output voltage to a constant value. These effects are not modeled; however, transient loading effects on the exciter alternator are included.   Reference: IEEE Standard 421.5-2005 Section 6.4.

    :ka: Voltage regulator gain (K).  Typical Value = 200. Default: 0.0
    :kc: Rectifier loading factor proportional to commutating reactance (K).  Typical Value = 0. Default: 0.0
    :ta: Voltage regulator time constant (T).  Typical Value = 0.015. Default: 0.0
    :tb: Voltage regulator time constant (T).  Typical Value = 10. Default: 0.0
    :tc: Voltage regulator time constant (T).  Typical Value = 1. Default: 0.0
    :vimax: Maximum voltage regulator input limit (V).  Typical Value = 10. Default: 0.0
    :vimin: Minimum voltage regulator input limit (V).  Typical Value = -10. Default: 0.0
    :vrmax: Maximum voltage regulator output (V).  Typical Value = 5.64. Default: 0.0
    :vrmin: Minimum voltage regulator output (V).  Typical Value = -4.53. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "ka": [Profile.DY.value, ],
        "kc": [Profile.DY.value, ],
        "ta": [Profile.DY.value, ],
        "tb": [Profile.DY.value, ],
        "tc": [Profile.DY.value, ],
        "vimax": [Profile.DY.value, ],
        "vimin": [Profile.DY.value, ],
        "vrmax": [Profile.DY.value, ],
        "vrmin": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, ka = 0.0, kc = 0.0, ta = 0.0, tb = 0.0, tc = 0.0, vimax = 0.0, vimin = 0.0, vrmax = 0.0, vrmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ka = ka
        self.kc = kc
        self.ta = ta
        self.tb = tb
        self.tc = tc
        self.vimax = vimax
        self.vimin = vimin
        self.vrmax = vrmax
        self.vrmin = vrmin

    def __str__(self):
        str = "class=ExcIEEEAC4A\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
