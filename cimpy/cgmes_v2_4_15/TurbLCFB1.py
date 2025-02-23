from .TurbineLoadControllerDynamics import TurbineLoadControllerDynamics
from .CGMESProfile import Profile


class TurbLCFB1(TurbineLoadControllerDynamics):
    """
    Turbine Load Controller model developed in the WECC.  This model represents a supervisory turbine load controller that acts to maintain turbine power at a set value by continuous adjustment of the turbine governor speed-load reference. This model is intended to represent slow reset 'outer loop' controllers managing the action of the turbine governor.

    :db: Controller dead band (db).  Typical Value = 0. Default: 0.0
    :emax: Maximum control error (Emax) (note 4).  Typical Value = 0.02. Default: 0.0
    :fb: Frequency bias gain (Fb).  Typical Value = 0. Default: 0.0
    :fbf: Frequency bias flag (Fbf). true = enable frequency bias false = disable frequency bias. Typical Value = false. Default: False
    :irmax: Maximum turbine speed/load reference bias (Irmax) (note 3).  Typical Value = 0. Default: 0.0
    :ki: Integral gain (Ki).  Typical Value = 0. Default: 0.0
    :kp: Proportional gain (Kp).  Typical Value = 0. Default: 0.0
    :mwbase: Base for power values (MWbase) (>0).  Unit = MW. Default: 0.0
    :pbf: Power controller flag (Pbf). true = enable load controller false = disable load controller. Typical Value = false. Default: False
    :pmwset: Power controller setpoint (Pmwset) (note 1).  Unit = MW. Typical Value = 0. Default: 0.0
    :speedReferenceGovernor: Type of turbine governor reference (Type). true = speed reference governor false = load reference governor. Typical Value = true. Default: False
    :tpelec: Power transducer time constant (Tpelec).  Typical Value = 0. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "db": [Profile.DY.value, ],
        "emax": [Profile.DY.value, ],
        "fb": [Profile.DY.value, ],
        "fbf": [Profile.DY.value, ],
        "irmax": [Profile.DY.value, ],
        "ki": [Profile.DY.value, ],
        "kp": [Profile.DY.value, ],
        "mwbase": [Profile.DY.value, ],
        "pbf": [Profile.DY.value, ],
        "pmwset": [Profile.DY.value, ],
        "speedReferenceGovernor": [Profile.DY.value, ],
        "tpelec": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class TurbineLoadControllerDynamics:\n" + TurbineLoadControllerDynamics.__doc__

    def __init__(self, db = 0.0, emax = 0.0, fb = 0.0, fbf = False, irmax = 0.0, ki = 0.0, kp = 0.0, mwbase = 0.0, pbf = False, pmwset = 0.0, speedReferenceGovernor = False, tpelec = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.db = db
        self.emax = emax
        self.fb = fb
        self.fbf = fbf
        self.irmax = irmax
        self.ki = ki
        self.kp = kp
        self.mwbase = mwbase
        self.pbf = pbf
        self.pmwset = pmwset
        self.speedReferenceGovernor = speedReferenceGovernor
        self.tpelec = tpelec

    def __str__(self):
        str = "class=TurbLCFB1\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
