from .UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics
from .CGMESProfile import Profile


class UnderexcLimIEEE1(UnderexcitationLimiterDynamics):
    """
    The class represents the Type UEL1 model which has a circular limit boundary when plotted in terms of machine reactive power vs. real power output.  Reference: IEEE UEL1 421.5-2005 Section 10.1.

    :kuc: UEL center setting (K).  Typical Value = 1.38. Default: 0.0
    :kuf: UEL excitation system stabilizer gain (K).  Typical Value = 3.3. Default: 0.0
    :kui: UEL integral gain (K).  Typical Value = 0. Default: 0.0
    :kul: UEL proportional gain (K).  Typical Value = 100. Default: 0.0
    :kur: UEL radius setting (K).  Typical Value = 1.95. Default: 0.0
    :tu1: UEL lead time constant (T).  Typical Value = 0. Default: 0.0
    :tu2: UEL lag time constant (T).  Typical Value = 0.05. Default: 0.0
    :tu3: UEL lead time constant (T).  Typical Value = 0. Default: 0.0
    :tu4: UEL lag time constant (T).  Typical Value = 0. Default: 0.0
    :vucmax: UEL maximum limit for operating point phasor magnitude (V).  Typical Value = 5.8. Default: 0.0
    :vuimax: UEL integrator output maximum limit (V). Default: 0.0
    :vuimin: UEL integrator output minimum limit (V). Default: 0.0
    :vulmax: UEL output maximum limit (V).  Typical Value = 18. Default: 0.0
    :vulmin: UEL output minimum limit (V).  Typical Value = -18. Default: 0.0
    :vurmax: UEL maximum limit for radius phasor magnitude (V).  Typical Value = 5.8. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "kuc": [Profile.DY.value, ],
        "kuf": [Profile.DY.value, ],
        "kui": [Profile.DY.value, ],
        "kul": [Profile.DY.value, ],
        "kur": [Profile.DY.value, ],
        "tu1": [Profile.DY.value, ],
        "tu2": [Profile.DY.value, ],
        "tu3": [Profile.DY.value, ],
        "tu4": [Profile.DY.value, ],
        "vucmax": [Profile.DY.value, ],
        "vuimax": [Profile.DY.value, ],
        "vuimin": [Profile.DY.value, ],
        "vulmax": [Profile.DY.value, ],
        "vulmin": [Profile.DY.value, ],
        "vurmax": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class UnderexcitationLimiterDynamics:\n" + UnderexcitationLimiterDynamics.__doc__

    def __init__(self, kuc = 0.0, kuf = 0.0, kui = 0.0, kul = 0.0, kur = 0.0, tu1 = 0.0, tu2 = 0.0, tu3 = 0.0, tu4 = 0.0, vucmax = 0.0, vuimax = 0.0, vuimin = 0.0, vulmax = 0.0, vulmin = 0.0, vurmax = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.kuc = kuc
        self.kuf = kuf
        self.kui = kui
        self.kul = kul
        self.kur = kur
        self.tu1 = tu1
        self.tu2 = tu2
        self.tu3 = tu3
        self.tu4 = tu4
        self.vucmax = vucmax
        self.vuimax = vuimax
        self.vuimin = vuimin
        self.vulmax = vulmax
        self.vulmin = vulmin
        self.vurmax = vurmax

    def __str__(self):
        str = "class=UnderexcLimIEEE1\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
