from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcCZ(ExcitationSystemDynamics):
    """
    Czech Proportion/Integral Exciter.

    :efdmax: Exciter output maximum limit (Efdmax). Default: 0.0
    :efdmin: Exciter output minimum limit (Efdmin). Default: 0.0
    :ka: Regulator gain (Ka). Default: 0.0
    :ke: Exciter constant related to self-excited field (Ke). Default: 0.0
    :kp: Regulator proportional gain (Kp). Default: 0.0
    :ta: Regulator time constant (Ta). Default: 0.0
    :tc: Regulator integral time constant (Tc). Default: 0.0
    :te: Exciter time constant, integration rate associated with exciter control (Te). Default: 0.0
    :vrmax: Voltage regulator maximum limit (Vrmax). Default: 0.0
    :vrmin: Voltage regulator minimum limit (Vrmin). Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "efdmax": [Profile.DY.value, ],
        "efdmin": [Profile.DY.value, ],
        "ka": [Profile.DY.value, ],
        "ke": [Profile.DY.value, ],
        "kp": [Profile.DY.value, ],
        "ta": [Profile.DY.value, ],
        "tc": [Profile.DY.value, ],
        "te": [Profile.DY.value, ],
        "vrmax": [Profile.DY.value, ],
        "vrmin": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, efdmax = 0.0, efdmin = 0.0, ka = 0.0, ke = 0.0, kp = 0.0, ta = 0.0, tc = 0.0, te = 0.0, vrmax = 0.0, vrmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.efdmax = efdmax
        self.efdmin = efdmin
        self.ka = ka
        self.ke = ke
        self.kp = kp
        self.ta = ta
        self.tc = tc
        self.te = te
        self.vrmax = vrmax
        self.vrmin = vrmin

    def __str__(self):
        str = "class=ExcCZ\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
