from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcAC2A(ExcitationSystemDynamics):
    """
    Modified IEEE AC2A alternator-supplied rectifier excitation system with different field current limit.

    :hvgate: Indicates if HV gate is active (HVgate). true = gate is used false = gate is not used. Typical Value = true. Default: False
    :ka: Voltage regulator gain (Ka).  Typical Value = 400. Default: 0.0
    :kb: Second stage regulator gain (Kb) (>0).  Exciter field current controller gain.  Typical Value = 25. Default: 0.0
    :kb1: Second stage regulator gain (Kb1). It is exciter field current controller gain used as alternative to Kb to represent a variant of the ExcAC2A model.  Typical Value = 25. Default: 0.0
    :kc: Rectifier loading factor proportional to commutating reactance (Kc).  Typical Value = 0.28. Default: 0.0
    :kd: Demagnetizing factor, a function of exciter alternator reactances (Kd).  Typical Value = 0.35. Default: 0.0
    :ke: Exciter constant related to self-excited field (Ke).  Typical Value = 1. Default: 0.0
    :kf: Excitation control system stabilizer gains (Kf).  Typical Value = 0.03. Default: 0.0
    :kh: Exciter field current feedback gain (Kh).  Typical Value = 1. Default: 0.0
    :kl: Exciter field current limiter gain (Kl).  Typical Value = 10. Default: 0.0
    :kl1: Coefficient to allow different usage of the model (Kl1).  Typical Value = 1. Default: 0.0
    :ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0. Default: 0.0
    :lvgate: Indicates if LV gate is active (LVgate). true = gate is used false = gate is not used. Typical Value = true. Default: False
    :seve1: Exciter saturation function value at the corresponding exciter voltage, Ve, back of commutating reactance (Se[Ve]).  Typical Value = 0.037. Default: 0.0
    :seve2: Exciter saturation function value at the corresponding exciter voltage, Ve, back of commutating reactance (Se[Ve]).  Typical Value = 0.012. Default: 0.0
    :ta: Voltage regulator time constant (Ta).  Typical Value = 0.02. Default: 0.0
    :tb: Voltage regulator time constant (Tb).  Typical Value = 0. Default: 0.0
    :tc: Voltage regulator time constant (T).  Typical Value = 0. Default: 0.0
    :te: Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 0.6. Default: 0.0
    :tf: Excitation control system stabilizer time constant (Tf).  Typical Value = 1. Default: 0.0
    :vamax: Maximum voltage regulator output (V).  Typical Value = 8. Default: 0.0
    :vamin: Minimum voltage regulator output (V).  Typical Value = -8. Default: 0.0
    :ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve).  Typical Value = 4.4. Default: 0.0
    :ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve).  Typical Value = 3.3. Default: 0.0
    :vfemax: Exciter field current limit reference (Vfemax).  Typical Value = 4.4. Default: 0.0
    :vlr: Maximum exciter field current (Vlr).  Typical Value = 4.4. Default: 0.0
    :vrmax: Maximum voltage regulator outputs (Vrmax).  Typical Value = 105. Default: 0.0
    :vrmin: Minimum voltage regulator outputs (Vrmin).  Typical Value = -95. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "hvgate": [Profile.DY.value, ],
        "ka": [Profile.DY.value, ],
        "kb": [Profile.DY.value, ],
        "kb1": [Profile.DY.value, ],
        "kc": [Profile.DY.value, ],
        "kd": [Profile.DY.value, ],
        "ke": [Profile.DY.value, ],
        "kf": [Profile.DY.value, ],
        "kh": [Profile.DY.value, ],
        "kl": [Profile.DY.value, ],
        "kl1": [Profile.DY.value, ],
        "ks": [Profile.DY.value, ],
        "lvgate": [Profile.DY.value, ],
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
        "vfemax": [Profile.DY.value, ],
        "vlr": [Profile.DY.value, ],
        "vrmax": [Profile.DY.value, ],
        "vrmin": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, hvgate = False, ka = 0.0, kb = 0.0, kb1 = 0.0, kc = 0.0, kd = 0.0, ke = 0.0, kf = 0.0, kh = 0.0, kl = 0.0, kl1 = 0.0, ks = 0.0, lvgate = False, seve1 = 0.0, seve2 = 0.0, ta = 0.0, tb = 0.0, tc = 0.0, te = 0.0, tf = 0.0, vamax = 0.0, vamin = 0.0, ve1 = 0.0, ve2 = 0.0, vfemax = 0.0, vlr = 0.0, vrmax = 0.0, vrmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.hvgate = hvgate
        self.ka = ka
        self.kb = kb
        self.kb1 = kb1
        self.kc = kc
        self.kd = kd
        self.ke = ke
        self.kf = kf
        self.kh = kh
        self.kl = kl
        self.kl1 = kl1
        self.ks = ks
        self.lvgate = lvgate
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
        self.vfemax = vfemax
        self.vlr = vlr
        self.vrmax = vrmax
        self.vrmin = vrmin

    def __str__(self):
        str = "class=ExcAC2A\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
