from .UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics
from .CGMESProfile import Profile


class UnderexcLimIEEE2(UnderexcitationLimiterDynamics):
    """
    The class represents the Type UEL2 which has either a straight-line or multi-segment characteristic when plotted in terms of machine reactive power output vs. real power output.  Reference: IEEE UEL2 421.5-2005 Section 10.2.  (Limit characteristic lookup table shown in Figure 10.4 (p 32) of the standard).

    :k1: UEL terminal voltage exponent applied to real power input to UEL limit look-up table (k1).  Typical Value = 2. Default: 0.0
    :k2: UEL terminal voltage exponent applied to reactive power output from UEL limit look-up table (k2).  Typical Value = 2. Default: 0.0
    :kfb: Gain associated with optional integrator feedback input signal to UEL (K).  Typical Value = 0. Default: 0.0
    :kuf: UEL excitation system stabilizer gain (K).  Typical Value = 0. Default: 0.0
    :kui: UEL integral gain (K).  Typical Value = 0.5. Default: 0.0
    :kul: UEL proportional gain (K).  Typical Value = 0.8. Default: 0.0
    :p0: Real power values for endpoints (P).  Typical Value = 0. Default: 0.0
    :p1: Real power values for endpoints (P).  Typical Value = 0.3. Default: 0.0
    :p10: Real power values for endpoints (P). Default: 0.0
    :p2: Real power values for endpoints (P).  Typical Value = 0.6. Default: 0.0
    :p3: Real power values for endpoints (P).  Typical Value = 0.9. Default: 0.0
    :p4: Real power values for endpoints (P).  Typical Value = 1.02. Default: 0.0
    :p5: Real power values for endpoints (P). Default: 0.0
    :p6: Real power values for endpoints (P). Default: 0.0
    :p7: Real power values for endpoints (P). Default: 0.0
    :p8: Real power values for endpoints (P). Default: 0.0
    :p9: Real power values for endpoints (P). Default: 0.0
    :q0: Reactive power values for endpoints (Q).  Typical Value = -0.31. Default: 0.0
    :q1: Reactive power values for endpoints (Q).  Typical Value = -0.31. Default: 0.0
    :q10: Reactive power values for endpoints (Q). Default: 0.0
    :q2: Reactive power values for endpoints (Q).  Typical Value = -0.28. Default: 0.0
    :q3: Reactive power values for endpoints (Q).  Typical Value = -0.21. Default: 0.0
    :q4: Reactive power values for endpoints (Q).  Typical Value = 0. Default: 0.0
    :q5: Reactive power values for endpoints (Q). Default: 0.0
    :q6: Reactive power values for endpoints (Q). Default: 0.0
    :q7: Reactive power values for endpoints (Q). Default: 0.0
    :q8: Reactive power values for endpoints (Q). Default: 0.0
    :q9: Reactive power values for endpoints (Q). Default: 0.0
    :tu1: UEL lead time constant (T).  Typical Value = 0. Default: 0.0
    :tu2: UEL lag time constant (T).  Typical Value = 0. Default: 0.0
    :tu3: UEL lead time constant (T).  Typical Value = 0. Default: 0.0
    :tu4: UEL lag time constant (T).  Typical Value = 0. Default: 0.0
    :tul: Time constant associated with optional integrator feedback input signal to UEL (T).  Typical Value = 0. Default: 0.0
    :tup: Real power filter time constant (T).  Typical Value = 5. Default: 0.0
    :tuq: Reactive power filter time constant (T).  Typical Value = 0. Default: 0.0
    :tuv: Voltage filter time constant (T).  Typical Value = 5. Default: 0.0
    :vuimax: UEL integrator output maximum limit (V).  Typical Value = 0.25. Default: 0.0
    :vuimin: UEL integrator output minimum limit (V).  Typical Value = 0. Default: 0.0
    :vulmax: UEL output maximum limit (V).  Typical Value = 0.25. Default: 0.0
    :vulmin: UEL output minimum limit (V).  Typical Value = 0. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "k1": [Profile.DY.value, ],
        "k2": [Profile.DY.value, ],
        "kfb": [Profile.DY.value, ],
        "kuf": [Profile.DY.value, ],
        "kui": [Profile.DY.value, ],
        "kul": [Profile.DY.value, ],
        "p0": [Profile.DY.value, ],
        "p1": [Profile.DY.value, ],
        "p10": [Profile.DY.value, ],
        "p2": [Profile.DY.value, ],
        "p3": [Profile.DY.value, ],
        "p4": [Profile.DY.value, ],
        "p5": [Profile.DY.value, ],
        "p6": [Profile.DY.value, ],
        "p7": [Profile.DY.value, ],
        "p8": [Profile.DY.value, ],
        "p9": [Profile.DY.value, ],
        "q0": [Profile.DY.value, ],
        "q1": [Profile.DY.value, ],
        "q10": [Profile.DY.value, ],
        "q2": [Profile.DY.value, ],
        "q3": [Profile.DY.value, ],
        "q4": [Profile.DY.value, ],
        "q5": [Profile.DY.value, ],
        "q6": [Profile.DY.value, ],
        "q7": [Profile.DY.value, ],
        "q8": [Profile.DY.value, ],
        "q9": [Profile.DY.value, ],
        "tu1": [Profile.DY.value, ],
        "tu2": [Profile.DY.value, ],
        "tu3": [Profile.DY.value, ],
        "tu4": [Profile.DY.value, ],
        "tul": [Profile.DY.value, ],
        "tup": [Profile.DY.value, ],
        "tuq": [Profile.DY.value, ],
        "tuv": [Profile.DY.value, ],
        "vuimax": [Profile.DY.value, ],
        "vuimin": [Profile.DY.value, ],
        "vulmax": [Profile.DY.value, ],
        "vulmin": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class UnderexcitationLimiterDynamics:\n" + UnderexcitationLimiterDynamics.__doc__

    def __init__(self, k1 = 0.0, k2 = 0.0, kfb = 0.0, kuf = 0.0, kui = 0.0, kul = 0.0, p0 = 0.0, p1 = 0.0, p10 = 0.0, p2 = 0.0, p3 = 0.0, p4 = 0.0, p5 = 0.0, p6 = 0.0, p7 = 0.0, p8 = 0.0, p9 = 0.0, q0 = 0.0, q1 = 0.0, q10 = 0.0, q2 = 0.0, q3 = 0.0, q4 = 0.0, q5 = 0.0, q6 = 0.0, q7 = 0.0, q8 = 0.0, q9 = 0.0, tu1 = 0.0, tu2 = 0.0, tu3 = 0.0, tu4 = 0.0, tul = 0.0, tup = 0.0, tuq = 0.0, tuv = 0.0, vuimax = 0.0, vuimin = 0.0, vulmax = 0.0, vulmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.k1 = k1
        self.k2 = k2
        self.kfb = kfb
        self.kuf = kuf
        self.kui = kui
        self.kul = kul
        self.p0 = p0
        self.p1 = p1
        self.p10 = p10
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5
        self.p6 = p6
        self.p7 = p7
        self.p8 = p8
        self.p9 = p9
        self.q0 = q0
        self.q1 = q1
        self.q10 = q10
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5
        self.q6 = q6
        self.q7 = q7
        self.q8 = q8
        self.q9 = q9
        self.tu1 = tu1
        self.tu2 = tu2
        self.tu3 = tu3
        self.tu4 = tu4
        self.tul = tul
        self.tup = tup
        self.tuq = tuq
        self.tuv = tuv
        self.vuimax = vuimax
        self.vuimin = vuimin
        self.vulmax = vulmax
        self.vulmin = vulmin

    def __str__(self):
        str = "class=UnderexcLimIEEE2\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
