from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcSEXS(ExcitationSystemDynamics):
    """
    Simplified Excitation System Model.

    :efdmax: Field voltage clipping maximum limit (Efdmax).  Typical Value = 5. Default: 0.0
    :efdmin: Field voltage clipping minimum limit (Efdmin).  Typical Value = -5. Default: 0.0
    :emax: Maximum field voltage output (Emax).  Typical Value = 5. Default: 0.0
    :emin: Minimum field voltage output (Emin).  Typical Value = -5. Default: 0.0
    :k: Gain (K) (>0).  Typical Value = 100. Default: 0.0
    :kc: PI controller gain (Kc).  Typical Value = 0.08. Default: 0.0
    :tatb: Ta/Tb - gain reduction ratio of lag-lead element (TaTb).  Typical Value = 0.1. Default: 0.0
    :tb: Denominator time constant of lag-lead block (Tb).  Typical Value = 10. Default: 0.0
    :tc: PI controller phase lead time constant (Tc).  Typical Value = 0. Default: 0.0
    :te: Time constant of gain block (Te).  Typical Value = 0.05. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "efdmax": [Profile.DY.value, ],
        "efdmin": [Profile.DY.value, ],
        "emax": [Profile.DY.value, ],
        "emin": [Profile.DY.value, ],
        "k": [Profile.DY.value, ],
        "kc": [Profile.DY.value, ],
        "tatb": [Profile.DY.value, ],
        "tb": [Profile.DY.value, ],
        "tc": [Profile.DY.value, ],
        "te": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, efdmax = 0.0, efdmin = 0.0, emax = 0.0, emin = 0.0, k = 0.0, kc = 0.0, tatb = 0.0, tb = 0.0, tc = 0.0, te = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.efdmax = efdmax
        self.efdmin = efdmin
        self.emax = emax
        self.emin = emin
        self.k = k
        self.kc = kc
        self.tatb = tatb
        self.tb = tb
        self.tc = tc
        self.te = te

    def __str__(self):
        str = "class=ExcSEXS\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
