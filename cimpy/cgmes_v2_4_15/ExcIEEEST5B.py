from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcIEEEST5B(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type ST5B model. The Type ST5B excitation system is a variation of the Type ST1A model, with alternative overexcitation and underexcitation inputs and additional limits.  Reference: IEEE Standard 421.5-2005 Section 7.5.   Note: the block diagram in the IEEE 421.5 standard has input signal Vc and does not indicate the summation point with Vref. The implementation of the ExcIEEEST5B shall consider summation point with Vref.

    :kc: Rectifier regulation factor (K).  Typical Value = 0.004. Default: 0.0
    :kr: Regulator gain (K).  Typical Value = 200. Default: 0.0
    :t1: Firing circuit time constant (T1).  Typical Value = 0.004. Default: 0.0
    :tb1: Regulator lag time constant (T).  Typical Value = 6. Default: 0.0
    :tb2: Regulator lag time constant (T).  Typical Value = 0.01. Default: 0.0
    :tc1: Regulator lead time constant (T).  Typical Value = 0.8. Default: 0.0
    :tc2: Regulator lead time constant (T).  Typical Value = 0.08. Default: 0.0
    :tob1: OEL lag time constant (T).  Typical Value = 2. Default: 0.0
    :tob2: OEL lag time constant (T).  Typical Value = 0.08. Default: 0.0
    :toc1: OEL lead time constant (T).  Typical Value = 0.1. Default: 0.0
    :toc2: OEL lead time constant (T).  Typical Value = 0.08. Default: 0.0
    :tub1: UEL lag time constant (T).  Typical Value = 10. Default: 0.0
    :tub2: UEL lag time constant (T).  Typical Value = 0.05. Default: 0.0
    :tuc1: UEL lead time constant (T).  Typical Value = 2. Default: 0.0
    :tuc2: UEL lead time constant (T).  Typical Value = 0.1. Default: 0.0
    :vrmax: Maximum voltage regulator output (V).  Typical Value = 5. Default: 0.0
    :vrmin: Minimum voltage regulator output (V).  Typical Value = -4. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "kc": [Profile.DY.value, ],
        "kr": [Profile.DY.value, ],
        "t1": [Profile.DY.value, ],
        "tb1": [Profile.DY.value, ],
        "tb2": [Profile.DY.value, ],
        "tc1": [Profile.DY.value, ],
        "tc2": [Profile.DY.value, ],
        "tob1": [Profile.DY.value, ],
        "tob2": [Profile.DY.value, ],
        "toc1": [Profile.DY.value, ],
        "toc2": [Profile.DY.value, ],
        "tub1": [Profile.DY.value, ],
        "tub2": [Profile.DY.value, ],
        "tuc1": [Profile.DY.value, ],
        "tuc2": [Profile.DY.value, ],
        "vrmax": [Profile.DY.value, ],
        "vrmin": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, kc = 0.0, kr = 0.0, t1 = 0.0, tb1 = 0.0, tb2 = 0.0, tc1 = 0.0, tc2 = 0.0, tob1 = 0.0, tob2 = 0.0, toc1 = 0.0, toc2 = 0.0, tub1 = 0.0, tub2 = 0.0, tuc1 = 0.0, tuc2 = 0.0, vrmax = 0.0, vrmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.kc = kc
        self.kr = kr
        self.t1 = t1
        self.tb1 = tb1
        self.tb2 = tb2
        self.tc1 = tc1
        self.tc2 = tc2
        self.tob1 = tob1
        self.tob2 = tob2
        self.toc1 = toc1
        self.toc2 = toc2
        self.tub1 = tub1
        self.tub2 = tub2
        self.tuc1 = tuc1
        self.tuc2 = tuc2
        self.vrmax = vrmax
        self.vrmin = vrmin

    def __str__(self):
        str = "class=ExcIEEEST5B\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
