from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics
from .CGMESProfile import Profile


class PssPTIST3(PowerSystemStabilizerDynamics):
    """
    PTI Microprocessor-Based Stabilizer type 3.

    :a0: Filter coefficient (A0). Default: 0.0
    :a1: Limiter (Al). Default: 0.0
    :a2: Filter coefficient (A2). Default: 0.0
    :a3: Filter coefficient (A3). Default: 0.0
    :a4: Filter coefficient (A4). Default: 0.0
    :a5: Filter coefficient (A5). Default: 0.0
    :al: Limiter (Al). Default: 0.0
    :athres: Threshold value above which output averaging will be bypassed (Athres).  Typical Value = 0.005. Default: 0.0
    :b0: Filter coefficient (B0). Default: 0.0
    :b1: Filter coefficient (B1). Default: 0.0
    :b2: Filter coefficient (B2). Default: 0.0
    :b3: Filter coefficient (B3). Default: 0.0
    :b4: Filter coefficient (B4). Default: 0.0
    :b5: Filter coefficient (B5). Default: 0.0
    :dl: Limiter (Dl). Default: 0.0
    :dtc: Time step related to activation of controls (0.03 for 50 Hz) (Dtc).  Typical Value = 0.025. Default: 0.0
    :dtf: Time step frequency calculation (0.03 for 50 Hz) (Dtf).  Typical Value = 0.025. Default: 0.0
    :dtp: Time step active power calculation (0.015 for 50 Hz) (Dtp).  Typical Value = 0.0125. Default: 0.0
    :isw: Digital/analog output switch (Isw). true = produce analog output false = convert to digital output, using tap selection table. Default: False
    :k: Gain (K).  Typical Value = 9. Default: 0.0
    :lthres: Threshold value (Lthres). Default: 0.0
    :m: (M).  M=2*H.  Typical Value = 5. Default: 0.0
    :nav: Number of control outputs to average (Nav) (1 <= Nav <= 16).  Typical Value = 4. Default: 0.0
    :ncl: Number of counts at limit to active limit function (Ncl) (>0). Default: 0.0
    :ncr: Number of counts until reset after limit function is triggered (Ncr). Default: 0.0
    :pmin: (Pmin). Default: 0.0
    :t1: Time constant (T1).  Typical Value = 0.3. Default: 0.0
    :t2: Time constant (T2).  Typical Value = 1. Default: 0.0
    :t3: Time constant (T3).  Typical Value = 0.2. Default: 0.0
    :t4: Time constant (T4).  Typical Value = 0.05. Default: 0.0
    :t5: Time constant (T5). Default: 0.0
    :t6: Time constant (T6). Default: 0.0
    :tf: Time constant (Tf).  Typical Value = 0.2. Default: 0.0
    :tp: Time constant (Tp).  Typical Value = 0.2. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "a0": [Profile.DY.value, ],
        "a1": [Profile.DY.value, ],
        "a2": [Profile.DY.value, ],
        "a3": [Profile.DY.value, ],
        "a4": [Profile.DY.value, ],
        "a5": [Profile.DY.value, ],
        "al": [Profile.DY.value, ],
        "athres": [Profile.DY.value, ],
        "b0": [Profile.DY.value, ],
        "b1": [Profile.DY.value, ],
        "b2": [Profile.DY.value, ],
        "b3": [Profile.DY.value, ],
        "b4": [Profile.DY.value, ],
        "b5": [Profile.DY.value, ],
        "dl": [Profile.DY.value, ],
        "dtc": [Profile.DY.value, ],
        "dtf": [Profile.DY.value, ],
        "dtp": [Profile.DY.value, ],
        "isw": [Profile.DY.value, ],
        "k": [Profile.DY.value, ],
        "lthres": [Profile.DY.value, ],
        "m": [Profile.DY.value, ],
        "nav": [Profile.DY.value, ],
        "ncl": [Profile.DY.value, ],
        "ncr": [Profile.DY.value, ],
        "pmin": [Profile.DY.value, ],
        "t1": [Profile.DY.value, ],
        "t2": [Profile.DY.value, ],
        "t3": [Profile.DY.value, ],
        "t4": [Profile.DY.value, ],
        "t5": [Profile.DY.value, ],
        "t6": [Profile.DY.value, ],
        "tf": [Profile.DY.value, ],
        "tp": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class PowerSystemStabilizerDynamics:\n" + PowerSystemStabilizerDynamics.__doc__

    def __init__(self, a0 = 0.0, a1 = 0.0, a2 = 0.0, a3 = 0.0, a4 = 0.0, a5 = 0.0, al = 0.0, athres = 0.0, b0 = 0.0, b1 = 0.0, b2 = 0.0, b3 = 0.0, b4 = 0.0, b5 = 0.0, dl = 0.0, dtc = 0.0, dtf = 0.0, dtp = 0.0, isw = False, k = 0.0, lthres = 0.0, m = 0.0, nav = 0.0, ncl = 0.0, ncr = 0.0, pmin = 0.0, t1 = 0.0, t2 = 0.0, t3 = 0.0, t4 = 0.0, t5 = 0.0, t6 = 0.0, tf = 0.0, tp = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.a0 = a0
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.al = al
        self.athres = athres
        self.b0 = b0
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.dl = dl
        self.dtc = dtc
        self.dtf = dtf
        self.dtp = dtp
        self.isw = isw
        self.k = k
        self.lthres = lthres
        self.m = m
        self.nav = nav
        self.ncl = ncl
        self.ncr = ncr
        self.pmin = pmin
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t5 = t5
        self.t6 = t6
        self.tf = tf
        self.tp = tp

    def __str__(self):
        str = "class=PssPTIST3\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
