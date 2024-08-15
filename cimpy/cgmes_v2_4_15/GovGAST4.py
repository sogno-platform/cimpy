from .TurbineGovernorDynamics import TurbineGovernorDynamics
from .CGMESProfile import Profile


class GovGAST4(TurbineGovernorDynamics):
    """
    Generic turbogas.

    :bp: Droop (bp).  Typical Value = 0.05. Default: 0.0
    :ktm: Compressor gain (K).  Typical Value = 0. Default: 0.0
    :mnef: Fuel flow maximum negative error value (MN).  Typical Value = -0.05. Default: 0.0
    :mxef: Fuel flow maximum positive error value (MX).  Typical Value = 0.05. Default: 0.0
    :rymn: Minimum valve opening (RYMN).  Typical Value = 0. Default: 0.0
    :rymx: Maximum valve opening (RYMX).  Typical Value = 1.1. Default: 0.0
    :ta: Maximum gate opening velocity (T).  Typical Value = 3. Default: 0.0
    :tc: Maximum gate closing velocity (T).  Typical Value = 0.5. Default: 0.0
    :tcm: Fuel control time constant (T).  Typical Value = 0.1. Default: 0.0
    :tm: Compressor discharge volume time constant (T).  Typical Value = 0.2. Default: 0.0
    :tv: Time constant of fuel valve positioner (T).  Typical Value = 0.1. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "bp": [Profile.DY.value, ],
        "ktm": [Profile.DY.value, ],
        "mnef": [Profile.DY.value, ],
        "mxef": [Profile.DY.value, ],
        "rymn": [Profile.DY.value, ],
        "rymx": [Profile.DY.value, ],
        "ta": [Profile.DY.value, ],
        "tc": [Profile.DY.value, ],
        "tcm": [Profile.DY.value, ],
        "tm": [Profile.DY.value, ],
        "tv": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class TurbineGovernorDynamics:\n" + TurbineGovernorDynamics.__doc__

    def __init__(self, bp = 0.0, ktm = 0.0, mnef = 0.0, mxef = 0.0, rymn = 0.0, rymx = 0.0, ta = 0.0, tc = 0.0, tcm = 0.0, tm = 0.0, tv = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.bp = bp
        self.ktm = ktm
        self.mnef = mnef
        self.mxef = mxef
        self.rymn = rymn
        self.rymx = rymx
        self.ta = ta
        self.tc = tc
        self.tcm = tcm
        self.tm = tm
        self.tv = tv

    def __str__(self):
        str = "class=GovGAST4\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
