from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics
from .CGMESProfile import Profile


class Pss2B(PowerSystemStabilizerDynamics):
    """
    Modified IEEE PSS2B Model.  Extra lead/lag (or rate) block added at end (up to 4 lead/lags total).

    :a: Numerator constant (a).  Typical Value = 1. Default: 0.0
    :inputSignal1Type: Type of input signal #1.  Typical Value = rotorSpeed. Default: None
    :inputSignal2Type: Type of input signal #2.  Typical Value = generatorElectricalPower. Default: None
    :ks1: Stabilizer gain (Ks1).  Typical Value = 12. Default: 0.0
    :ks2: Gain on signal #2 (Ks2).  Typical Value = 0.2. Default: 0.0
    :ks3: Gain on signal #2 input before ramp-tracking filter (Ks3).  Typical Value = 1. Default: 0.0
    :ks4: Gain on signal #2 input after ramp-tracking filter (Ks4).  Typical Value = 1. Default: 0.0
    :m: Denominator order of ramp tracking filter (M).  Typical Value = 5. Default: 0
    :n: Order of ramp tracking filter (N).  Typical Value = 1. Default: 0
    :t1: Lead/lag time constant (T1).  Typical Value = 0.12. Default: 0.0
    :t10: Lead/lag time constant (T10).  Typical Value = 0. Default: 0.0
    :t11: Lead/lag time constant (T11).  Typical Value = 0. Default: 0.0
    :t2: Lead/lag time constant (T2).  Typical Value = 0.02. Default: 0.0
    :t3: Lead/lag time constant (T3).  Typical Value = 0.3. Default: 0.0
    :t4: Lead/lag time constant (T4).  Typical Value = 0.02. Default: 0.0
    :t6: Time constant on signal #1 (T6).  Typical Value = 0. Default: 0.0
    :t7: Time constant on signal #2 (T7).  Typical Value = 2. Default: 0.0
    :t8: Lead of ramp tracking filter (T8).  Typical Value = 0.2. Default: 0.0
    :t9: Lag of ramp tracking filter (T9).  Typical Value = 0.1. Default: 0.0
    :ta: Lead constant (Ta).  Typical Value = 0. Default: 0.0
    :tb: Lag time constant (Tb).  Typical Value = 0. Default: 0.0
    :tw1: First washout on signal #1 (Tw1).  Typical Value = 2. Default: 0.0
    :tw2: Second washout on signal #1 (Tw2).  Typical Value = 2. Default: 0.0
    :tw3: First washout on signal #2 (Tw3).  Typical Value = 2. Default: 0.0
    :tw4: Second washout on signal #2 (Tw4).  Typical Value = 0. Default: 0.0
    :vsi1max: Input signal #1 max limit (Vsi1max).  Typical Value = 2. Default: 0.0
    :vsi1min: Input signal #1 min limit (Vsi1min).  Typical Value = -2. Default: 0.0
    :vsi2max: Input signal #2 max limit (Vsi2max).  Typical Value = 2. Default: 0.0
    :vsi2min: Input signal #2 min limit (Vsi2min).  Typical Value = -2. Default: 0.0
    :vstmax: Stabilizer output max limit (Vstmax).  Typical Value = 0.1. Default: 0.0
    :vstmin: Stabilizer output min limit (Vstmin).  Typical Value = -0.1. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "a": [Profile.DY.value, ],
        "inputSignal1Type": [Profile.DY.value, ],
        "inputSignal2Type": [Profile.DY.value, ],
        "ks1": [Profile.DY.value, ],
        "ks2": [Profile.DY.value, ],
        "ks3": [Profile.DY.value, ],
        "ks4": [Profile.DY.value, ],
        "m": [Profile.DY.value, ],
        "n": [Profile.DY.value, ],
        "t1": [Profile.DY.value, ],
        "t10": [Profile.DY.value, ],
        "t11": [Profile.DY.value, ],
        "t2": [Profile.DY.value, ],
        "t3": [Profile.DY.value, ],
        "t4": [Profile.DY.value, ],
        "t6": [Profile.DY.value, ],
        "t7": [Profile.DY.value, ],
        "t8": [Profile.DY.value, ],
        "t9": [Profile.DY.value, ],
        "ta": [Profile.DY.value, ],
        "tb": [Profile.DY.value, ],
        "tw1": [Profile.DY.value, ],
        "tw2": [Profile.DY.value, ],
        "tw3": [Profile.DY.value, ],
        "tw4": [Profile.DY.value, ],
        "vsi1max": [Profile.DY.value, ],
        "vsi1min": [Profile.DY.value, ],
        "vsi2max": [Profile.DY.value, ],
        "vsi2min": [Profile.DY.value, ],
        "vstmax": [Profile.DY.value, ],
        "vstmin": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class PowerSystemStabilizerDynamics:\n" + PowerSystemStabilizerDynamics.__doc__

    def __init__(self, a = 0.0, inputSignal1Type = None, inputSignal2Type = None, ks1 = 0.0, ks2 = 0.0, ks3 = 0.0, ks4 = 0.0, m = 0, n = 0, t1 = 0.0, t10 = 0.0, t11 = 0.0, t2 = 0.0, t3 = 0.0, t4 = 0.0, t6 = 0.0, t7 = 0.0, t8 = 0.0, t9 = 0.0, ta = 0.0, tb = 0.0, tw1 = 0.0, tw2 = 0.0, tw3 = 0.0, tw4 = 0.0, vsi1max = 0.0, vsi1min = 0.0, vsi2max = 0.0, vsi2min = 0.0, vstmax = 0.0, vstmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.a = a
        self.inputSignal1Type = inputSignal1Type
        self.inputSignal2Type = inputSignal2Type
        self.ks1 = ks1
        self.ks2 = ks2
        self.ks3 = ks3
        self.ks4 = ks4
        self.m = m
        self.n = n
        self.t1 = t1
        self.t10 = t10
        self.t11 = t11
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t6 = t6
        self.t7 = t7
        self.t8 = t8
        self.t9 = t9
        self.ta = ta
        self.tb = tb
        self.tw1 = tw1
        self.tw2 = tw2
        self.tw3 = tw3
        self.tw4 = tw4
        self.vsi1max = vsi1max
        self.vsi1min = vsi1min
        self.vsi2max = vsi2max
        self.vsi2min = vsi2min
        self.vstmax = vstmax
        self.vstmin = vstmin

    def __str__(self):
        str = "class=Pss2B\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
