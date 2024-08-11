from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcAC3A(ExcitationSystemDynamics):
    """
    Modified IEEE AC3A alternator-supplied rectifier excitation system with different field current limit.

    :efdn: Value of at which feedback gain changes (Efdn).  Typical Value = 2.36. Default: 0.0
    :ka: Voltage regulator gain (Ka).  Typical Value = 45.62. Default: 0.0
    :kc: Rectifier loading factor proportional to commutating reactance (Kc).  Typical Value = 0.104. Default: 0.0
    :kd: Demagnetizing factor, a function of exciter alternator reactances (Kd).  Typical Value = 0.499. Default: 0.0
    :ke: Exciter constant related to self-excited field (Ke).  Typical Value = 1. Default: 0.0
    :kf: Excitation control system stabilizer gains (Kf).  Typical Value = 0.143. Default: 0.0
    :kf1: Coefficient to allow different usage of the model (Kf1).  Typical Value = 1. Default: 0.0
    :kf2: Coefficient to allow different usage of the model (Kf2).  Typical Value = 0. Default: 0.0
    :klv: Gain used in the minimum field voltage limiter loop (Klv).  Typical Value = 0.194. Default: 0.0
    :kn: Excitation control system stabilizer gain (Kn).  Typical Value =0.05. Default: 0.0
    :kr: Constant associated with regulator and alternator field power supply (Kr).  Typical Value =3.77. Default: 0.0
    :ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0. Default: 0.0
    :seve1: Exciter saturation function value at the corresponding exciter voltage, Ve, back of commutating reactance (Se[Ve]).  Typical Value = 1.143. Default: 0.0
    :seve2: Exciter saturation function value at the corresponding exciter voltage, Ve, back of commutating reactance (Se[Ve]).  Typical Value = 0.1. Default: 0.0
    :ta: Voltage regulator time constant (Ta).  Typical Value = 0.013. Default: 0.0
    :tb: Voltage regulator time constant (Tb).  Typical Value = 0. Default: 0.0
    :tc: Voltage regulator time constant (T).  Typical Value = 0. Default: 0.0
    :te: Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 1.17. Default: 0.0
    :tf: Excitation control system stabilizer time constant (Tf).  Typical Value = 1. Default: 0.0
    :vamax: Maximum voltage regulator output (V).  Typical Value = 1. Default: 0.0
    :vamin: Minimum voltage regulator output (V).  Typical Value = -0.95. Default: 0.0
    :ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1) equals Vemax (Ve1).  Typical Value = 6.24. Default: 0.0
    :ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve).  Typical Value = 4.68. Default: 0.0
    :vemin: Minimum exciter voltage output (Vemin).  Typical Value = 0.1. Default: 0.0
    :vfemax: Exciter field current limit reference (Vfemax).  Typical Value = 16. Default: 0.0
    :vlv: Field voltage used in the minimum field voltage limiter loop (Vlv).  Typical Value = 0.79. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "efdn": [Profile.DY.value, ],
        "ka": [Profile.DY.value, ],
        "kc": [Profile.DY.value, ],
        "kd": [Profile.DY.value, ],
        "ke": [Profile.DY.value, ],
        "kf": [Profile.DY.value, ],
        "kf1": [Profile.DY.value, ],
        "kf2": [Profile.DY.value, ],
        "klv": [Profile.DY.value, ],
        "kn": [Profile.DY.value, ],
        "kr": [Profile.DY.value, ],
        "ks": [Profile.DY.value, ],
        "seve1": [Profile.DY.value, ],
        "seve2": [Profile.DY.value, ],
        "ta": [Profile.DY.value, ],
        "tb": [Profile.DY.value, ],
        "tc": [Profile.DY.value, ],
        "te": [Profile.DY.value, ],
        "tf": [Profile.DY.value, ],
        "vamax": [Profile.DY.value, ],
        "vamin": [Profile.DY.value, ],
        "ve1": [Profile.DY.value, ],
        "ve2": [Profile.DY.value, ],
        "vemin": [Profile.DY.value, ],
        "vfemax": [Profile.DY.value, ],
        "vlv": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, efdn = 0.0, ka = 0.0, kc = 0.0, kd = 0.0, ke = 0.0, kf = 0.0, kf1 = 0.0, kf2 = 0.0, klv = 0.0, kn = 0.0, kr = 0.0, ks = 0.0, seve1 = 0.0, seve2 = 0.0, ta = 0.0, tb = 0.0, tc = 0.0, te = 0.0, tf = 0.0, vamax = 0.0, vamin = 0.0, ve1 = 0.0, ve2 = 0.0, vemin = 0.0, vfemax = 0.0, vlv = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.efdn = efdn
        self.ka = ka
        self.kc = kc
        self.kd = kd
        self.ke = ke
        self.kf = kf
        self.kf1 = kf1
        self.kf2 = kf2
        self.klv = klv
        self.kn = kn
        self.kr = kr
        self.ks = ks
        self.seve1 = seve1
        self.seve2 = seve2
        self.ta = ta
        self.tb = tb
        self.tc = tc
        self.te = te
        self.tf = tf
        self.vamax = vamax
        self.vamin = vamin
        self.ve1 = ve1
        self.ve2 = ve2
        self.vemin = vemin
        self.vfemax = vfemax
        self.vlv = vlv

    def __str__(self):
        str = "class=ExcAC3A\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
