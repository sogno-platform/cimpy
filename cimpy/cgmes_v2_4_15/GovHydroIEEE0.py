from .TurbineGovernorDynamics import TurbineGovernorDynamics
from .CGMESProfile import Profile


class GovHydroIEEE0(TurbineGovernorDynamics):
    """
    IEEE Simplified Hydro Governor-Turbine Model.  Used for Mechanical-Hydraulic and Electro-Hydraulic turbine governors, with our without steam feedback. Typical values given are for Mechanical-Hydraulic.  Ref

    :k: Governor gain (K. Default: 0.0
    :mwbase: Base for power values (MWbase) (> 0).  Unit = MW. Default: 0.0
    :pmax: Gate maximum (Pmax). Default: 0.0
    :pmin: Gate minimum (Pmin). Default: 0.0
    :t1: Governor lag time constant (T1).  Typical Value = 0.25. Default: 0.0
    :t2: Governor lead time constant (T2.  Typical Value = 0. Default: 0.0
    :t3: Gate actuator time constant (T3).  Typical Value = 0.1. Default: 0.0
    :t4: Water starting time (T4). Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "k": [Profile.DY.value, ],
        "mwbase": [Profile.DY.value, ],
        "pmax": [Profile.DY.value, ],
        "pmin": [Profile.DY.value, ],
        "t1": [Profile.DY.value, ],
        "t2": [Profile.DY.value, ],
        "t3": [Profile.DY.value, ],
        "t4": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class TurbineGovernorDynamics:\n" + TurbineGovernorDynamics.__doc__

    def __init__(self, k = 0.0, mwbase = 0.0, pmax = 0.0, pmin = 0.0, t1 = 0.0, t2 = 0.0, t3 = 0.0, t4 = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.k = k
        self.mwbase = mwbase
        self.pmax = pmax
        self.pmin = pmin
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4

    def __str__(self):
        str = "class=GovHydroIEEE0\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
