from .TurbineGovernorDynamics import TurbineGovernorDynamics
from .CGMESProfile import Profile


class GovCT1(TurbineGovernorDynamics):
    """
    General model for any prime mover with a PID governor, used primarily for combustion turbine and combined cycle units. This model can be used to represent a variety of prime movers controlled by PID governors.  It is suitable, for example, for representation of     Additional information on this model is available in the 2012 IEEE report, , section 3.1.2.3 page 3-4 (GGOV1).

    :aset: Acceleration limiter setpoint (Aset).  Unit = PU/sec.  Typical Value = 0.01. Default: 0.0
    :db: Speed governor dead band in per unit speed (db).  In the majority of applications, it is recommended that this value be set to zero.  Typical Value = 0. Default: 0.0
    :dm: Speed sensitivity coefficient (Dm).  Dm can represent either the variation of the engine power with the shaft speed or the variation of maximum power capability with shaft speed.  If it is positive it describes the falling slope of the engine speed verses power characteristic as speed increases. A slightly falling characteristic is typical for reciprocating engines and some aero-derivative turbines.  If it is negative the engine power is assumed to be unaffected by the shaft speed, but the maximum permissible fuel flow is taken to fall with falling shaft speed. This is characteristic of single-shaft industrial turbines due to exhaust temperature limits.  Typical Value = 0. Default: 0.0
    :ka: Acceleration limiter gain (Ka).  Typical Value = 10. Default: 0.0
    :kdgov: Governor derivative gain (Kdgov).  Typical Value = 0. Default: 0.0
    :kigov: Governor integral gain (Kigov).  Typical Value = 2. Default: 0.0
    :kiload: Load limiter integral gain for PI controller (Kiload).  Typical Value = 0.67. Default: 0.0
    :kimw: Power controller (reset) gain (Kimw).  The default value of 0.01 corresponds to a reset time of 100 seconds.  A value of 0.001 corresponds to a relatively slow acting load controller.  Typical Value = 0.01. Default: 0.0
    :kpgov: Governor proportional gain (Kpgov).  Typical Value = 10. Default: 0.0
    :kpload: Load limiter proportional gain for PI controller (Kpload).  Typical Value = 2. Default: 0.0
    :kturb: Turbine gain (Kturb) (>0).  Typical Value = 1.5. Default: 0.0
    :ldref: Load limiter reference value (Ldref).  Typical Value = 1. Default: 0.0
    :maxerr: Maximum value for speed error signal (maxerr).  Typical Value = 0.05. Default: 0.0
    :minerr: Minimum value for speed error signal (minerr).  Typical Value = -0.05. Default: 0.0
    :mwbase: Base for power values (MWbase) (> 0).  Unit = MW. Default: 0.0
    :r: Permanent droop (R).  Typical Value = 0.04. Default: 0.0
    :rclose: Minimum valve closing rate (Rclose).  Unit = PU/sec.  Typical Value = -0.1. Default: 0.0
    :rdown: Maximum rate of load limit decrease (Rdown).  Typical Value = -99. Default: 0.0
    :ropen: Maximum valve opening rate (Ropen).  Unit = PU/sec.  Typical Value = 0.10. Default: 0.0
    :rselect: Feedback signal for droop (Rselect).  Typical Value = electricalPower. Default: None
    :rup: Maximum rate of load limit increase (Rup).  Typical Value = 99. Default: 0.0
    :ta: Acceleration limiter time constant (Ta) (>0).  Typical Value = 0.1. Default: 0.0
    :tact: Actuator time constant (Tact).  Typical Value = 0.5. Default: 0.0
    :tb: Turbine lag time constant (Tb) (>0).  Typical Value = 0.5. Default: 0.0
    :tc: Turbine lead time constant (Tc).  Typical Value = 0. Default: 0.0
    :tdgov: Governor derivative controller time constant (Tdgov).  Typical Value = 1. Default: 0.0
    :teng: Transport time delay for diesel engine used in representing diesel engines where there is a small but measurable transport delay between a change in fuel flow setting and the development of torque (Teng).  Teng should be zero in all but special cases where this transport delay is of particular concern.  Typical Value = 0. Default: 0.0
    :tfload: Load Limiter time constant (Tfload) (>0).  Typical Value = 3. Default: 0.0
    :tpelec: Electrical power transducer time constant (Tpelec) (>0).  Typical Value = 1. Default: 0.0
    :tsa: Temperature detection lead time constant (Tsa).  Typical Value = 4. Default: 0.0
    :tsb: Temperature detection lag time constant (Tsb).  Typical Value = 5. Default: 0.0
    :vmax: Maximum valve position limit (Vmax).  Typical Value = 1. Default: 0.0
    :vmin: Minimum valve position limit (Vmin).  Typical Value = 0.15. Default: 0.0
    :wfnl: No load fuel flow (Wfnl).  Typical Value = 0.2. Default: 0.0
    :wfspd: Switch for fuel source characteristic to recognize that fuel flow, for a given fuel valve stroke, can be proportional to engine speed (Wfspd). true = fuel flow proportional to speed (for some gas turbines and diesel engines with positive displacement fuel injectors) false = fuel control system keeps fuel flow independent of engine speed. Typical Value = true. Default: False
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "aset": [Profile.DY.value, ],
        "db": [Profile.DY.value, ],
        "dm": [Profile.DY.value, ],
        "ka": [Profile.DY.value, ],
        "kdgov": [Profile.DY.value, ],
        "kigov": [Profile.DY.value, ],
        "kiload": [Profile.DY.value, ],
        "kimw": [Profile.DY.value, ],
        "kpgov": [Profile.DY.value, ],
        "kpload": [Profile.DY.value, ],
        "kturb": [Profile.DY.value, ],
        "ldref": [Profile.DY.value, ],
        "maxerr": [Profile.DY.value, ],
        "minerr": [Profile.DY.value, ],
        "mwbase": [Profile.DY.value, ],
        "r": [Profile.DY.value, ],
        "rclose": [Profile.DY.value, ],
        "rdown": [Profile.DY.value, ],
        "ropen": [Profile.DY.value, ],
        "rselect": [Profile.DY.value, ],
        "rup": [Profile.DY.value, ],
        "ta": [Profile.DY.value, ],
        "tact": [Profile.DY.value, ],
        "tb": [Profile.DY.value, ],
        "tc": [Profile.DY.value, ],
        "tdgov": [Profile.DY.value, ],
        "teng": [Profile.DY.value, ],
        "tfload": [Profile.DY.value, ],
        "tpelec": [Profile.DY.value, ],
        "tsa": [Profile.DY.value, ],
        "tsb": [Profile.DY.value, ],
        "vmax": [Profile.DY.value, ],
        "vmin": [Profile.DY.value, ],
        "wfnl": [Profile.DY.value, ],
        "wfspd": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class TurbineGovernorDynamics:\n" + TurbineGovernorDynamics.__doc__

    def __init__(self, aset = 0.0, db = 0.0, dm = 0.0, ka = 0.0, kdgov = 0.0, kigov = 0.0, kiload = 0.0, kimw = 0.0, kpgov = 0.0, kpload = 0.0, kturb = 0.0, ldref = 0.0, maxerr = 0.0, minerr = 0.0, mwbase = 0.0, r = 0.0, rclose = 0.0, rdown = 0.0, ropen = 0.0, rselect = None, rup = 0.0, ta = 0.0, tact = 0.0, tb = 0.0, tc = 0.0, tdgov = 0.0, teng = 0.0, tfload = 0.0, tpelec = 0.0, tsa = 0.0, tsb = 0.0, vmax = 0.0, vmin = 0.0, wfnl = 0.0, wfspd = False, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.aset = aset
        self.db = db
        self.dm = dm
        self.ka = ka
        self.kdgov = kdgov
        self.kigov = kigov
        self.kiload = kiload
        self.kimw = kimw
        self.kpgov = kpgov
        self.kpload = kpload
        self.kturb = kturb
        self.ldref = ldref
        self.maxerr = maxerr
        self.minerr = minerr
        self.mwbase = mwbase
        self.r = r
        self.rclose = rclose
        self.rdown = rdown
        self.ropen = ropen
        self.rselect = rselect
        self.rup = rup
        self.ta = ta
        self.tact = tact
        self.tb = tb
        self.tc = tc
        self.tdgov = tdgov
        self.teng = teng
        self.tfload = tfload
        self.tpelec = tpelec
        self.tsa = tsa
        self.tsb = tsb
        self.vmax = vmax
        self.vmin = vmin
        self.wfnl = wfnl
        self.wfspd = wfspd

    def __str__(self):
        str = "class=GovCT1\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
