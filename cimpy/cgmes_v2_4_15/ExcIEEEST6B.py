from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcIEEEST6B(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type ST6B model. This model consists of a PI voltage regulator with an inner loop field voltage regulator and pre-control. The field voltage regulator implements a proportional control. The pre-control and the delay in the feedback circuit increase the dynamic response.  Reference: IEEE Standard 421.5-2005 Section 7.6.

    :ilr: Exciter output current limit reference (I).  Typical Value = 4.164. Default: 0.0
    :kci: Exciter output current limit adjustment (K).  Typical Value = 1.0577. Default: 0.0
    :kff: Pre-control gain constant of the inner loop field regulator (K). Typical Value = 1. Default: 0.0
    :kg: Feedback gain constant of the inner loop field regulator (K).  Typical Value = 1. Default: 0.0
    :kia: Voltage regulator integral gain (K).  Typical Value = 45.094. Default: 0.0
    :klr: Exciter output current limiter gain (K).  Typical Value = 17.33. Default: 0.0
    :km: Forward gain constant of the inner loop field regulator (K).  Typical Value = 1. Default: 0.0
    :kpa: Voltage regulator proportional gain (K).  Typical Value = 18.038. Default: 0.0
    :oelin: OEL input selector (OELin). Typical Value = noOELinput. Default: None
    :tg: Feedback time constant of inner loop field voltage regulator (T). Typical Value = 0.02. Default: 0.0
    :vamax: Maximum voltage regulator output (V).  Typical Value = 4.81. Default: 0.0
    :vamin: Minimum voltage regulator output (V).  Typical Value = -3.85. Default: 0.0
    :vrmax: Maximum voltage regulator output (V).  Typical Value = 4.81. Default: 0.0
    :vrmin: Minimum voltage regulator output (V).  Typical Value = -3.85. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "ilr": [Profile.DY.value, ],
        "kci": [Profile.DY.value, ],
        "kff": [Profile.DY.value, ],
        "kg": [Profile.DY.value, ],
        "kia": [Profile.DY.value, ],
        "klr": [Profile.DY.value, ],
        "km": [Profile.DY.value, ],
        "kpa": [Profile.DY.value, ],
        "oelin": [Profile.DY.value, ],
        "tg": [Profile.DY.value, ],
        "vamax": [Profile.DY.value, ],
        "vamin": [Profile.DY.value, ],
        "vrmax": [Profile.DY.value, ],
        "vrmin": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, ilr = 0.0, kci = 0.0, kff = 0.0, kg = 0.0, kia = 0.0, klr = 0.0, km = 0.0, kpa = 0.0, oelin = None, tg = 0.0, vamax = 0.0, vamin = 0.0, vrmax = 0.0, vrmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ilr = ilr
        self.kci = kci
        self.kff = kff
        self.kg = kg
        self.kia = kia
        self.klr = klr
        self.km = km
        self.kpa = kpa
        self.oelin = oelin
        self.tg = tg
        self.vamax = vamax
        self.vamin = vamin
        self.vrmax = vrmax
        self.vrmin = vrmin

    def __str__(self):
        str = "class=ExcIEEEST6B\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
