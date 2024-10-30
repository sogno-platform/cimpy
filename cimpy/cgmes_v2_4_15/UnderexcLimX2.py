from .UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics
from .CGMESProfile import Profile


class UnderexcLimX2(UnderexcitationLimiterDynamics):
    """
    

    :kf2: Differential gain (Kf2). Default: 0.0
    :km: Minimum excitation limit gain (Km). Default: 0.0
    :melmax: Minimum excitation limit value (MELMAX). Default: 0.0
    :qo: Excitation center setting (Qo). Default: 0.0
    :r: Excitation radius (R). Default: 0.0
    :tf2: Differential time constant (Tf2) (>0). Default: 0.0
    :tm: Minimum excitation limit time constant (Tm). Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "kf2": [Profile.DY.value, ],
        "km": [Profile.DY.value, ],
        "melmax": [Profile.DY.value, ],
        "qo": [Profile.DY.value, ],
        "r": [Profile.DY.value, ],
        "tf2": [Profile.DY.value, ],
        "tm": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class UnderexcitationLimiterDynamics:\n" + UnderexcitationLimiterDynamics.__doc__

    def __init__(self, kf2 = 0.0, km = 0.0, melmax = 0.0, qo = 0.0, r = 0.0, tf2 = 0.0, tm = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.kf2 = kf2
        self.km = km
        self.melmax = melmax
        self.qo = qo
        self.r = r
        self.tf2 = tf2
        self.tm = tm

    def __str__(self):
        str = "class=UnderexcLimX2\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
