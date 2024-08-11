from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcOEX3T(ExcitationSystemDynamics):
    """
    Modified IEEE Type ST1 Excitation System with semi-continuous and acting terminal voltage limiter.

    :e1: Saturation parameter (E). Default: 0.0
    :e2: Saturation parameter (E). Default: 0.0
    :ka: Gain (K). Default: 0.0
    :kc: Gain (K). Default: 0.0
    :kd: Gain (K). Default: 0.0
    :ke: Gain (K). Default: 0.0
    :kf: Gain (K). Default: 0.0
    :see1: Saturation parameter (S(E)). Default: 0.0
    :see2: Saturation parameter (S(E)). Default: 0.0
    :t1: Time constant (T). Default: 0.0
    :t2: Time constant (T). Default: 0.0
    :t3: Time constant (T). Default: 0.0
    :t4: Time constant (T). Default: 0.0
    :t5: Time constant (T). Default: 0.0
    :t6: Time constant (T). Default: 0.0
    :te: Time constant (T). Default: 0.0
    :tf: Time constant (T). Default: 0.0
    :vrmax: Limiter (V). Default: 0.0
    :vrmin: Limiter (V). Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "e1": [Profile.DY.value, ],
        "e2": [Profile.DY.value, ],
        "ka": [Profile.DY.value, ],
        "kc": [Profile.DY.value, ],
        "kd": [Profile.DY.value, ],
        "ke": [Profile.DY.value, ],
        "kf": [Profile.DY.value, ],
        "see1": [Profile.DY.value, ],
        "see2": [Profile.DY.value, ],
        "t1": [Profile.DY.value, ],
        "t2": [Profile.DY.value, ],
        "t3": [Profile.DY.value, ],
        "t4": [Profile.DY.value, ],
        "t5": [Profile.DY.value, ],
        "t6": [Profile.DY.value, ],
        "te": [Profile.DY.value, ],
        "tf": [Profile.DY.value, ],
        "vrmax": [Profile.DY.value, ],
        "vrmin": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, e1 = 0.0, e2 = 0.0, ka = 0.0, kc = 0.0, kd = 0.0, ke = 0.0, kf = 0.0, see1 = 0.0, see2 = 0.0, t1 = 0.0, t2 = 0.0, t3 = 0.0, t4 = 0.0, t5 = 0.0, t6 = 0.0, te = 0.0, tf = 0.0, vrmax = 0.0, vrmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.e1 = e1
        self.e2 = e2
        self.ka = ka
        self.kc = kc
        self.kd = kd
        self.ke = ke
        self.kf = kf
        self.see1 = see1
        self.see2 = see2
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t5 = t5
        self.t6 = t6
        self.te = te
        self.tf = tf
        self.vrmax = vrmax
        self.vrmin = vrmin

    def __str__(self):
        str = "class=ExcOEX3T\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
