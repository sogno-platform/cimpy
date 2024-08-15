from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcAVR3(ExcitationSystemDynamics):
    """
    Italian excitation system. It represents exciter dynamo and electric regulator.

    :e1: Field voltage value 1 (E1).  Typical Value = 4.18. Default: 0.0
    :e2: Field voltage value 2 (E2).  Typical Value = 3.14. Default: 0.0
    :ka: AVR gain (K).  Typical Value = 3000. Default: 0.0
    :se1: Saturation factor at E1 (S(E1)).  Typical Value = 0.1. Default: 0.0
    :se2: Saturation factor at E2 (S(E2)).  Typical Value = 0.03. Default: 0.0
    :t1: AVR time constant (T).  Typical Value = 220. Default: 0.0
    :t2: AVR time constant (T).  Typical Value = 1.6. Default: 0.0
    :t3: AVR time constant (T).  Typical Value = 0.66. Default: 0.0
    :t4: AVR time constant (T).  Typical Value = 0.07. Default: 0.0
    :te: Exciter time constant (T).  Typical Value = 1. Default: 0.0
    :vrmn: Maximum AVR output (V).  Typical Value = -7.5. Default: 0.0
    :vrmx: Minimum AVR output (V).  Typical Value = 7.5. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "e1": [Profile.DY.value, ],
        "e2": [Profile.DY.value, ],
        "ka": [Profile.DY.value, ],
        "se1": [Profile.DY.value, ],
        "se2": [Profile.DY.value, ],
        "t1": [Profile.DY.value, ],
        "t2": [Profile.DY.value, ],
        "t3": [Profile.DY.value, ],
        "t4": [Profile.DY.value, ],
        "te": [Profile.DY.value, ],
        "vrmn": [Profile.DY.value, ],
        "vrmx": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, e1 = 0.0, e2 = 0.0, ka = 0.0, se1 = 0.0, se2 = 0.0, t1 = 0.0, t2 = 0.0, t3 = 0.0, t4 = 0.0, te = 0.0, vrmn = 0.0, vrmx = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.e1 = e1
        self.e2 = e2
        self.ka = ka
        self.se1 = se1
        self.se2 = se2
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.te = te
        self.vrmn = vrmn
        self.vrmx = vrmx

    def __str__(self):
        str = "class=ExcAVR3\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
