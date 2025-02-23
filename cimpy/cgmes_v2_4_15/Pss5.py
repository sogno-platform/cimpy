from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics
from .CGMESProfile import Profile


class Pss5(PowerSystemStabilizerDynamics):
    """
    Italian PSS - Detailed PSS.

    :ctw2: Selector for Second washout enabling (C). true = second washout filter is bypassed false = second washout filter in use. Typical Value = true. Default: False
    :deadband: Stabilizer output dead band (DeadBand).  Typical Value = 0. Default: 0.0
    :isfreq: Selector for Frequency/shaft speed input (IsFreq). true = speed false = frequency. Typical Value = true. Default: False
    :kf: Frequency/shaft speed input gain (K).  Typical Value = 5. Default: 0.0
    :kpe: Electric power input gain (K).  Typical Value = 0.3. Default: 0.0
    :kpss: PSS gain (K).  Typical Value = 1. Default: 0.0
    :pmm: Minimum power PSS enabling (P).  Typical Value = 0.25. Default: 0.0
    :tl1: Lead/lag time constant (T).  Typical Value = 0. Default: 0.0
    :tl2: Lead/lag time constant (T).  Typical Value = 0. Default: 0.0
    :tl3: Lead/lag time constant (T).  Typical Value = 0. Default: 0.0
    :tl4: Lead/lag time constant (T).  Typical Value = 0. Default: 0.0
    :tpe: Electric power filter time constant (T).  Typical Value = 0.05. Default: 0.0
    :tw1: First WashOut (T).  Typical Value = 3.5. Default: 0.0
    :tw2: Second WashOut (T).  Typical Value = 0. Default: 0.0
    :vadat:  Default: False
    :vsmn: Stabilizer output max limit (V).  Typical Value = -0.1. Default: 0.0
    :vsmx: Stabilizer output min limit (V).  Typical Value = 0.1. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "ctw2": [Profile.DY.value, ],
        "deadband": [Profile.DY.value, ],
        "isfreq": [Profile.DY.value, ],
        "kf": [Profile.DY.value, ],
        "kpe": [Profile.DY.value, ],
        "kpss": [Profile.DY.value, ],
        "pmm": [Profile.DY.value, ],
        "tl1": [Profile.DY.value, ],
        "tl2": [Profile.DY.value, ],
        "tl3": [Profile.DY.value, ],
        "tl4": [Profile.DY.value, ],
        "tpe": [Profile.DY.value, ],
        "tw1": [Profile.DY.value, ],
        "tw2": [Profile.DY.value, ],
        "vadat": [Profile.DY.value, ],
        "vsmn": [Profile.DY.value, ],
        "vsmx": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class PowerSystemStabilizerDynamics:\n" + PowerSystemStabilizerDynamics.__doc__

    def __init__(self, ctw2 = False, deadband = 0.0, isfreq = False, kf = 0.0, kpe = 0.0, kpss = 0.0, pmm = 0.0, tl1 = 0.0, tl2 = 0.0, tl3 = 0.0, tl4 = 0.0, tpe = 0.0, tw1 = 0.0, tw2 = 0.0, vadat = False, vsmn = 0.0, vsmx = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ctw2 = ctw2
        self.deadband = deadband
        self.isfreq = isfreq
        self.kf = kf
        self.kpe = kpe
        self.kpss = kpss
        self.pmm = pmm
        self.tl1 = tl1
        self.tl2 = tl2
        self.tl3 = tl3
        self.tl4 = tl4
        self.tpe = tpe
        self.tw1 = tw1
        self.tw2 = tw2
        self.vadat = vadat
        self.vsmn = vsmn
        self.vsmx = vsmx

    def __str__(self):
        str = "class=Pss5\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
