from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcST2A(ExcitationSystemDynamics):
    """
    Modified IEEE ST2A static excitation system - another lead-lag block added to match  the model defined by WECC.

    :efdmax: Maximum field voltage (Efdmax).  Typical Value = 99. Default: 0.0
    :ka: Voltage regulator gain (Ka).  Typical Value = 120. Default: 0.0
    :kc: Rectifier loading factor proportional to commutating reactance (Kc).  Typical Value = 1.82. Default: 0.0
    :ke: Exciter constant related to self-excited field (Ke).  Typical Value = 1. Default: 0.0
    :kf: Excitation control system stabilizer gains (Kf).  Typical Value = 0.05. Default: 0.0
    :ki: Potential circuit gain coefficient (Ki).  Typical Value = 8. Default: 0.0
    :kp: Potential circuit gain coefficient (Kp).  Typical Value = 4.88. Default: 0.0
    :ta: Voltage regulator time constant (Ta).  Typical Value = 0.15. Default: 0.0
    :tb: Voltage regulator time constant (Tb).  Typical Value = 0. Default: 0.0
    :tc: Voltage regulator time constant (Tc).  Typical Value = 0. Default: 0.0
    :te: Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 0.5. Default: 0.0
    :tf: Excitation control system stabilizer time constant (Tf).  Typical Value = 0.7. Default: 0.0
    :uelin: UEL input (UELin). true = HV gate false = add to error signal. Typical Value = false. Default: False
    :vrmax: Maximum voltage regulator outputs (Vrmax).  Typical Value = 1. Default: 0.0
    :vrmin: Minimum voltage regulator outputs (Vrmin).  Typical Value = -1. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "efdmax": [Profile.DY.value, ],
        "ka": [Profile.DY.value, ],
        "kc": [Profile.DY.value, ],
        "ke": [Profile.DY.value, ],
        "kf": [Profile.DY.value, ],
        "ki": [Profile.DY.value, ],
        "kp": [Profile.DY.value, ],
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

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, efdmax = 0.0, ka = 0.0, kc = 0.0, ke = 0.0, kf = 0.0, ki = 0.0, kp = 0.0, ta = 0.0, tb = 0.0, tc = 0.0, te = 0.0, tf = 0.0, uelin = False, vrmax = 0.0, vrmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.efdmax = efdmax
        self.ka = ka
        self.kc = kc
        self.ke = ke
        self.kf = kf
        self.ki = ki
        self.kp = kp
        self.ta = ta
        self.tb = tb
        self.tc = tc
        self.te = te
        self.tf = tf
        self.uelin = uelin
        self.vrmax = vrmax
        self.vrmin = vrmin

    def __str__(self):
        str = "class=ExcST2A\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
