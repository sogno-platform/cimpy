from .TurbineGovernorDynamics import TurbineGovernorDynamics
from .CGMESProfile import Profile


class GovHydro1(TurbineGovernorDynamics):
    """
    Basic Hydro turbine governor model.

    :at: Turbine gain (At) (>0).  Typical Value = 1.2. Default: 0.0
    :dturb: Turbine damping factor (Dturb) (>=0).  Typical Value = 0.5. Default: 0.0
    :gmax: Maximum gate opening (Gmax) (>0).  Typical Value = 1. Default: 0.0
    :gmin: Minimum gate opening (Gmin) (>=0).  Typical Value = 0. Default: 0.0
    :hdam: Turbine nominal head (hdam).  Typical Value = 1. Default: 0.0
    :mwbase: Base for power values (MWbase) (> 0).  Unit = MW. Default: 0.0
    :qnl: No-load flow at nominal head (qnl) (>=0).  Typical Value = 0.08. Default: 0.0
    :rperm: Permanent droop (R) (>0).  Typical Value = 0.04. Default: 0.0
    :rtemp: Temporary droop (r) (>R).  Typical Value = 0.3. Default: 0.0
    :tf: Filter time constant () (>0).  Typical Value = 0.05. Default: 0.0
    :tg: Gate servo time constant (Tg) (>0).  Typical Value = 0.5. Default: 0.0
    :tr: Washout time constant (Tr) (>0).  Typical Value = 5. Default: 0.0
    :tw: Water inertia time constant (Tw) (>0).  Typical Value = 1. Default: 0.0
    :velm: Maximum gate velocity (Vlem) (>0).  Typical Value = 0.2. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "at": [Profile.DY.value, ],
        "dturb": [Profile.DY.value, ],
        "gmax": [Profile.DY.value, ],
        "gmin": [Profile.DY.value, ],
        "hdam": [Profile.DY.value, ],
        "mwbase": [Profile.DY.value, ],
        "qnl": [Profile.DY.value, ],
        "rperm": [Profile.DY.value, ],
        "rtemp": [Profile.DY.value, ],
        "tf": [Profile.DY.value, ],
        "tg": [Profile.DY.value, ],
        "tr": [Profile.DY.value, ],
        "tw": [Profile.DY.value, ],
        "velm": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class TurbineGovernorDynamics:\n" + TurbineGovernorDynamics.__doc__

    def __init__(self, at = 0.0, dturb = 0.0, gmax = 0.0, gmin = 0.0, hdam = 0.0, mwbase = 0.0, qnl = 0.0, rperm = 0.0, rtemp = 0.0, tf = 0.0, tg = 0.0, tr = 0.0, tw = 0.0, velm = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.at = at
        self.dturb = dturb
        self.gmax = gmax
        self.gmin = gmin
        self.hdam = hdam
        self.mwbase = mwbase
        self.qnl = qnl
        self.rperm = rperm
        self.rtemp = rtemp
        self.tf = tf
        self.tg = tg
        self.tr = tr
        self.tw = tw
        self.velm = velm

    def __str__(self):
        str = "class=GovHydro1\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
