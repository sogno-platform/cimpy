from .TurbineGovernorDynamics import TurbineGovernorDynamics


class GovGAST1(TurbineGovernorDynamics):
    """
    Modified single shaft gas turbine.

    :mwbase: Base for power values (<i>MWbase</i>) (&gt; 0).  Unit = MW. Default: 0.0
    :r: Permanent droop (<i>R</i>) (&gt;0).  Typical value = 0,04. Default: 0.0
    :t1: Governor mechanism time constant (<i>T1</i>) (&gt;= 0).  <i>T1</i> represents the natural valve positioning time constant of the governor for small disturbances, as seen when rate limiting is not in effect.  Typical value = 0,5. Default: 0
    :t2: Turbine power time constant (<i>T2</i>) (&gt;= 0). <i>T2</i> represents delay due to internal energy storage of the gas turbine engine. <i>T2</i> can be used to give a rough approximation to the delay associated with acceleration of the compressor spool of a multi-shaft engine, or with the compressibility of gas in the plenum of the free power turbine of an aero-derivative unit, for example.  Typical value = 0,5. Default: 0
    :t3: Turbine exhaust temperature time constant (<i>T3</i>) (&gt;= 0).  <i>T3</i> represents delay in the exhaust temperature and load limiting system. Typical value = 3. Default: 0
    :lmax: Ambient temperature load limit (<i>Lmax</i>).  <i>Lmax</i> is the turbine power output corresponding to the limiting exhaust gas temperature.  Typical value = 1. Default: 0.0
    :kt: Temperature limiter gain (<i>Kt</i>).  Typical value = 3. Default: 0.0
    :vmax: Maximum turbine power, PU of MWbase (<i>Vmax</i>) (&gt; GovGAST1.vmin).  Typical value = 1. Default: 0.0
    :vmin: Minimum turbine power, PU of MWbase (<i>Vmin</i>) (&lt; GovGAST1.vmax).  Typical value = 0. Default: 0.0
    :fidle: Fuel flow at zero power output (<i>Fidle</i>).  Typical value = 0,18. Default: 0.0
    :rmax: Maximum fuel valve opening rate (<i>Rmax</i>).  Unit = PU / s.  Typical value = 1. Default: 0.0
    :loadinc: Valve position change allowed at fast rate (<i>Loadinc</i>).  Typical value = 0,05. Default: 0.0
    :tltr: Valve position averaging time constant (<i>Tltr</i>) (&gt;= 0).  Typical value = 10. Default: 0
    :ltrate: Maximum long term fuel valve opening rate (<i>Ltrate</i>).  Typical value = 0,02. Default: 0.0
    :a: Turbine power time constant numerator scale factor (<i>a</i>).  Typical value = 0,8. Default: 0.0
    :b: Turbine power time constant denominator scale factor (<i>b</i>) (&gt;0).  Typical value = 1. Default: 0.0
    :db1: Intentional dead-band width (<i>db1</i>).  Unit = Hz.  Typical value = 0. Default: 0.0
    :eps: Intentional db hysteresis (<i>eps</i>).  Unit = Hz.  Typical value = 0. Default: 0.0
    :db2: Unintentional dead-band (<i>db2</i>).  Unit = MW.  Typical value = 0. Default: 0.0
    :gv1: Nonlinear gain point 1, PU gv (<i>Gv1</i>).  Typical value = 0. Default: 0.0
    :pgv1: Nonlinear gain point 1, PU power (<i>Pgv1</i>).  Typical value = 0. Default: 0.0
    :gv2: Nonlinear gain point 2,PU gv (<i>Gv2</i>).  Typical value = 0. Default: 0.0
    :pgv2: Nonlinear gain point 2, PU power (<i>Pgv2</i>).  Typical value = 0. Default: 0.0
    :gv3: Nonlinear gain point 3, PU gv (<i>Gv3</i>).  Typical value = 0. Default: 0.0
    :pgv3: Nonlinear gain point 3, PU power (<i>Pgv3</i>).  Typical value = 0. Default: 0.0
    :gv4: Nonlinear gain point 4, PU gv (<i>Gv4</i>).  Typical value = 0. Default: 0.0
    :pgv4: Nonlinear gain point 4, PU power (<i>Pgv4</i>).  Typical value = 0. Default: 0.0
    :gv5: Nonlinear gain point 5, PU gv (<i>Gv5</i>).  Typical value = 0. Default: 0.0
    :pgv5: Nonlinear gain point 5, PU power (<i>Pgv5</i>).  Typical value = 0. Default: 0.0
    :gv6: Nonlinear gain point 6, PU gv (<i>Gv6</i>).  Typical value = 0. Default: 0.0
    :pgv6: Nonlinear gain point 6, PU power (<i>Pgv6</i>).  Typical value = 0. Default: 0.0
    :ka: Governor gain (<i>Ka</i>).  Typical value = 0. Default: 0.0
    :t4: Governor lead time constant (<i>T4</i>) (&gt;= 0).  Typical value = 0. Default: 0
    :t5: Governor lag time constant (<i>T5</i>) (&gt;= 0).  If = 0, entire gain and lead-lag block is bypassed.  Typical value = 0. Default: 0
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
        "lmax": [
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
        "fidle": [
            cgmesProfile.DY.value,
        ],
        "rmax": [
            cgmesProfile.DY.value,
        ],
        "loadinc": [
            cgmesProfile.DY.value,
        ],
        "tltr": [
            cgmesProfile.DY.value,
        ],
        "ltrate": [
            cgmesProfile.DY.value,
        ],
        "a": [
            cgmesProfile.DY.value,
        ],
        "b": [
            cgmesProfile.DY.value,
        ],
        "db1": [
            cgmesProfile.DY.value,
        ],
        "eps": [
            cgmesProfile.DY.value,
        ],
        "db2": [
            cgmesProfile.DY.value,
        ],
        "gv1": [
            cgmesProfile.DY.value,
        ],
        "pgv1": [
            cgmesProfile.DY.value,
        ],
        "gv2": [
            cgmesProfile.DY.value,
        ],
        "pgv2": [
            cgmesProfile.DY.value,
        ],
        "gv3": [
            cgmesProfile.DY.value,
        ],
        "pgv3": [
            cgmesProfile.DY.value,
        ],
        "gv4": [
            cgmesProfile.DY.value,
        ],
        "pgv4": [
            cgmesProfile.DY.value,
        ],
        "gv5": [
            cgmesProfile.DY.value,
        ],
        "pgv5": [
            cgmesProfile.DY.value,
        ],
        "gv6": [
            cgmesProfile.DY.value,
        ],
        "pgv6": [
            cgmesProfile.DY.value,
        ],
        "ka": [
            cgmesProfile.DY.value,
        ],
        "t4": [
            cgmesProfile.DY.value,
        ],
        "t5": [
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
        lmax=0.0,
        kt=0.0,
        vmax=0.0,
        vmin=0.0,
        fidle=0.0,
        rmax=0.0,
        loadinc=0.0,
        tltr=0,
        ltrate=0.0,
        a=0.0,
        b=0.0,
        db1=0.0,
        eps=0.0,
        db2=0.0,
        gv1=0.0,
        pgv1=0.0,
        gv2=0.0,
        pgv2=0.0,
        gv3=0.0,
        pgv3=0.0,
        gv4=0.0,
        pgv4=0.0,
        gv5=0.0,
        pgv5=0.0,
        gv6=0.0,
        pgv6=0.0,
        ka=0.0,
        t4=0,
        t5=0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.mwbase = mwbase
        self.r = r
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.lmax = lmax
        self.kt = kt
        self.vmax = vmax
        self.vmin = vmin
        self.fidle = fidle
        self.rmax = rmax
        self.loadinc = loadinc
        self.tltr = tltr
        self.ltrate = ltrate
        self.a = a
        self.b = b
        self.db1 = db1
        self.eps = eps
        self.db2 = db2
        self.gv1 = gv1
        self.pgv1 = pgv1
        self.gv2 = gv2
        self.pgv2 = pgv2
        self.gv3 = gv3
        self.pgv3 = pgv3
        self.gv4 = gv4
        self.pgv4 = pgv4
        self.gv5 = gv5
        self.pgv5 = pgv5
        self.gv6 = gv6
        self.pgv6 = pgv6
        self.ka = ka
        self.t4 = t4
        self.t5 = t5

    def __str__(self):
        str = "class=GovGAST1\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
