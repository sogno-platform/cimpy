from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcIEEEDC4B(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type DC4B model. These excitation systems utilize a field-controlled dc commutator exciter with a continuously acting voltage regulator having supplies obtained from the generator or auxiliary bus.  Reference: IEEE Standard 421.5-2005 Section 5.4.

    :efd1: Exciter voltage at which exciter saturation is defined (E).  Typical Value = 1.75. Default: 0.0
    :efd2: Exciter voltage at which exciter saturation is defined (E).  Typical Value = 2.33. Default: 0.0
    :ka: Voltage regulator gain (K).  Typical Value = 1. Default: 0.0
    :kd: Regulator derivative gain (K).  Typical Value = 20. Default: 0.0
    :ke: Exciter constant related to self-excited field (K).  Typical Value = 1. Default: 0.0
    :kf: Excitation control system stabilizer gain (K).  Typical Value = 0. Default: 0.0
    :ki: Regulator integral gain (K).  Typical Value = 20. Default: 0.0
    :kp: Regulator proportional gain (K).  Typical Value = 20. Default: 0.0
    :oelin: OEL input (OELin). true = LV gate false = subtract from error signal. Typical Value = true. Default: False
    :seefd1: Exciter saturation function value at the corresponding exciter voltage, E (S[E]).  Typical Value = 0.08. Default: 0.0
    :seefd2: Exciter saturation function value at the corresponding exciter voltage, E (S[E]).  Typical Value = 0.27. Default: 0.0
    :ta: Voltage regulator time constant (T).  Typical Value = 0.2. Default: 0.0
    :td: Regulator derivative filter time constant(T).  Typical Value = 0.01. Default: 0.0
    :te: Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 0.8. Default: 0.0
    :tf: Excitation control system stabilizer time constant (T).  Typical Value = 1. Default: 0.0
    :uelin: UEL input (UELin). true = HV gate false = add to error signal. Typical Value = true. Default: False
    :vemin: Minimum exciter voltage output(V).  Typical Value = 0. Default: 0.0
    :vrmax: Maximum voltage regulator output (V).  Typical Value = 2.7. Default: 0.0
    :vrmin: Minimum voltage regulator output (V).  Typical Value = -0.9. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "efd1": [Profile.DY.value, ],
        "efd2": [Profile.DY.value, ],
        "ka": [Profile.DY.value, ],
        "kd": [Profile.DY.value, ],
        "ke": [Profile.DY.value, ],
        "kf": [Profile.DY.value, ],
        "ki": [Profile.DY.value, ],
        "kp": [Profile.DY.value, ],
        "oelin": [Profile.DY.value, ],
        "seefd1": [Profile.DY.value, ],
        "seefd2": [Profile.DY.value, ],
        "ta": [Profile.DY.value, ],
        "td": [Profile.DY.value, ],
        "te": [Profile.DY.value, ],
        "tf": [Profile.DY.value, ],
        "uelin": [Profile.DY.value, ],
        "vemin": [Profile.DY.value, ],
        "vrmax": [Profile.DY.value, ],
        "vrmin": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, efd1 = 0.0, efd2 = 0.0, ka = 0.0, kd = 0.0, ke = 0.0, kf = 0.0, ki = 0.0, kp = 0.0, oelin = False, seefd1 = 0.0, seefd2 = 0.0, ta = 0.0, td = 0.0, te = 0.0, tf = 0.0, uelin = False, vemin = 0.0, vrmax = 0.0, vrmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.efd1 = efd1
        self.efd2 = efd2
        self.ka = ka
        self.kd = kd
        self.ke = ke
        self.kf = kf
        self.ki = ki
        self.kp = kp
        self.oelin = oelin
        self.seefd1 = seefd1
        self.seefd2 = seefd2
        self.ta = ta
        self.td = td
        self.te = te
        self.tf = tf
        self.uelin = uelin
        self.vemin = vemin
        self.vrmax = vrmax
        self.vrmin = vrmin

    def __str__(self):
        str = "class=ExcIEEEDC4B\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
