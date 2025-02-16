from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics
from .CGMESProfile import Profile


class PssPTIST1(PowerSystemStabilizerDynamics):
    """
    PTI Microprocessor-Based Stabilizer type 1.

    :dtc: Time step related to activation of controls (Dtc).  Typical Value = 0.025. Default: 0.0
    :dtf: Time step frequency calculation (Dtf).  Typical Value = 0.025. Default: 0.0
    :dtp: Time step active power calculation (Dtp).  Typical Value = 0.0125. Default: 0.0
    :k: Gain (K).  Typical Value = 9. Default: 0.0
    :m: (M).  M=2*H.  Typical Value = 5. Default: 0.0
    :t1: Time constant (T1).  Typical Value = 0.3. Default: 0.0
    :t2: Time constant (T2).  Typical Value = 1. Default: 0.0
    :t3: Time constant (T3).  Typical Value = 0.2. Default: 0.0
    :t4: Time constant (T4).  Typical Value = 0.05. Default: 0.0
    :tf: Time constant (Tf).  Typical Value = 0.2. Default: 0.0
    :tp: Time constant (Tp).  Typical Value = 0.2. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "dtc": [Profile.DY.value, ],
        "dtf": [Profile.DY.value, ],
        "dtp": [Profile.DY.value, ],
        "k": [Profile.DY.value, ],
        "m": [Profile.DY.value, ],
        "t1": [Profile.DY.value, ],
        "t2": [Profile.DY.value, ],
        "t3": [Profile.DY.value, ],
        "t4": [Profile.DY.value, ],
        "tf": [Profile.DY.value, ],
        "tp": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class PowerSystemStabilizerDynamics:\n" + PowerSystemStabilizerDynamics.__doc__

    def __init__(self, dtc = 0.0, dtf = 0.0, dtp = 0.0, k = 0.0, m = 0.0, t1 = 0.0, t2 = 0.0, t3 = 0.0, t4 = 0.0, tf = 0.0, tp = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.dtc = dtc
        self.dtf = dtf
        self.dtp = dtp
        self.k = k
        self.m = m
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.tf = tf
        self.tp = tp

    def __str__(self):
        str = "class=PssPTIST1\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
