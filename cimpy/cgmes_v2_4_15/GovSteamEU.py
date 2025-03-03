from .TurbineGovernorDynamics import TurbineGovernorDynamics
from .CGMESProfile import Profile


class GovSteamEU(TurbineGovernorDynamics):
    """
    Simplified model  of boiler and steam turbine with PID governor.

    :chc: Control valves rate closing limit (Chc).  Unit = PU/sec.  Typical Value = -3.3. Default: 0.0
    :cho: Control valves rate opening limit (Cho).  Unit = PU/sec.  Typical Value = 0.17. Default: 0.0
    :cic: Intercept valves rate closing limit (Cic).  Typical Value = -2.2. Default: 0.0
    :cio: Intercept valves rate opening limit (Cio).  Typical Value = 0.123. Default: 0.0
    :db1: Dead band of the frequency corrector (db1).  Typical Value = 0. Default: 0.0
    :db2: Dead band of the speed governor (db2).  Typical Value = 0.0004. Default: 0.0
    :hhpmax: Maximum control valve position (Hhpmax).  Typical Value = 1. Default: 0.0
    :ke: Gain of the power controller (Ke).  Typical Value = 0.65. Default: 0.0
    :kfcor: Gain of the frequency corrector (Kfcor).  Typical Value = 20. Default: 0.0
    :khp: Fraction of total turbine output generated by HP part (Khp).  Typical Value = 0.277. Default: 0.0
    :klp: Fraction of total turbine output generated by HP part (Klp).  Typical Value = 0.723. Default: 0.0
    :kwcor: Gain of the speed governor (Kwcor).  Typical Value = 20. Default: 0.0
    :mwbase: Base for power values (MWbase) (>0).  Unit = MW. Default: 0.0
    :pmax: Maximal active power of the turbine (Pmax).  Typical Value = 1. Default: 0.0
    :prhmax: Maximum low pressure limit (Prhmax).  Typical Value = 1.4. Default: 0.0
    :simx: Intercept valves transfer limit (Simx).  Typical Value = 0.425. Default: 0.0
    :tb: Boiler time constant (Tb).  Typical Value = 100. Default: 0.0
    :tdp: Derivative time constant of the power controller (Tdp).  Typical Value = 0. Default: 0.0
    :ten: Electro hydraulic transducer (Ten).  Typical Value = 0.1. Default: 0.0
    :tf: Frequency transducer time constant (Tf).  Typical Value = 0. Default: 0.0
    :tfp: Time constant of the power controller (Tfp).  Typical Value = 0. Default: 0.0
    :thp: High pressure (HP) time constant of the turbine (Thp).  Typical Value = 0.31. Default: 0.0
    :tip: Integral time constant of the power controller (Tip).  Typical Value = 2. Default: 0.0
    :tlp: Low pressure(LP) time constant of the turbine (Tlp).  Typical Value = 0.45. Default: 0.0
    :tp: Power transducer time constant (Tp).  Typical Value = 0.07. Default: 0.0
    :trh: Reheater  time constant of the turbine (Trh).  Typical Value = 8. Default: 0.0
    :tvhp: Control valves servo time constant (Tvhp).  Typical Value = 0.1. Default: 0.0
    :tvip: Intercept valves servo time constant (Tvip).  Typical Value = 0.15. Default: 0.0
    :tw: Speed transducer time constant (Tw).  Typical Value = 0.02. Default: 0.0
    :wfmax: Upper limit for frequency correction (Wfmax).  Typical Value = 0.05. Default: 0.0
    :wfmin: Lower limit for frequency correction (Wfmin).  Typical Value = -0.05. Default: 0.0
    :wmax1: Emergency speed control lower limit (wmax1).  Typical Value = 1.025. Default: 0.0
    :wmax2: Emergency speed control upper limit (wmax2).  Typical Value = 1.05. Default: 0.0
    :wwmax: Upper limit for the speed governor (Wwmax).  Typical Value = 0.1. Default: 0.0
    :wwmin: Lower limit for the speed governor frequency correction (Wwmin).  Typical Value = -1. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "chc": [Profile.DY.value, ],
        "cho": [Profile.DY.value, ],
        "cic": [Profile.DY.value, ],
        "cio": [Profile.DY.value, ],
        "db1": [Profile.DY.value, ],
        "db2": [Profile.DY.value, ],
        "hhpmax": [Profile.DY.value, ],
        "ke": [Profile.DY.value, ],
        "kfcor": [Profile.DY.value, ],
        "khp": [Profile.DY.value, ],
        "klp": [Profile.DY.value, ],
        "kwcor": [Profile.DY.value, ],
        "mwbase": [Profile.DY.value, ],
        "pmax": [Profile.DY.value, ],
        "prhmax": [Profile.DY.value, ],
        "simx": [Profile.DY.value, ],
        "tb": [Profile.DY.value, ],
        "tdp": [Profile.DY.value, ],
        "ten": [Profile.DY.value, ],
        "tf": [Profile.DY.value, ],
        "tfp": [Profile.DY.value, ],
        "thp": [Profile.DY.value, ],
        "tip": [Profile.DY.value, ],
        "tlp": [Profile.DY.value, ],
        "tp": [Profile.DY.value, ],
        "trh": [Profile.DY.value, ],
        "tvhp": [Profile.DY.value, ],
        "tvip": [Profile.DY.value, ],
        "tw": [Profile.DY.value, ],
        "wfmax": [Profile.DY.value, ],
        "wfmin": [Profile.DY.value, ],
        "wmax1": [Profile.DY.value, ],
        "wmax2": [Profile.DY.value, ],
        "wwmax": [Profile.DY.value, ],
        "wwmin": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class TurbineGovernorDynamics:\n" + TurbineGovernorDynamics.__doc__

    def __init__(self, chc = 0.0, cho = 0.0, cic = 0.0, cio = 0.0, db1 = 0.0, db2 = 0.0, hhpmax = 0.0, ke = 0.0, kfcor = 0.0, khp = 0.0, klp = 0.0, kwcor = 0.0, mwbase = 0.0, pmax = 0.0, prhmax = 0.0, simx = 0.0, tb = 0.0, tdp = 0.0, ten = 0.0, tf = 0.0, tfp = 0.0, thp = 0.0, tip = 0.0, tlp = 0.0, tp = 0.0, trh = 0.0, tvhp = 0.0, tvip = 0.0, tw = 0.0, wfmax = 0.0, wfmin = 0.0, wmax1 = 0.0, wmax2 = 0.0, wwmax = 0.0, wwmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.chc = chc
        self.cho = cho
        self.cic = cic
        self.cio = cio
        self.db1 = db1
        self.db2 = db2
        self.hhpmax = hhpmax
        self.ke = ke
        self.kfcor = kfcor
        self.khp = khp
        self.klp = klp
        self.kwcor = kwcor
        self.mwbase = mwbase
        self.pmax = pmax
        self.prhmax = prhmax
        self.simx = simx
        self.tb = tb
        self.tdp = tdp
        self.ten = ten
        self.tf = tf
        self.tfp = tfp
        self.thp = thp
        self.tip = tip
        self.tlp = tlp
        self.tp = tp
        self.trh = trh
        self.tvhp = tvhp
        self.tvip = tvip
        self.tw = tw
        self.wfmax = wfmax
        self.wfmin = wfmin
        self.wmax1 = wmax1
        self.wmax2 = wmax2
        self.wwmax = wwmax
        self.wwmin = wwmin

    def __str__(self):
        str = "class=GovSteamEU\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
