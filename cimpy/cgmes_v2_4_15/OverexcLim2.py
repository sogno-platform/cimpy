from .OverexcitationLimiterDynamics import OverexcitationLimiterDynamics
from .CGMESProfile import Profile


class OverexcLim2(OverexcitationLimiterDynamics):
    """
    Different from LimIEEEOEL, LimOEL2 has a fixed pickup threshold and reduces the excitation set-point by mean of non-windup integral regulator. Irated is the rated machine excitation current (calculated from nameplate conditions: V, P, CosPhi).

    :ifdlim: Limit value of rated field current (I).  Typical Value = 1.05. Default: 0.0
    :koi: Gain Over excitation limiter (K).  Typical Value = 0.1. Default: 0.0
    :voimax: Maximum error signal (V).  Typical Value = 0. Default: 0.0
    :voimin: Minimum error signal (V).  Typical Value = -9999. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "ifdlim": [Profile.DY.value, ],
        "koi": [Profile.DY.value, ],
        "voimax": [Profile.DY.value, ],
        "voimin": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class OverexcitationLimiterDynamics:\n" + OverexcitationLimiterDynamics.__doc__

    def __init__(self, ifdlim = 0.0, koi = 0.0, voimax = 0.0, voimin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ifdlim = ifdlim
        self.koi = koi
        self.voimax = voimax
        self.voimin = voimin

    def __str__(self):
        str = "class=OverexcLim2\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
