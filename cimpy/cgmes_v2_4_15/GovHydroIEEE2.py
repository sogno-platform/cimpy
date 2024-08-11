from .TurbineGovernorDynamics import TurbineGovernorDynamics
from .CGMESProfile import Profile


class GovHydroIEEE2(TurbineGovernorDynamics):
    """
    IEEE hydro turbine governor model represents plants with straightforward penstock configurations and hydraulic-dashpot governors.  Ref

    :aturb: Turbine numerator multiplier (Aturb).  Typical Value = -1. Default: 0.0
    :bturb: Turbine denominator multiplier (Bturb).  Typical Value = 0.5. Default: 0.0
    :gv1: Nonlinear gain point 1, PU gv (Gv1).  Typical Value = 0. Default: 0.0
    :gv2: Nonlinear gain point 2, PU gv (Gv2).  Typical Value = 0. Default: 0.0
    :gv3: Nonlinear gain point 3, PU gv (Gv3).  Typical Value = 0. Default: 0.0
    :gv4: Nonlinear gain point 4, PU gv (Gv4).  Typical Value = 0. Default: 0.0
    :gv5: Nonlinear gain point 5, PU gv (Gv5).  Typical Value = 0. Default: 0.0
    :gv6: Nonlinear gain point 6, PU gv (Gv6).  Typical Value = 0. Default: 0.0
    :kturb: Turbine gain (Kturb).  Typical Value = 1. Default: 0.0
    :mwbase: Base for power values (MWbase) (> 0).  Unit = MW. Default: 0.0
    :pgv1: Nonlinear gain point 1, PU power (Pgv1).  Typical Value = 0. Default: 0.0
    :pgv2: Nonlinear gain point 2, PU power (Pgv2).  Typical Value = 0. Default: 0.0
    :pgv3: Nonlinear gain point 3, PU power (Pgv3).  Typical Value = 0. Default: 0.0
    :pgv4: Nonlinear gain point 4, PU power (Pgv4).  Typical Value = 0. Default: 0.0
    :pgv5: Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0. Default: 0.0
    :pgv6: Nonlinear gain point 6, PU power (Pgv6).  Typical Value = 0. Default: 0.0
    :pmax: Maximum gate opening (Pmax).  Typical Value = 1. Default: 0.0
    :pmin: Minimum gate opening (Pmin).  Typical Value = 0. Default: 0.0
    :rperm: Permanent droop (Rperm).  Typical Value = 0.05. Default: 0.0
    :rtemp: Temporary droop (Rtemp).  Typical Value = 0.5. Default: 0.0
    :tg: Gate servo time constant (Tg).  Typical Value = 0.5. Default: 0.0
    :tp: Pilot servo valve time constant (Tp).  Typical Value = 0.03. Default: 0.0
    :tr: Dashpot time constant (Tr).  Typical Value = 12. Default: 0.0
    :tw: Water inertia time constant (Tw).  Typical Value = 2. Default: 0.0
    :uc: Maximum gate closing velocity (Uc) (<0).  Typical Value = -0.1. Default: 0.0
    :uo: Maximum gate opening velocity (Uo). Unit = PU/sec.  Typical Value = 0.1. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "aturb": [Profile.DY.value, ],
        "bturb": [Profile.DY.value, ],
        "gv1": [Profile.DY.value, ],
        "gv2": [Profile.DY.value, ],
        "gv3": [Profile.DY.value, ],
        "gv4": [Profile.DY.value, ],
        "gv5": [Profile.DY.value, ],
        "gv6": [Profile.DY.value, ],
        "kturb": [Profile.DY.value, ],
        "mwbase": [Profile.DY.value, ],
        "pgv1": [Profile.DY.value, ],
        "pgv2": [Profile.DY.value, ],
        "pgv3": [Profile.DY.value, ],
        "pgv4": [Profile.DY.value, ],
        "pgv5": [Profile.DY.value, ],
        "pgv6": [Profile.DY.value, ],
        "pmax": [Profile.DY.value, ],
        "pmin": [Profile.DY.value, ],
        "rperm": [Profile.DY.value, ],
        "rtemp": [Profile.DY.value, ],
        "tg": [Profile.DY.value, ],
        "tp": [Profile.DY.value, ],
        "tr": [Profile.DY.value, ],
        "tw": [Profile.DY.value, ],
        "uc": [Profile.DY.value, ],
        "uo": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class TurbineGovernorDynamics:\n" + TurbineGovernorDynamics.__doc__

    def __init__(self, aturb = 0.0, bturb = 0.0, gv1 = 0.0, gv2 = 0.0, gv3 = 0.0, gv4 = 0.0, gv5 = 0.0, gv6 = 0.0, kturb = 0.0, mwbase = 0.0, pgv1 = 0.0, pgv2 = 0.0, pgv3 = 0.0, pgv4 = 0.0, pgv5 = 0.0, pgv6 = 0.0, pmax = 0.0, pmin = 0.0, rperm = 0.0, rtemp = 0.0, tg = 0.0, tp = 0.0, tr = 0.0, tw = 0.0, uc = 0.0, uo = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.aturb = aturb
        self.bturb = bturb
        self.gv1 = gv1
        self.gv2 = gv2
        self.gv3 = gv3
        self.gv4 = gv4
        self.gv5 = gv5
        self.gv6 = gv6
        self.kturb = kturb
        self.mwbase = mwbase
        self.pgv1 = pgv1
        self.pgv2 = pgv2
        self.pgv3 = pgv3
        self.pgv4 = pgv4
        self.pgv5 = pgv5
        self.pgv6 = pgv6
        self.pmax = pmax
        self.pmin = pmin
        self.rperm = rperm
        self.rtemp = rtemp
        self.tg = tg
        self.tp = tp
        self.tr = tr
        self.tw = tw
        self.uc = uc
        self.uo = uo

    def __str__(self):
        str = "class=GovHydroIEEE2\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
