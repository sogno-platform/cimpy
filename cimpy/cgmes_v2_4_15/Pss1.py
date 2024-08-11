from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics
from .CGMESProfile import Profile


class Pss1(PowerSystemStabilizerDynamics):
    """
    Italian PSS - three input PSS (speed, frequency, power).

    :kf: Frequency power input gain (K).  Typical Value = 5. Default: 0.0
    :kpe: Electric power input gain (K).  Typical Value = 0.3. Default: 0.0
    :ks: PSS gain (K).  Typical Value = 1. Default: 0.0
    :kw: Shaft speed power input gain (K).  Typical Value = 0. Default: 0.0
    :pmin: Minimum power PSS enabling (P).  Typical Value = 0.25. Default: 0.0
    :t10: Lead/lag time constant (T).  Typical Value = 0. Default: 0.0
    :t5: Washout (T).  Typical Value = 3.5. Default: 0.0
    :t6: Filter time constant (T).  Typical Value = 0. Default: 0.0
    :t7: Lead/lag time constant (T).  Typical Value = 0. Default: 0.0
    :t8: Lead/lag time constant (T).  Typical Value = 0. Default: 0.0
    :t9: Lead/lag time constant (T).  Typical Value = 0. Default: 0.0
    :tpe: Electric power filter time constant (T).  Typical Value = 0.05. Default: 0.0
    :vadat:  Default: False
    :vsmn: Stabilizer output max limit (V).  Typical Value = -0.06. Default: 0.0
    :vsmx: Stabilizer output min limit (V).  Typical Value = 0.06. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "kf": [Profile.DY.value, ],
        "kpe": [Profile.DY.value, ],
        "ks": [Profile.DY.value, ],
        "kw": [Profile.DY.value, ],
        "pmin": [Profile.DY.value, ],
        "t10": [Profile.DY.value, ],
        "t5": [Profile.DY.value, ],
        "t6": [Profile.DY.value, ],
        "t7": [Profile.DY.value, ],
        "t8": [Profile.DY.value, ],
        "t9": [Profile.DY.value, ],
        "tpe": [Profile.DY.value, ],
        "vadat": [Profile.DY.value, ],
        "vsmn": [Profile.DY.value, ],
        "vsmx": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class PowerSystemStabilizerDynamics:\n" + PowerSystemStabilizerDynamics.__doc__

    def __init__(self, kf = 0.0, kpe = 0.0, ks = 0.0, kw = 0.0, pmin = 0.0, t10 = 0.0, t5 = 0.0, t6 = 0.0, t7 = 0.0, t8 = 0.0, t9 = 0.0, tpe = 0.0, vadat = False, vsmn = 0.0, vsmx = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.kf = kf
        self.kpe = kpe
        self.ks = ks
        self.kw = kw
        self.pmin = pmin
        self.t10 = t10
        self.t5 = t5
        self.t6 = t6
        self.t7 = t7
        self.t8 = t8
        self.t9 = t9
        self.tpe = tpe
        self.vadat = vadat
        self.vsmn = vsmn
        self.vsmx = vsmx

    def __str__(self):
        str = "class=Pss1\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
