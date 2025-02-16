from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcIEEEDC1A(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type DC1A model. This model represents field-controlled dc commutator exciters with continuously acting voltage regulators (especially the direct-acting rheostatic, rotating amplifier, and magnetic amplifier types).  Because this model has been widely implemented by the industry, it is sometimes used to represent other types of systems when detailed data for them are not available or when a simplified model is required.   Reference: IEEE Standard 421.5-2005 Section 5.1.

    :efd1: Exciter voltage at which exciter saturation is defined (E).  Typical Value = 3.1. Default: 0.0
    :efd2: Exciter voltage at which exciter saturation is defined (E).  Typical Value = 2.3. Default: 0.0
    :exclim: (exclim).  IEEE standard is ambiguous about lower limit on exciter output. true = a lower limit of zero is applied to integrator output false = a lower limit of zero is not applied to integrator output. Typical Value = true. Default: False
    :ka: Voltage regulator gain (K).  Typical Value = 46. Default: 0.0
    :ke: Exciter constant related to self-excited field (K).  Typical Value = 0. Default: 0.0
    :kf: Excitation control system stabilizer gain (K).  Typical Value = 0.1. Default: 0.0
    :seefd1: Exciter saturation function value at the corresponding exciter voltage, E (S[E]).  Typical Value = 0.33. Default: 0.0
    :seefd2: Exciter saturation function value at the corresponding exciter voltage, E (S[E]).  Typical Value = 0.1. Default: 0.0
    :ta: Voltage regulator time constant (T).  Typical Value = 0.06. Default: 0.0
    :tb: Voltage regulator time constant (T).  Typical Value = 0. Default: 0.0
    :tc: Voltage regulator time constant (T).  Typical Value = 0. Default: 0.0
    :te: Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 0.46. Default: 0.0
    :tf: Excitation control system stabilizer time constant (T).  Typical Value = 1. Default: 0.0
    :uelin: UEL input (uelin). true = input is connected to the HV gate false = input connects to the error signal. Typical Value = true. Default: False
    :vrmax: Maximum voltage regulator output (V).  Typical Value = 1. Default: 0.0
    :vrmin: Minimum voltage regulator output (V).  Typical Value = -0.9. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "efd1": [Profile.DY.value, ],
        "efd2": [Profile.DY.value, ],
        "exclim": [Profile.DY.value, ],
        "ka": [Profile.DY.value, ],
        "ke": [Profile.DY.value, ],
        "kf": [Profile.DY.value, ],
        "seefd1": [Profile.DY.value, ],
        "seefd2": [Profile.DY.value, ],
        "ta": [Profile.DY.value, ],
        "tb": [Profile.DY.value, ],
        "tc": [Profile.DY.value, ],
        "te": [Profile.DY.value, ],
        "tf": [Profile.DY.value, ],
        "uelin": [Profile.DY.value, ],
        "vrmax": [Profile.DY.value, ],
        "vrmin": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, efd1 = 0.0, efd2 = 0.0, exclim = False, ka = 0.0, ke = 0.0, kf = 0.0, seefd1 = 0.0, seefd2 = 0.0, ta = 0.0, tb = 0.0, tc = 0.0, te = 0.0, tf = 0.0, uelin = False, vrmax = 0.0, vrmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.efd1 = efd1
        self.efd2 = efd2
        self.exclim = exclim
        self.ka = ka
        self.ke = ke
        self.kf = kf
        self.seefd1 = seefd1
        self.seefd2 = seefd2
        self.ta = ta
        self.tb = tb
        self.tc = tc
        self.te = te
        self.tf = tf
        self.uelin = uelin
        self.vrmax = vrmax
        self.vrmin = vrmin

    def __str__(self):
        str = "class=ExcIEEEDC1A\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
