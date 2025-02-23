from .TurbineGovernorDynamics import TurbineGovernorDynamics
from .CGMESProfile import Profile


class GovSteamCC(TurbineGovernorDynamics):
    """
    Cross compound turbine governor model.

    :dhp: HP damping factor (Dhp).  Typical Value = 0. Default: 0.0
    :dlp: LP damping factor (Dlp).  Typical Value = 0. Default: 0.0
    :fhp: Fraction of HP power ahead of reheater (Fhp).  Typical Value = 0.3. Default: 0.0
    :flp: Fraction of LP power ahead of reheater (Flp).  Typical Value = 0.7. Default: 0.0
    :mwbase: Base for power values (MWbase) (>0).  Unit = MW. Default: 0.0
    :pmaxhp: Maximum HP value position (Pmaxhp).  Typical Value = 1. Default: 0.0
    :pmaxlp: Maximum LP value position (Pmaxlp).  Typical Value = 1. Default: 0.0
    :rhp: HP governor droop (Rhp).  Typical Value = 0.05. Default: 0.0
    :rlp: LP governor droop (Rlp).  Typical Value = 0.05. Default: 0.0
    :t1hp: HP governor time constant (T1hp).  Typical Value = 0.1. Default: 0.0
    :t1lp: LP governor time constant (T1lp).  Typical Value = 0.1. Default: 0.0
    :t3hp: HP turbine time constant (T3hp).  Typical Value = 0.1. Default: 0.0
    :t3lp: LP turbine time constant (T3lp).  Typical Value = 0.1. Default: 0.0
    :t4hp: HP turbine time constant (T4hp).  Typical Value = 0.1. Default: 0.0
    :t4lp: LP turbine time constant (T4lp).  Typical Value = 0.1. Default: 0.0
    :t5hp: HP reheater time constant (T5hp).  Typical Value = 10. Default: 0.0
    :t5lp: LP reheater time constant (T5lp).  Typical Value = 10. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "dhp": [Profile.DY.value, ],
        "dlp": [Profile.DY.value, ],
        "fhp": [Profile.DY.value, ],
        "flp": [Profile.DY.value, ],
        "mwbase": [Profile.DY.value, ],
        "pmaxhp": [Profile.DY.value, ],
        "pmaxlp": [Profile.DY.value, ],
        "rhp": [Profile.DY.value, ],
        "rlp": [Profile.DY.value, ],
        "t1hp": [Profile.DY.value, ],
        "t1lp": [Profile.DY.value, ],
        "t3hp": [Profile.DY.value, ],
        "t3lp": [Profile.DY.value, ],
        "t4hp": [Profile.DY.value, ],
        "t4lp": [Profile.DY.value, ],
        "t5hp": [Profile.DY.value, ],
        "t5lp": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class TurbineGovernorDynamics:\n" + TurbineGovernorDynamics.__doc__

    def __init__(self, dhp = 0.0, dlp = 0.0, fhp = 0.0, flp = 0.0, mwbase = 0.0, pmaxhp = 0.0, pmaxlp = 0.0, rhp = 0.0, rlp = 0.0, t1hp = 0.0, t1lp = 0.0, t3hp = 0.0, t3lp = 0.0, t4hp = 0.0, t4lp = 0.0, t5hp = 0.0, t5lp = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.dhp = dhp
        self.dlp = dlp
        self.fhp = fhp
        self.flp = flp
        self.mwbase = mwbase
        self.pmaxhp = pmaxhp
        self.pmaxlp = pmaxlp
        self.rhp = rhp
        self.rlp = rlp
        self.t1hp = t1hp
        self.t1lp = t1lp
        self.t3hp = t3hp
        self.t3lp = t3lp
        self.t4hp = t4hp
        self.t4lp = t4lp
        self.t5hp = t5hp
        self.t5lp = t5lp

    def __str__(self):
        str = "class=GovSteamCC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
