from .TurbineGovernorDynamics import TurbineGovernorDynamics


class GovCT2(TurbineGovernorDynamics):
    """
    General governor with frequency-dependent fuel flow limit.  This model is a modification of the GovCT1<b> </b>model in order to represent the frequency-dependent fuel flow limit of a specific gas turbine manufacturer.

    :mwbase: Base for power values (<i>MWbase</i>) (&gt; 0).  Unit = MW. Default: 0.0
    :r: Permanent droop (<i>R</i>).  Typical value = 0,05. Default: 0.0
    :rselect: Feedback signal for droop (<i>Rselect</i>).  Typical value = electricalPower. Default: None
    :tpelec: Electrical power transducer time constant (<i>Tpelec</i>) (&gt;= 0).  Typical value = 2,5. Default: 0
    :maxerr: Maximum value for speed error signal (<i>Maxerr</i>) (&gt; GovCT2.minerr).  Typical value = 1. Default: 0.0
    :minerr: Minimum value for speed error signal (<i>Minerr</i>) (&lt; GovCT2.maxerr).  Typical value = -1. Default: 0.0
    :kpgov: Governor proportional gain (<i>Kpgov</i>).  Typical value = 4. Default: 0.0
    :kigov: Governor integral gain (<i>Kigov</i>).  Typical value = 0,45. Default: 0.0
    :kdgov: Governor derivative gain (<i>Kdgov</i>).  Typical value = 0. Default: 0.0
    :tdgov: Governor derivative controller time constant (<i>Tdgov</i>) (&gt;= 0).  Typical value = 1. Default: 0
    :vmax: Maximum valve position limit (<i>Vmax</i>) (&gt; GovCT2.vmin).  Typical value = 1. Default: 0.0
    :vmin: Minimum valve position limit (<i>Vmin</i>) (&lt; GovCT2.vmax).  Typical value = 0,175. Default: 0.0
    :tact: Actuator time constant (<i>Tact</i>) (&gt;= 0).  Typical value = 0,4. Default: 0
    :kturb: Turbine gain (<i>Kturb</i>).  Typical value = 1,9168. Default: 0.0
    :wfnl: No load fuel flow (<i>Wfnl</i>).  Typical value = 0,187. Default: 0.0
    :tb: Turbine lag time constant (<i>Tb</i>) (&gt;= 0).  Typical value = 0,1. Default: 0
    :tc: Turbine lead time constant (<i>Tc</i>) (&gt;= 0).  Typical value = 0. Default: 0
    :wfspd: Switch for fuel source characteristic to recognize that fuel flow, for a given fuel valve stroke, can be proportional to engine speed (<i>Wfspd</i>). true = fuel flow proportional to speed (for some gas turbines and diesel engines with positive displacement fuel injectors) false = fuel control system keeps fuel flow independent of engine speed. Typical value = false. Default: False
    :teng: Transport time delay for diesel engine used in representing diesel engines where there is a small but measurable transport delay between a change in fuel flow setting and the development of torque (<i>Teng</i>) (&gt;= 0).  <i>Teng</i> should be zero in all but special cases where this transport delay is of particular concern.  Typical value = 0. Default: 0
    :tfload: Load limiter time constant (<i>Tfload</i>) (&gt;= 0).  Typical value = 3. Default: 0
    :kpload: Load limiter proportional gain for PI controller (<i>Kpload</i>).  Typical value = 1. Default: 0.0
    :kiload: Load limiter integral gain for PI controller (<i>Kiload</i>).  Typical value = 1. Default: 0.0
    :ldref: Load limiter reference value (<i>Ldref</i>).  Typical value = 1. Default: 0.0
    :dm: Speed sensitivity coefficient (<i>Dm</i>).  <i>Dm</i> can represent either the variation of the engine power with the shaft speed or the variation of maximum power capability with shaft speed.  If it is positive it describes the falling slope of the engine speed verses power characteristic as speed increases. A slightly falling characteristic is typical for reciprocating engines and some aero-derivative turbines.  If it is negative the engine power is assumed to be unaffected by the shaft speed, but the maximum permissible fuel flow is taken to fall with falling shaft speed. This is characteristic of single-shaft industrial turbines due to exhaust temperature limits.  Typical value = 0. Default: 0.0
    :ropen: Maximum valve opening rate (<i>Ropen</i>).  Unit = PU / s.  Typical value = 99. Default: 0.0
    :rclose: Minimum valve closing rate (<i>Rclose</i>).  Unit = PU / s.  Typical value = -99. Default: 0.0
    :kimw: Power controller (reset) gain (<i>Kimw</i>).  The default value of 0,01 corresponds to a reset time of 100 seconds.  A value of 0,001 corresponds to a relatively slow-acting load controller.  Typical value = 0. Default: 0.0
    :aset: Acceleration limiter setpoint (<i>Aset</i>).  Unit = PU / s.  Typical value = 10. Default: 0.0
    :ka: Acceleration limiter gain (<i>Ka</i>).  Typical value = 10. Default: 0.0
    :ta: Acceleration limiter time constant (<i>Ta</i>) (&gt;= 0).  Typical value = 1. Default: 0
    :db: Speed governor deadband in PU speed (<i>db</i>).  In the majority of applications, it is recommended that this value be set to zero.  Typical value = 0. Default: 0.0
    :tsa: Temperature detection lead time constant (<i>Tsa</i>) (&gt;= 0).  Typical value = 0. Default: 0
    :tsb: Temperature detection lag time constant (<i>Tsb</i>) (&gt;= 0).  Typical value = 50. Default: 0
    :rup: Maximum rate of load limit increase (<i>Rup</i>).  Typical value = 99. Default: 0.0
    :rdown: Maximum rate of load limit decrease (<i>Rdown</i>).  Typical value = -99. Default: 0.0
    :prate: Ramp rate for frequency-dependent power limit (<i>Prate</i>).  Typical value = 0,017. Default: 0.0
    :flim1: Frequency threshold 1 (<i>Flim1</i>).  Unit = Hz.  Typical value = 59. Default: 0.0
    :plim1: Power limit 1 (<i>Plim1</i>).  Typical value = 0,8325. Default: 0.0
    :flim2: Frequency threshold 2 (<i>Flim2</i>).  Unit = Hz.  Typical value = 0. Default: 0.0
    :plim2: Power limit 2 (Plim2).  Typical value = 0. Default: 0.0
    :flim3: Frequency threshold 3 (<i>Flim3</i>).  Unit = Hz.  Typical value = 0. Default: 0.0
    :plim3: Power limit 3 (<i>Plim3</i>).  Typical value = 0. Default: 0.0
    :flim4: Frequency threshold 4 (<i>Flim4</i>).  Unit = Hz.  Typical value = 0. Default: 0.0
    :plim4: Power limit 4 (<i>Plim4</i>).  Typical value = 0. Default: 0.0
    :flim5: Frequency threshold 5 (<i>Flim5</i>).  Unit = Hz.  Typical value = 0. Default: 0.0
    :plim5: Power limit 5 (<i>Plim5</i>).  Typical value = 0. Default: 0.0
    :flim6: Frequency threshold 6 (<i>Flim6</i>).  Unit = Hz.  Typical value = 0. Default: 0.0
    :plim6: Power limit 6 (<i>Plim6</i>).  Typical value = 0. Default: 0.0
    :flim7: Frequency threshold 7 (<i>Flim7</i>).  Unit = Hz.  Typical value = 0. Default: 0.0
    :plim7: Power limit 7 (<i>Plim7</i>).  Typical value = 0. Default: 0.0
    :flim8: Frequency threshold 8 (<i>Flim8</i>).  Unit = Hz.  Typical value = 0. Default: 0.0
    :plim8: Power limit 8 (<i>Plim8</i>).  Typical value = 0. Default: 0.0
    :flim9: Frequency threshold 9 (<i>Flim9</i>).  Unit = Hz.  Typical value = 0. Default: 0.0
    :plim9: Power Limit 9 (<i>Plim9</i>).  Typical value = 0. Default: 0.0
    :flim10: Frequency threshold 10 (<i>Flim10</i>).  Unit = Hz.  Typical value = 0. Default: 0.0
    :plim10: Power limit 10 (<i>Plim10</i>).  Typical value = 0. Default: 0.0
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
        "rselect": [
            cgmesProfile.DY.value,
        ],
        "tpelec": [
            cgmesProfile.DY.value,
        ],
        "maxerr": [
            cgmesProfile.DY.value,
        ],
        "minerr": [
            cgmesProfile.DY.value,
        ],
        "kpgov": [
            cgmesProfile.DY.value,
        ],
        "kigov": [
            cgmesProfile.DY.value,
        ],
        "kdgov": [
            cgmesProfile.DY.value,
        ],
        "tdgov": [
            cgmesProfile.DY.value,
        ],
        "vmax": [
            cgmesProfile.DY.value,
        ],
        "vmin": [
            cgmesProfile.DY.value,
        ],
        "tact": [
            cgmesProfile.DY.value,
        ],
        "kturb": [
            cgmesProfile.DY.value,
        ],
        "wfnl": [
            cgmesProfile.DY.value,
        ],
        "tb": [
            cgmesProfile.DY.value,
        ],
        "tc": [
            cgmesProfile.DY.value,
        ],
        "wfspd": [
            cgmesProfile.DY.value,
        ],
        "teng": [
            cgmesProfile.DY.value,
        ],
        "tfload": [
            cgmesProfile.DY.value,
        ],
        "kpload": [
            cgmesProfile.DY.value,
        ],
        "kiload": [
            cgmesProfile.DY.value,
        ],
        "ldref": [
            cgmesProfile.DY.value,
        ],
        "dm": [
            cgmesProfile.DY.value,
        ],
        "ropen": [
            cgmesProfile.DY.value,
        ],
        "rclose": [
            cgmesProfile.DY.value,
        ],
        "kimw": [
            cgmesProfile.DY.value,
        ],
        "aset": [
            cgmesProfile.DY.value,
        ],
        "ka": [
            cgmesProfile.DY.value,
        ],
        "ta": [
            cgmesProfile.DY.value,
        ],
        "db": [
            cgmesProfile.DY.value,
        ],
        "tsa": [
            cgmesProfile.DY.value,
        ],
        "tsb": [
            cgmesProfile.DY.value,
        ],
        "rup": [
            cgmesProfile.DY.value,
        ],
        "rdown": [
            cgmesProfile.DY.value,
        ],
        "prate": [
            cgmesProfile.DY.value,
        ],
        "flim1": [
            cgmesProfile.DY.value,
        ],
        "plim1": [
            cgmesProfile.DY.value,
        ],
        "flim2": [
            cgmesProfile.DY.value,
        ],
        "plim2": [
            cgmesProfile.DY.value,
        ],
        "flim3": [
            cgmesProfile.DY.value,
        ],
        "plim3": [
            cgmesProfile.DY.value,
        ],
        "flim4": [
            cgmesProfile.DY.value,
        ],
        "plim4": [
            cgmesProfile.DY.value,
        ],
        "flim5": [
            cgmesProfile.DY.value,
        ],
        "plim5": [
            cgmesProfile.DY.value,
        ],
        "flim6": [
            cgmesProfile.DY.value,
        ],
        "plim6": [
            cgmesProfile.DY.value,
        ],
        "flim7": [
            cgmesProfile.DY.value,
        ],
        "plim7": [
            cgmesProfile.DY.value,
        ],
        "flim8": [
            cgmesProfile.DY.value,
        ],
        "plim8": [
            cgmesProfile.DY.value,
        ],
        "flim9": [
            cgmesProfile.DY.value,
        ],
        "plim9": [
            cgmesProfile.DY.value,
        ],
        "flim10": [
            cgmesProfile.DY.value,
        ],
        "plim10": [
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
        rselect=None,
        tpelec=0,
        maxerr=0.0,
        minerr=0.0,
        kpgov=0.0,
        kigov=0.0,
        kdgov=0.0,
        tdgov=0,
        vmax=0.0,
        vmin=0.0,
        tact=0,
        kturb=0.0,
        wfnl=0.0,
        tb=0,
        tc=0,
        wfspd=False,
        teng=0,
        tfload=0,
        kpload=0.0,
        kiload=0.0,
        ldref=0.0,
        dm=0.0,
        ropen=0.0,
        rclose=0.0,
        kimw=0.0,
        aset=0.0,
        ka=0.0,
        ta=0,
        db=0.0,
        tsa=0,
        tsb=0,
        rup=0.0,
        rdown=0.0,
        prate=0.0,
        flim1=0.0,
        plim1=0.0,
        flim2=0.0,
        plim2=0.0,
        flim3=0.0,
        plim3=0.0,
        flim4=0.0,
        plim4=0.0,
        flim5=0.0,
        plim5=0.0,
        flim6=0.0,
        plim6=0.0,
        flim7=0.0,
        plim7=0.0,
        flim8=0.0,
        plim8=0.0,
        flim9=0.0,
        plim9=0.0,
        flim10=0.0,
        plim10=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.mwbase = mwbase
        self.r = r
        self.rselect = rselect
        self.tpelec = tpelec
        self.maxerr = maxerr
        self.minerr = minerr
        self.kpgov = kpgov
        self.kigov = kigov
        self.kdgov = kdgov
        self.tdgov = tdgov
        self.vmax = vmax
        self.vmin = vmin
        self.tact = tact
        self.kturb = kturb
        self.wfnl = wfnl
        self.tb = tb
        self.tc = tc
        self.wfspd = wfspd
        self.teng = teng
        self.tfload = tfload
        self.kpload = kpload
        self.kiload = kiload
        self.ldref = ldref
        self.dm = dm
        self.ropen = ropen
        self.rclose = rclose
        self.kimw = kimw
        self.aset = aset
        self.ka = ka
        self.ta = ta
        self.db = db
        self.tsa = tsa
        self.tsb = tsb
        self.rup = rup
        self.rdown = rdown
        self.prate = prate
        self.flim1 = flim1
        self.plim1 = plim1
        self.flim2 = flim2
        self.plim2 = plim2
        self.flim3 = flim3
        self.plim3 = plim3
        self.flim4 = flim4
        self.plim4 = plim4
        self.flim5 = flim5
        self.plim5 = plim5
        self.flim6 = flim6
        self.plim6 = plim6
        self.flim7 = flim7
        self.plim7 = plim7
        self.flim8 = flim8
        self.plim8 = plim8
        self.flim9 = flim9
        self.plim9 = plim9
        self.flim10 = flim10
        self.plim10 = plim10

    def __str__(self):
        str = "class=GovCT2\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
