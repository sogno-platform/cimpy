from .TurbineGovernorDynamics import TurbineGovernorDynamics
from .CGMESProfile import Profile


class GovGASTWD(TurbineGovernorDynamics):
    """
    Woodward Gas turbine governor model.

    :a: Valve positioner (). Default: 0.0
    :af1: Exhaust temperature Parameter (Af1). Default: 0.0
    :af2: Coefficient equal to 0.5(1-speed) (Af2). Default: 0.0
    :b: Valve positioner (). Default: 0.0
    :bf1: (Bf1).  Bf1 = E(1-w) where E (speed sensitivity coefficient) is 0.55 to 0.65 x Tr. Default: 0.0
    :bf2: Turbine Torque Coefficient K (depends on heating value of fuel stream in combustion chamber) (Bf2). Default: 0.0
    :c: Valve positioner (). Default: 0.0
    :cf2: Coefficient defining fuel flow where power output is 0% (Cf2).  Synchronous but no output.  Typically 0.23 x K(23% fuel flow). Default: 0.0
    :ecr: Combustion reaction time delay (Ecr). Default: 0.0
    :etd: Turbine and exhaust delay (Etd). Default: 0.0
    :k3: Ratio of Fuel Adjustment (K3). Default: 0.0
    :k4: Gain of radiation shield (K4). Default: 0.0
    :k5: Gain of radiation shield (K5). Default: 0.0
    :k6: Minimum fuel flow (K6). Default: 0.0
    :kd: Drop Governor Gain (Kd). Default: 0.0
    :kdroop: (Kdroop). Default: 0.0
    :kf: Fuel system feedback (Kf). Default: 0.0
    :ki: Isochronous Governor Gain (Ki). Default: 0.0
    :kp: PID Proportional gain (Kp). Default: 0.0
    :mwbase: Base for power values (MWbase) (> 0).  Unit = MW. Default: 0.0
    :t: Fuel Control Time Constant (T). Default: 0.0
    :t3: Radiation shield time constant (T3). Default: 0.0
    :t4: Thermocouple time constant (T4). Default: 0.0
    :t5: Temperature control time constant (T5). Default: 0.0
    :tc: Temperature control (Tc). Default: 0.0
    :tcd: Compressor discharge time constant (Tcd). Default: 0.0
    :td: Power transducer time constant (Td). Default: 0.0
    :tf: Fuel system time constant (Tf). Default: 0.0
    :tmax: Maximum Turbine limit (Tmax). Default: 0.0
    :tmin: Minimum Turbine limit (Tmin). Default: 0.0
    :tr: Rated temperature (Tr). Default: 0.0
    :trate: Turbine rating (Trate).  Unit = MW. Default: 0.0
    :tt: Temperature controller integration rate (Tt). Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "a": [Profile.DY.value, ],
        "af1": [Profile.DY.value, ],
        "af2": [Profile.DY.value, ],
        "b": [Profile.DY.value, ],
        "bf1": [Profile.DY.value, ],
        "bf2": [Profile.DY.value, ],
        "c": [Profile.DY.value, ],
        "cf2": [Profile.DY.value, ],
        "ecr": [Profile.DY.value, ],
        "etd": [Profile.DY.value, ],
        "k3": [Profile.DY.value, ],
        "k4": [Profile.DY.value, ],
        "k5": [Profile.DY.value, ],
        "k6": [Profile.DY.value, ],
        "kd": [Profile.DY.value, ],
        "kdroop": [Profile.DY.value, ],
        "kf": [Profile.DY.value, ],
        "ki": [Profile.DY.value, ],
        "kp": [Profile.DY.value, ],
        "mwbase": [Profile.DY.value, ],
        "t": [Profile.DY.value, ],
        "t3": [Profile.DY.value, ],
        "t4": [Profile.DY.value, ],
        "t5": [Profile.DY.value, ],
        "tc": [Profile.DY.value, ],
        "tcd": [Profile.DY.value, ],
        "td": [Profile.DY.value, ],
        "tf": [Profile.DY.value, ],
        "tmax": [Profile.DY.value, ],
        "tmin": [Profile.DY.value, ],
        "tr": [Profile.DY.value, ],
        "trate": [Profile.DY.value, ],
        "tt": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class TurbineGovernorDynamics:\n" + TurbineGovernorDynamics.__doc__

    def __init__(self, a = 0.0, af1 = 0.0, af2 = 0.0, b = 0.0, bf1 = 0.0, bf2 = 0.0, c = 0.0, cf2 = 0.0, ecr = 0.0, etd = 0.0, k3 = 0.0, k4 = 0.0, k5 = 0.0, k6 = 0.0, kd = 0.0, kdroop = 0.0, kf = 0.0, ki = 0.0, kp = 0.0, mwbase = 0.0, t = 0.0, t3 = 0.0, t4 = 0.0, t5 = 0.0, tc = 0.0, tcd = 0.0, td = 0.0, tf = 0.0, tmax = 0.0, tmin = 0.0, tr = 0.0, trate = 0.0, tt = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.a = a
        self.af1 = af1
        self.af2 = af2
        self.b = b
        self.bf1 = bf1
        self.bf2 = bf2
        self.c = c
        self.cf2 = cf2
        self.ecr = ecr
        self.etd = etd
        self.k3 = k3
        self.k4 = k4
        self.k5 = k5
        self.k6 = k6
        self.kd = kd
        self.kdroop = kdroop
        self.kf = kf
        self.ki = ki
        self.kp = kp
        self.mwbase = mwbase
        self.t = t
        self.t3 = t3
        self.t4 = t4
        self.t5 = t5
        self.tc = tc
        self.tcd = tcd
        self.td = td
        self.tf = tf
        self.tmax = tmax
        self.tmin = tmin
        self.tr = tr
        self.trate = trate
        self.tt = tt

    def __str__(self):
        str = "class=GovGASTWD\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
