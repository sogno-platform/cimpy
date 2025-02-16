from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcAC4A(ExcitationSystemDynamics):
    """
    Modified IEEE AC4A alternator-supplied rectifier excitation system with different minimum controller output.

    :ka: Voltage regulator gain (Ka).  Typical Value = 200. Default: 0.0
    :kc: Rectifier loading factor proportional to commutating reactance (Kc).  Typical Value = 0. Default: 0.0
    :ta: Voltage regulator time constant (Ta).  Typical Value = 0.015. Default: 0.0
    :tb: Voltage regulator time constant (Tb).  Typical Value = 10. Default: 0.0
    :tc: Voltage regulator time constant (Tc).  Typical Value = 1. Default: 0.0
    :vimax: Maximum voltage regulator input limit (Vimax).  Typical Value = 10. Default: 0.0
    :vimin: Minimum voltage regulator input limit (Vimin).  Typical Value = -10. Default: 0.0
    :vrmax: Maximum voltage regulator output (Vrmax).  Typical Value = 5.64. Default: 0.0
    :vrmin: Minimum voltage regulator output (Vrmin).  Typical Value = -4.53. Default: 0.0
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
        str = "class=ExcAC4A\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
