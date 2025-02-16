from .TurbineGovernorDynamics import TurbineGovernorDynamics
from .CGMESProfile import Profile


class GovSteamFV2(TurbineGovernorDynamics):
    """
    Steam turbine governor with reheat time constants and modeling of the effects of fast valve closing to reduce mechanical power.

    :dt: (Dt). Default: 0.0
    :k: Fraction of the turbine power developed by turbine sections not involved in fast valving (K). Default: 0.0
    :mwbase: Alternate Base used instead of Machine base in equipment model if necessary (MWbase) (>0).  Unit = MW. Default: 0.0
    :r: (R). Default: 0.0
    :t1: Governor time constant (T1). Default: 0.0
    :t3: Reheater time constant (T3). Default: 0.0
    :ta: Time after initial time for valve to close (Ta). Default: 0.0
    :tb: Time after initial time for valve to begin opening (Tb). Default: 0.0
    :tc: Time after initial time for valve to become fully open (Tc). Default: 0.0
    :ti: Initial time to begin fast valving (Ti). Default: 0.0
    :tt: Time constant with which power falls off after intercept valve closure (Tt). Default: 0.0
    :vmax: (Vmax). Default: 0.0
    :vmin: (Vmin). Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "dt": [Profile.DY.value, ],
        "k": [Profile.DY.value, ],
        "mwbase": [Profile.DY.value, ],
        "r": [Profile.DY.value, ],
        "t1": [Profile.DY.value, ],
        "t3": [Profile.DY.value, ],
        "ta": [Profile.DY.value, ],
        "tb": [Profile.DY.value, ],
        "tc": [Profile.DY.value, ],
        "ti": [Profile.DY.value, ],
        "tt": [Profile.DY.value, ],
        "vmax": [Profile.DY.value, ],
        "vmin": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class TurbineGovernorDynamics:\n" + TurbineGovernorDynamics.__doc__

    def __init__(self, dt = 0.0, k = 0.0, mwbase = 0.0, r = 0.0, t1 = 0.0, t3 = 0.0, ta = 0.0, tb = 0.0, tc = 0.0, ti = 0.0, tt = 0.0, vmax = 0.0, vmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.dt = dt
        self.k = k
        self.mwbase = mwbase
        self.r = r
        self.t1 = t1
        self.t3 = t3
        self.ta = ta
        self.tb = tb
        self.tc = tc
        self.ti = ti
        self.tt = tt
        self.vmax = vmax
        self.vmin = vmin

    def __str__(self):
        str = "class=GovSteamFV2\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
