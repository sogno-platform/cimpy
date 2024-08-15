from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcAVR7(ExcitationSystemDynamics):
    """
    IVO excitation system.

    :a1: Lead coefficient (A1).  Typical Value = 0.5. Default: 0.0
    :a2: Lag coefficient (A2).  Typical Value = 0.5. Default: 0.0
    :a3: Lead coefficient (A3).  Typical Value = 0.5. Default: 0.0
    :a4: Lag coefficient (A4).  Typical Value = 0.5. Default: 0.0
    :a5: Lead coefficient (A5).  Typical Value = 0.5. Default: 0.0
    :a6: Lag coefficient (A6).  Typical Value = 0.5. Default: 0.0
    :k1: Gain (K1).  Typical Value = 1. Default: 0.0
    :k3: Gain (K3).  Typical Value = 3. Default: 0.0
    :k5: Gain (K5).  Typical Value = 1. Default: 0.0
    :t1: Lead time constant (T1).  Typical Value = 0.05. Default: 0.0
    :t2: Lag time constant (T2).  Typical Value = 0.1. Default: 0.0
    :t3: Lead time constant (T3).  Typical Value = 0.1. Default: 0.0
    :t4: Lag time constant (T4).  Typical Value = 0.1. Default: 0.0
    :t5: Lead time constant (T5).  Typical Value = 0.1. Default: 0.0
    :t6: Lag time constant (T6).  Typical Value = 0.1. Default: 0.0
    :vmax1: Lead-lag max. limit (Vmax1).  Typical Value = 5. Default: 0.0
    :vmax3: Lead-lag max. limit (Vmax3).  Typical Value = 5. Default: 0.0
    :vmax5: Lead-lag max. limit (Vmax5).  Typical Value = 5. Default: 0.0
    :vmin1: Lead-lag min. limit (Vmin1).  Typical Value = -5. Default: 0.0
    :vmin3: Lead-lag min. limit (Vmin3).  Typical Value = -5. Default: 0.0
    :vmin5: Lead-lag min. limit (Vmin5).  Typical Value = -2. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "a1": [Profile.DY.value, ],
        "a2": [Profile.DY.value, ],
        "a3": [Profile.DY.value, ],
        "a4": [Profile.DY.value, ],
        "a5": [Profile.DY.value, ],
        "a6": [Profile.DY.value, ],
        "k1": [Profile.DY.value, ],
        "k3": [Profile.DY.value, ],
        "k5": [Profile.DY.value, ],
        "t1": [Profile.DY.value, ],
        "t2": [Profile.DY.value, ],
        "t3": [Profile.DY.value, ],
        "t4": [Profile.DY.value, ],
        "t5": [Profile.DY.value, ],
        "t6": [Profile.DY.value, ],
        "vmax1": [Profile.DY.value, ],
        "vmax3": [Profile.DY.value, ],
        "vmax5": [Profile.DY.value, ],
        "vmin1": [Profile.DY.value, ],
        "vmin3": [Profile.DY.value, ],
        "vmin5": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, a1 = 0.0, a2 = 0.0, a3 = 0.0, a4 = 0.0, a5 = 0.0, a6 = 0.0, k1 = 0.0, k3 = 0.0, k5 = 0.0, t1 = 0.0, t2 = 0.0, t3 = 0.0, t4 = 0.0, t5 = 0.0, t6 = 0.0, vmax1 = 0.0, vmax3 = 0.0, vmax5 = 0.0, vmin1 = 0.0, vmin3 = 0.0, vmin5 = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.a6 = a6
        self.k1 = k1
        self.k3 = k3
        self.k5 = k5
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t5 = t5
        self.t6 = t6
        self.vmax1 = vmax1
        self.vmax3 = vmax3
        self.vmax5 = vmax5
        self.vmin1 = vmin1
        self.vmin3 = vmin3
        self.vmin5 = vmin5

    def __str__(self):
        str = "class=ExcAVR7\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
