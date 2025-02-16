from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcIEEEDC3A(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type DC3A model. This model represents represent older systems, in particular those dc commutator exciters with non-continuously acting regulators that were commonly used before the development of the continuously acting varieties.  These systems respond at basically two different rates, depending upon the magnitude of voltage error. For small errors, adjustment is made periodically with a signal to a motor-operated rheostat. Larger errors cause resistors to be quickly shorted or inserted and a strong forcing signal applied to the exciter. Continuous motion of the motor-operated rheostat occurs for these larger error signals, even though it is bypassed by contactor action.   Reference: IEEE Standard 421.5-2005 Section 5.3.

    :efd1: Exciter voltage at which exciter saturation is defined (E).  Typical Value = 3.375. Default: 0.0
    :efd2: Exciter voltage at which exciter saturation is defined (E).  Typical Value = 3.15. Default: 0.0
    :exclim: (exclim).  IEEE standard is ambiguous about lower limit on exciter output. true = a lower limit of zero is applied to integrator output false = a lower limit of zero is not applied to integrator output. Typical Value = true. Default: False
    :ke: Exciter constant related to self-excited field (K).  Typical Value = 0.05. Default: 0.0
    :kv: Fast raise/lower contact setting (K).  Typical Value = 0.05. Default: 0.0
    :seefd1: Exciter saturation function value at the corresponding exciter voltage, E (S[E]).  Typical Value = 0.267. Default: 0.0
    :seefd2: Exciter saturation function value at the corresponding exciter voltage, E (S[E]).  Typical Value = 0.068. Default: 0.0
    :te: Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 0.5. Default: 0.0
    :trh: Rheostat travel time (T).  Typical Value = 20. Default: 0.0
    :vrmax: Maximum voltage regulator output (V).  Typical Value = 1. Default: 0.0
    :vrmin: Minimum voltage regulator output (V).  Typical Value = 0. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "efd1": [Profile.DY.value, ],
        "efd2": [Profile.DY.value, ],
        "exclim": [Profile.DY.value, ],
        "ke": [Profile.DY.value, ],
        "kv": [Profile.DY.value, ],
        "seefd1": [Profile.DY.value, ],
        "seefd2": [Profile.DY.value, ],
        "te": [Profile.DY.value, ],
        "trh": [Profile.DY.value, ],
        "vrmax": [Profile.DY.value, ],
        "vrmin": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, efd1 = 0.0, efd2 = 0.0, exclim = False, ke = 0.0, kv = 0.0, seefd1 = 0.0, seefd2 = 0.0, te = 0.0, trh = 0.0, vrmax = 0.0, vrmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.efd1 = efd1
        self.efd2 = efd2
        self.exclim = exclim
        self.ke = ke
        self.kv = kv
        self.seefd1 = seefd1
        self.seefd2 = seefd2
        self.te = te
        self.trh = trh
        self.vrmax = vrmax
        self.vrmin = vrmin

    def __str__(self):
        str = "class=ExcIEEEDC3A\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
