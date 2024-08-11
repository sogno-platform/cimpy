from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcAVR1(ExcitationSystemDynamics):
    """
    Italian excitation system corresponding to IEEE (1968) Type 1 Model. It represents exciter dynamo and electromechanical regulator.

    :e1: Field voltage value 1  (E1).  Typical Value = 4.18. Default: 0.0
    :e2: Field voltage value 2 (E2).  Typical Value = 3.14. Default: 0.0
    :ka: AVR gain (K).  Typical Value = 500. Default: 0.0
    :kf: Rate feedback gain (K).  Typical Value = 0.02. Default: 0.0
    :se1: Saturation factor at E1 (S(E1)).  Typical Value = 0.1. Default: 0.0
    :se2: Saturation factor at E2 (S(E2)).  Typical Value = 0.03. Default: 0.0
    :ta: AVR time constant (T).  Typical Value = 0.2. Default: 0.0
    :tb: AVR time constant (T).  Typical Value = 0. Default: 0.0
    :te: Exciter time constant (T).  Typical Value = 1. Default: 0.0
    :tf: Rate feedback time constant (T).  Typical Value = 1. Default: 0.0
    :vrmn: Maximum AVR output (V).  Typical Value = -6. Default: 0.0
    :vrmx: Minimum AVR output (V).  Typical Value = 7. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "e1": [Profile.DY.value, ],
        "e2": [Profile.DY.value, ],
        "ka": [Profile.DY.value, ],
        "kf": [Profile.DY.value, ],
        "se1": [Profile.DY.value, ],
        "se2": [Profile.DY.value, ],
        "ta": [Profile.DY.value, ],
        "tb": [Profile.DY.value, ],
        "te": [Profile.DY.value, ],
        "tf": [Profile.DY.value, ],
        "vrmn": [Profile.DY.value, ],
        "vrmx": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, e1 = 0.0, e2 = 0.0, ka = 0.0, kf = 0.0, se1 = 0.0, se2 = 0.0, ta = 0.0, tb = 0.0, te = 0.0, tf = 0.0, vrmn = 0.0, vrmx = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.e1 = e1
        self.e2 = e2
        self.ka = ka
        self.kf = kf
        self.se1 = se1
        self.se2 = se2
        self.ta = ta
        self.tb = tb
        self.te = te
        self.tf = tf
        self.vrmn = vrmn
        self.vrmx = vrmx

    def __str__(self):
        str = "class=ExcAVR1\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
