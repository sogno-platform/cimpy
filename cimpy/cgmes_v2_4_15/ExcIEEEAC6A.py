from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcIEEEAC6A(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type AC6A model. The model represents field-controlled alternator-rectifier excitation systems with system-supplied electronic voltage regulators.  The maximum output of the regulator, , is a function of terminal voltage, . The field current limiter included in the original model AC6A remains in the 2005 update.  Reference: IEEE Standard 421.5-2005 Section 6.6.

    :ka: Voltage regulator gain (K).  Typical Value = 536. Default: 0.0
    :kc: Rectifier loading factor proportional to commutating reactance (K). Typical Value = 0.173. Default: 0.0
    :kd: Demagnetizing factor, a function of exciter alternator reactances (K).  Typical Value = 1.91. Default: 0.0
    :ke: Exciter constant related to self-excited field (K).  Typical Value = 1.6. Default: 0.0
    :kh: Exciter field current limiter gain (K).  Typical Value = 92. Default: 0.0
    :seve1: Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 0.214. Default: 0.0
    :seve2: Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 0.044. Default: 0.0
    :ta: Voltage regulator time constant (T).  Typical Value = 0.086. Default: 0.0
    :tb: Voltage regulator time constant (T).  Typical Value = 9. Default: 0.0
    :tc: Voltage regulator time constant (T).  Typical Value = 3. Default: 0.0
    :te: Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 1. Default: 0.0
    :th: Exciter field current limiter time constant (T).  Typical Value = 0.08. Default: 0.0
    :tj: Exciter field current limiter time constant (T).  Typical Value = 0.02. Default: 0.0
    :tk: Voltage regulator time constant (T).  Typical Value = 0.18. Default: 0.0
    :vamax: Maximum voltage regulator output (V).  Typical Value = 75. Default: 0.0
    :vamin: Minimum voltage regulator output (V).  Typical Value = -75. Default: 0.0
    :ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (V) equals V(V).  Typical Value = 7.4. Default: 0.0
    :ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (V).  Typical Value = 5.55. Default: 0.0
    :vfelim: Exciter field current limit reference (V).  Typical Value = 19. Default: 0.0
    :vhmax: Maximum field current limiter signal reference (V).  Typical Value = 75. Default: 0.0
    :vrmax: Maximum voltage regulator output (V).  Typical Value = 44. Default: 0.0
    :vrmin: Minimum voltage regulator output (V).  Typical Value = -36. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "ka": [Profile.DY.value, ],
        "kc": [Profile.DY.value, ],
        "kd": [Profile.DY.value, ],
        "ke": [Profile.DY.value, ],
        "kh": [Profile.DY.value, ],
        "seve1": [Profile.DY.value, ],
        "seve2": [Profile.DY.value, ],
        "ta": [Profile.DY.value, ],
        "tb": [Profile.DY.value, ],
        "tc": [Profile.DY.value, ],
        "te": [Profile.DY.value, ],
        "th": [Profile.DY.value, ],
        "tj": [Profile.DY.value, ],
        "tk": [Profile.DY.value, ],
        "vamax": [Profile.DY.value, ],
        "vamin": [Profile.DY.value, ],
        "ve1": [Profile.DY.value, ],
        "ve2": [Profile.DY.value, ],
        "vfelim": [Profile.DY.value, ],
        "vhmax": [Profile.DY.value, ],
        "vrmax": [Profile.DY.value, ],
        "vrmin": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, ka = 0.0, kc = 0.0, kd = 0.0, ke = 0.0, kh = 0.0, seve1 = 0.0, seve2 = 0.0, ta = 0.0, tb = 0.0, tc = 0.0, te = 0.0, th = 0.0, tj = 0.0, tk = 0.0, vamax = 0.0, vamin = 0.0, ve1 = 0.0, ve2 = 0.0, vfelim = 0.0, vhmax = 0.0, vrmax = 0.0, vrmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ka = ka
        self.kc = kc
        self.kd = kd
        self.ke = ke
        self.kh = kh
        self.seve1 = seve1
        self.seve2 = seve2
        self.ta = ta
        self.tb = tb
        self.tc = tc
        self.te = te
        self.th = th
        self.tj = tj
        self.tk = tk
        self.vamax = vamax
        self.vamin = vamin
        self.ve1 = ve1
        self.ve2 = ve2
        self.vfelim = vfelim
        self.vhmax = vhmax
        self.vrmax = vrmax
        self.vrmin = vrmin

    def __str__(self):
        str = "class=ExcIEEEAC6A\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
