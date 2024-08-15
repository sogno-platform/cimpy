from .TurbineGovernorDynamics import TurbineGovernorDynamics
from .CGMESProfile import Profile


class GovSteamFV3(TurbineGovernorDynamics):
    """
    Simplified GovSteamIEEE1 Steam turbine governor model with Prmax limit and fast valving.

    :k: Governor gain, (reciprocal of droop) (K).  Typical Value = 20. Default: 0.0
    :k1: Fraction of turbine power developed after first boiler pass (K1).  Typical Value = 0.2. Default: 0.0
    :k2: Fraction of turbine power developed after second boiler pass (K2).  Typical Value = 0.2. Default: 0.0
    :k3: Fraction of hp turbine power developed after crossover or third boiler pass (K3). Typical Value = 0.6. Default: 0.0
    :mwbase: Base for power values (MWbase) (>0).  Unit = MW. Default: 0.0
    :pmax: Maximum valve opening, PU of MWbase (Pmax).  Typical Value = 1. Default: 0.0
    :pmin: Minimum valve opening, PU of MWbase (Pmin).  Typical Value = 0. Default: 0.0
    :prmax: Max. pressure in reheater (Prmax).  Typical Value = 1. Default: 0.0
    :t1: Governor lead time constant (T1).  Typical Value = 0. Default: 0.0
    :t2: Governor lag time constant (T2).  Typical Value = 0. Default: 0.0
    :t3: Valve positioner time constant (T3).  Typical Value = 0. Default: 0.0
    :t4: Inlet piping/steam bowl time constant (T4).  Typical Value = 0.2. Default: 0.0
    :t5: Time constant of second boiler pass (i.e. reheater) (T5).  Typical Value = 0.5. Default: 0.0
    :t6: Time constant of crossover or third boiler pass (T6).  Typical Value = 10. Default: 0.0
    :ta: Time to close intercept valve (IV) (Ta).  Typical Value = 0.97. Default: 0.0
    :tb: Time until IV starts to reopen (Tb).  Typical Value = 0.98. Default: 0.0
    :tc: Time until IV is fully open (Tc).  Typical Value = 0.99. Default: 0.0
    :uc: Maximum valve closing velocity (Uc).  Unit = PU/sec.  Typical Value = -1. Default: 0.0
    :uo: Maximum valve opening velocity (Uo).  Unit = PU/sec.  Typical Value = 0.1. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "k": [Profile.DY.value, ],
        "k1": [Profile.DY.value, ],
        "k2": [Profile.DY.value, ],
        "k3": [Profile.DY.value, ],
        "mwbase": [Profile.DY.value, ],
        "pmax": [Profile.DY.value, ],
        "pmin": [Profile.DY.value, ],
        "prmax": [Profile.DY.value, ],
        "t1": [Profile.DY.value, ],
        "t2": [Profile.DY.value, ],
        "t3": [Profile.DY.value, ],
        "t4": [Profile.DY.value, ],
        "t5": [Profile.DY.value, ],
        "t6": [Profile.DY.value, ],
        "ta": [Profile.DY.value, ],
        "tb": [Profile.DY.value, ],
        "tc": [Profile.DY.value, ],
        "uc": [Profile.DY.value, ],
        "uo": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class TurbineGovernorDynamics:\n" + TurbineGovernorDynamics.__doc__

    def __init__(self, k = 0.0, k1 = 0.0, k2 = 0.0, k3 = 0.0, mwbase = 0.0, pmax = 0.0, pmin = 0.0, prmax = 0.0, t1 = 0.0, t2 = 0.0, t3 = 0.0, t4 = 0.0, t5 = 0.0, t6 = 0.0, ta = 0.0, tb = 0.0, tc = 0.0, uc = 0.0, uo = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.k = k
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.mwbase = mwbase
        self.pmax = pmax
        self.pmin = pmin
        self.prmax = prmax
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t5 = t5
        self.t6 = t6
        self.ta = ta
        self.tb = tb
        self.tc = tc
        self.uc = uc
        self.uo = uo

    def __str__(self):
        str = "class=GovSteamFV3\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
