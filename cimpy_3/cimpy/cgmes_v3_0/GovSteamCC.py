from .CrossCompoundTurbineGovernorDynamics import CrossCompoundTurbineGovernorDynamics


class GovSteamCC(CrossCompoundTurbineGovernorDynamics):
    """
    Cross compound turbine governor.  Unlike tandem compound units, cross compound units are not on the same shaft.

    :mwbase: Base for power values (<i>MWbase</i>) (&gt; 0).  Unit = MW. Default: 0.0
    :pmaxhp: Maximum HP value position (<i>Pmaxhp</i>).  Typical value = 1. Default: 0.0
    :rhp: HP governor droop (<i>Rhp</i>) (&gt; 0).  Typical value = 0,05. Default: 0.0
    :t1hp: HP governor time constant (<i>T1hp</i>) (&gt;= 0).  Typical value = 0,1. Default: 0
    :t3hp: HP turbine time constant (<i>T3hp</i>) (&gt;= 0).  Typical value = 0,1. Default: 0
    :t4hp: HP turbine time constant (<i>T4hp</i>) (&gt;= 0).  Typical value = 0,1. Default: 0
    :t5hp: HP reheater time constant (<i>T5hp</i>) (&gt;= 0).  Typical value = 10. Default: 0
    :fhp: Fraction of HP power ahead of reheater (<i>Fhp</i>).  Typical value = 0,3. Default: 0.0
    :dhp: HP damping factor (<i>Dhp</i>).  Typical value = 0. Default: 0.0
    :pmaxlp: Maximum LP value position (<i>Pmaxlp</i>).  Typical value = 1. Default: 0.0
    :rlp: LP governor droop (<i>Rlp</i>) (&gt; 0).  Typical value = 0,05. Default: 0.0
    :t1lp: LP governor time constant (<i>T1lp</i>) (&gt;= 0).  Typical value = 0,1. Default: 0
    :t3lp: LP turbine time constant (<i>T3lp</i>) (&gt;= 0).  Typical value = 0,1. Default: 0
    :t4lp: LP turbine time constant (<i>T4lp</i>) (&gt;= 0).  Typical value = 0,1. Default: 0
    :t5lp: LP reheater time constant (<i>T5lp</i>) (&gt;= 0).  Typical value = 10. Default: 0
    :flp: Fraction of LP power ahead of reheater (<i>Flp</i>).  Typical value = 0,7. Default: 0.0
    :dlp: LP damping factor (<i>Dlp</i>).  Typical value = 0. Default: 0.0
    """

    cgmesProfile = CrossCompoundTurbineGovernorDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "mwbase": [
            cgmesProfile.DY.value,
        ],
        "pmaxhp": [
            cgmesProfile.DY.value,
        ],
        "rhp": [
            cgmesProfile.DY.value,
        ],
        "t1hp": [
            cgmesProfile.DY.value,
        ],
        "t3hp": [
            cgmesProfile.DY.value,
        ],
        "t4hp": [
            cgmesProfile.DY.value,
        ],
        "t5hp": [
            cgmesProfile.DY.value,
        ],
        "fhp": [
            cgmesProfile.DY.value,
        ],
        "dhp": [
            cgmesProfile.DY.value,
        ],
        "pmaxlp": [
            cgmesProfile.DY.value,
        ],
        "rlp": [
            cgmesProfile.DY.value,
        ],
        "t1lp": [
            cgmesProfile.DY.value,
        ],
        "t3lp": [
            cgmesProfile.DY.value,
        ],
        "t4lp": [
            cgmesProfile.DY.value,
        ],
        "t5lp": [
            cgmesProfile.DY.value,
        ],
        "flp": [
            cgmesProfile.DY.value,
        ],
        "dlp": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class CrossCompoundTurbineGovernorDynamics: \n"
        + CrossCompoundTurbineGovernorDynamics.__doc__
    )

    def __init__(
        self,
        mwbase=0.0,
        pmaxhp=0.0,
        rhp=0.0,
        t1hp=0,
        t3hp=0,
        t4hp=0,
        t5hp=0,
        fhp=0.0,
        dhp=0.0,
        pmaxlp=0.0,
        rlp=0.0,
        t1lp=0,
        t3lp=0,
        t4lp=0,
        t5lp=0,
        flp=0.0,
        dlp=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.mwbase = mwbase
        self.pmaxhp = pmaxhp
        self.rhp = rhp
        self.t1hp = t1hp
        self.t3hp = t3hp
        self.t4hp = t4hp
        self.t5hp = t5hp
        self.fhp = fhp
        self.dhp = dhp
        self.pmaxlp = pmaxlp
        self.rlp = rlp
        self.t1lp = t1lp
        self.t3lp = t3lp
        self.t4lp = t4lp
        self.t5lp = t5lp
        self.flp = flp
        self.dlp = dlp

    def __str__(self):
        str = "class=GovSteamCC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
