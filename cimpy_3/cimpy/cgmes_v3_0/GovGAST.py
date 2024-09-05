from .TurbineGovernorDynamics import TurbineGovernorDynamics


class GovGAST(TurbineGovernorDynamics):
    """
    Single shaft gas turbine.

    :mwbase: Base for power values (<i>MWbase</i>) (&gt; 0).  Unit = MW. Default: 0.0
    :r: Permanent droop (<i>R</i>) (&gt;0). Typical value = 0,04. Default: 0.0
    :t1: Governor mechanism time constant (<i>T1</i>) (&gt;= 0).  <i>T1</i> represents the natural valve positioning time constant of the governor for small disturbances, as seen when rate limiting is not in effect.  Typical value = 0,5. Default: 0
    :t2: Turbine power time constant (<i>T2</i>) (&gt;= 0).  <i>T2</i> represents delay due to internal energy storage of the gas turbine engine. <i>T2</i> can be used to give a rough approximation to the delay associated with acceleration of the compressor spool of a multi-shaft engine, or with the compressibility of gas in the plenum of a free power turbine of an aero-derivative unit, for example.  Typical value = 0,5. Default: 0
    :t3: Turbine exhaust temperature time constant (<i>T3</i>) (&gt;= 0).  Typical value = 3. Default: 0
    :at: Ambient temperature load limit (<i>Load Limit</i>).  Typical value = 1. Default: 0.0
    :kt: Temperature limiter gain (<i>Kt</i>).  Typical value = 3. Default: 0.0
    :vmax: Maximum turbine power, PU of MWbase (<i>Vmax</i>) (&gt; GovGAST.vmin).  Typical value = 1. Default: 0.0
    :vmin: Minimum turbine power, PU of MWbase (<i>Vmin</i>) (&lt; GovGAST.vmax).  Typical value = 0. Default: 0.0
    :dturb: Turbine damping factor (<i>Dturb</i>).  Typical value = 0,18. Default: 0.0
    """

    cgmesProfile = TurbineGovernorDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "mwbase": [
            cgmesProfile.DY.value,
        ],
        "r": [
            cgmesProfile.DY.value,
        ],
        "t1": [
            cgmesProfile.DY.value,
        ],
        "t2": [
            cgmesProfile.DY.value,
        ],
        "t3": [
            cgmesProfile.DY.value,
        ],
        "at": [
            cgmesProfile.DY.value,
        ],
        "kt": [
            cgmesProfile.DY.value,
        ],
        "vmax": [
            cgmesProfile.DY.value,
        ],
        "vmin": [
            cgmesProfile.DY.value,
        ],
        "dturb": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class TurbineGovernorDynamics: \n"
        + TurbineGovernorDynamics.__doc__
    )

    def __init__(
        self,
        mwbase=0.0,
        r=0.0,
        t1=0,
        t2=0,
        t3=0,
        at=0.0,
        kt=0.0,
        vmax=0.0,
        vmin=0.0,
        dturb=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.mwbase = mwbase
        self.r = r
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.at = at
        self.kt = kt
        self.vmax = vmax
        self.vmin = vmin
        self.dturb = dturb

    def __str__(self):
        str = "class=GovGAST\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
