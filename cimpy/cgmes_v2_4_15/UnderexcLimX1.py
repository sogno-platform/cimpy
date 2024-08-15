from .UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics
from .CGMESProfile import Profile


class UnderexcLimX1(UnderexcitationLimiterDynamics):
    """
    

    :k: Minimum excitation limit slope (K) (>0). Default: 0.0
    :kf2: Differential gain (Kf2). Default: 0.0
    :km: Minimum excitation limit gain (Km). Default: 0.0
    :melmax: Minimum excitation limit value (MELMAX). Default: 0.0
    :tf2: Differential time constant (Tf2) (>0). Default: 0.0
    :tm: Minimum excitation limit time constant (Tm). Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "k": [Profile.DY.value, ],
        "kf2": [Profile.DY.value, ],
        "km": [Profile.DY.value, ],
        "melmax": [Profile.DY.value, ],
        "tf2": [Profile.DY.value, ],
        "tm": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class UnderexcitationLimiterDynamics:\n" + UnderexcitationLimiterDynamics.__doc__

    def __init__(self, k = 0.0, kf2 = 0.0, km = 0.0, melmax = 0.0, tf2 = 0.0, tm = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.k = k
        self.kf2 = kf2
        self.km = km
        self.melmax = melmax
        self.tf2 = tf2
        self.tm = tm

    def __str__(self):
        str = "class=UnderexcLimX1\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
