from .TurbineGovernorDynamics import TurbineGovernorDynamics
from .CGMESProfile import Profile


class GovSteamIEEE1(TurbineGovernorDynamics):
    """
    IEEE steam turbine governor model.  Ref

    :k: Governor gain (reciprocal of droop) (K) (> 0).  Typical Value = 25. Default: 0.0
    :k1: Fraction of HP shaft power after first boiler pass (K1).  Typical Value = 0.2. Default: 0.0
    :k2: Fraction of LP shaft power after first boiler pass (K2).  Typical Value = 0. Default: 0.0
    :k3: Fraction of HP shaft power after second boiler pass (K3).  Typical Value = 0.3. Default: 0.0
    :k4: Fraction of LP shaft power after second boiler pass (K4).  Typical Value = 0. Default: 0.0
    :k5: Fraction of HP shaft power after third boiler pass (K5).  Typical Value = 0.5. Default: 0.0
    :k6: Fraction of LP shaft power after third boiler pass (K6).  Typical Value = 0. Default: 0.0
    :k7: Fraction of HP shaft power after fourth boiler pass (K7).  Typical Value = 0. Default: 0.0
    :k8: Fraction of LP shaft power after fourth boiler pass (K8).  Typical Value = 0. Default: 0.0
    :mwbase: Base for power values (MWbase) (> 0) Default: 0.0
    :pmax: Maximum valve opening (Pmax) (> Pmin).  Typical Value = 1. Default: 0.0
    :pmin: Minimum valve opening (Pmin) (>= 0).  Typical Value = 0. Default: 0.0
    :t1: Governor lag time constant (T1).  Typical Value = 0. Default: 0.0
    :t2: Governor lead time constant (T2).  Typical Value = 0. Default: 0.0
    :t3: Valve positioner time constant (T3) (> 0).  Typical Value = 0.1. Default: 0.0
    :t4: Inlet piping/steam bowl time constant (T4).  Typical Value = 0.3. Default: 0.0
    :t5: Time constant of second boiler pass (T5).  Typical Value = 5. Default: 0.0
    :t6: Time constant of third boiler pass (T6).  Typical Value = 0.5. Default: 0.0
    :t7: Time constant of fourth boiler pass (T7).  Typical Value = 0. Default: 0.0
    :uc: Maximum valve closing velocity (Uc) (< 0).  Unit = PU/sec.  Typical Value = -10. Default: 0.0
    :uo: Maximum valve opening velocity (Uo) (> 0).  Unit = PU/sec.  Typical Value = 1. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "k": [Profile.DY.value, ],
        "k1": [Profile.DY.value, ],
        "k2": [Profile.DY.value, ],
        "k3": [Profile.DY.value, ],
        "k4": [Profile.DY.value, ],
        "k5": [Profile.DY.value, ],
        "k6": [Profile.DY.value, ],
        "k7": [Profile.DY.value, ],
        "k8": [Profile.DY.value, ],
        "mwbase": [Profile.DY.value, ],
        "pmax": [Profile.DY.value, ],
        "pmin": [Profile.DY.value, ],
        "t1": [Profile.DY.value, ],
        "t2": [Profile.DY.value, ],
        "t3": [Profile.DY.value, ],
        "t4": [Profile.DY.value, ],
        "t5": [Profile.DY.value, ],
        "t6": [Profile.DY.value, ],
        "t7": [Profile.DY.value, ],
        "uc": [Profile.DY.value, ],
        "uo": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class TurbineGovernorDynamics:\n" + TurbineGovernorDynamics.__doc__

    def __init__(self, k = 0.0, k1 = 0.0, k2 = 0.0, k3 = 0.0, k4 = 0.0, k5 = 0.0, k6 = 0.0, k7 = 0.0, k8 = 0.0, mwbase = 0.0, pmax = 0.0, pmin = 0.0, t1 = 0.0, t2 = 0.0, t3 = 0.0, t4 = 0.0, t5 = 0.0, t6 = 0.0, t7 = 0.0, uc = 0.0, uo = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.k = k
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.k4 = k4
        self.k5 = k5
        self.k6 = k6
        self.k7 = k7
        self.k8 = k8
        self.mwbase = mwbase
        self.pmax = pmax
        self.pmin = pmin
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t5 = t5
        self.t6 = t6
        self.t7 = t7
        self.uc = uc
        self.uo = uo

    def __str__(self):
        str = "class=GovSteamIEEE1\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
