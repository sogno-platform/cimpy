from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcAVR4(ExcitationSystemDynamics):
    """
    Italian excitation system. It represents static exciter and electric voltage regulator.

    :imul: AVR output voltage dependency selector (Imul). true = selector is connected false = selector is not connected. Typical Value = true. Default: False
    :ka: AVR gain (K).  Typical Value = 300. Default: 0.0
    :ke: Exciter gain (K).  Typical Value = 1. Default: 0.0
    :kif: Exciter internal reactance (K).  Typical Value = 0. Default: 0.0
    :t1: AVR time constant (T).  Typical Value = 4.8. Default: 0.0
    :t1if: Exciter current feedback time constant (T).  Typical Value = 60. Default: 0.0
    :t2: AVR time constant (T).  Typical Value = 1.5. Default: 0.0
    :t3: AVR time constant (T).  Typical Value = 0. Default: 0.0
    :t4: AVR time constant (T).  Typical Value = 0. Default: 0.0
    :tif: Exciter current feedback time constant (T).  Typical Value = 0. Default: 0.0
    :vfmn: Minimum exciter output (V).  Typical Value = 0. Default: 0.0
    :vfmx: Maximum exciter output (V).  Typical Value = 5. Default: 0.0
    :vrmn: Maximum AVR output (V).  Typical Value = 0. Default: 0.0
    :vrmx: Minimum AVR output (V).  Typical Value = 5. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "imul": [Profile.DY.value, ],
        "ka": [Profile.DY.value, ],
        "ke": [Profile.DY.value, ],
        "kif": [Profile.DY.value, ],
        "t1": [Profile.DY.value, ],
        "t1if": [Profile.DY.value, ],
        "t2": [Profile.DY.value, ],
        "t3": [Profile.DY.value, ],
        "t4": [Profile.DY.value, ],
        "tif": [Profile.DY.value, ],
        "vfmn": [Profile.DY.value, ],
        "vfmx": [Profile.DY.value, ],
        "vrmn": [Profile.DY.value, ],
        "vrmx": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, imul = False, ka = 0.0, ke = 0.0, kif = 0.0, t1 = 0.0, t1if = 0.0, t2 = 0.0, t3 = 0.0, t4 = 0.0, tif = 0.0, vfmn = 0.0, vfmx = 0.0, vrmn = 0.0, vrmx = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.imul = imul
        self.ka = ka
        self.ke = ke
        self.kif = kif
        self.t1 = t1
        self.t1if = t1if
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.tif = tif
        self.vfmn = vfmn
        self.vfmx = vfmx
        self.vrmn = vrmn
        self.vrmx = vrmx

    def __str__(self):
        str = "class=ExcAVR4\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
