from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcDC3A1(ExcitationSystemDynamics):
    """
    This is modified old IEEE type 3 excitation system.

    :exclim: (exclim). true = lower limit of zero is applied to integrator output false = lower limit of zero not applied to integrator output. Typical Value = true. Default: False
    :ka: Voltage regulator gain (Ka).  Typical Value = 300. Default: 0.0
    :ke: Exciter constant related to self-excited field (Ke).  Typical Value = 1. Default: 0.0
    :kf: Excitation control system stabilizer gain (Kf).  Typical Value = 0.1. Default: 0.0
    :ki: Potential circuit gain coefficient (Ki).  Typical Value = 4.83. Default: 0.0
    :kp: Potential circuit gain coefficient (Kp).  Typical Value = 4.37. Default: 0.0
    :ta: Voltage regulator time constant (Ta).  Typical Value = 0.01. Default: 0.0
    :te: Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 1.83. Default: 0.0
    :tf: Excitation control system stabilizer time constant (Tf).  Typical Value = 0.675. Default: 0.0
    :vb1max: Available exciter voltage limiter (Vb1max).  Typical Value = 11.63. Default: 0.0
    :vblim: Vb limiter indicator. true = exciter Vbmax limiter is active false = Vb1max is active.  Typical Value = true. Default: False
    :vbmax: Available exciter voltage limiter (Vbmax).  Typical Value = 11.63. Default: 0.0
    :vrmax: Maximum voltage regulator output (Vrmax).  Typical Value = 5. Default: 0.0
    :vrmin: Minimum voltage regulator output (Vrmin).  Typical Value = 0. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "exclim": [Profile.DY.value, ],
        "ka": [Profile.DY.value, ],
        "ke": [Profile.DY.value, ],
        "kf": [Profile.DY.value, ],
        "ki": [Profile.DY.value, ],
        "kp": [Profile.DY.value, ],
        "ta": [Profile.DY.value, ],
        "te": [Profile.DY.value, ],
        "tf": [Profile.DY.value, ],
        "vb1max": [Profile.DY.value, ],
        "vblim": [Profile.DY.value, ],
        "vbmax": [Profile.DY.value, ],
        "vrmax": [Profile.DY.value, ],
        "vrmin": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, exclim = False, ka = 0.0, ke = 0.0, kf = 0.0, ki = 0.0, kp = 0.0, ta = 0.0, te = 0.0, tf = 0.0, vb1max = 0.0, vblim = False, vbmax = 0.0, vrmax = 0.0, vrmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.exclim = exclim
        self.ka = ka
        self.ke = ke
        self.kf = kf
        self.ki = ki
        self.kp = kp
        self.ta = ta
        self.te = te
        self.tf = tf
        self.vb1max = vb1max
        self.vblim = vblim
        self.vbmax = vbmax
        self.vrmax = vrmax
        self.vrmin = vrmin

    def __str__(self):
        str = "class=ExcDC3A1\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
