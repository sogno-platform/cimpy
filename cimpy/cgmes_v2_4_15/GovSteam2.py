from .TurbineGovernorDynamics import TurbineGovernorDynamics
from .CGMESProfile import Profile


class GovSteam2(TurbineGovernorDynamics):
    """
    Simplified governor model.

    :dbf: Frequency dead band (DBF).  Typical Value = 0. Default: 0.0
    :k: Governor gain (reciprocal of droop) (K).  Typical Value = 20. Default: 0.0
    :mnef: Fuel flow maximum negative error value (MN).  Typical Value = -1. Default: 0.0
    :mxef: Fuel flow maximum positive error value (MX).  Typical Value = 1. Default: 0.0
    :pmax: Maximum fuel flow (P).  Typical Value = 1. Default: 0.0
    :pmin: Minimum fuel flow (P).  Typical Value = 0. Default: 0.0
    :t1: Governor lag time constant (T) (>0).  Typical Value = 0.45. Default: 0.0
    :t2: Governor lead time constant (T) (may be 0).  Typical Value = 0. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "dbf": [Profile.DY.value, ],
        "k": [Profile.DY.value, ],
        "mnef": [Profile.DY.value, ],
        "mxef": [Profile.DY.value, ],
        "pmax": [Profile.DY.value, ],
        "pmin": [Profile.DY.value, ],
        "t1": [Profile.DY.value, ],
        "t2": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class TurbineGovernorDynamics:\n" + TurbineGovernorDynamics.__doc__

    def __init__(self, dbf = 0.0, k = 0.0, mnef = 0.0, mxef = 0.0, pmax = 0.0, pmin = 0.0, t1 = 0.0, t2 = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.dbf = dbf
        self.k = k
        self.mnef = mnef
        self.mxef = mxef
        self.pmax = pmax
        self.pmin = pmin
        self.t1 = t1
        self.t2 = t2

    def __str__(self):
        str = "class=GovSteam2\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
