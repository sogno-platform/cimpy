from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcBBC(ExcitationSystemDynamics):
    """
    Transformer fed static excitation system (static with ABB regulator). This model represents a static excitation system in which a gated thyristor bridge fed by a transformer at the main generator terminals feeds the main generator directly.

    :efdmax: Maximum open circuit exciter voltage (Efdmax).  Typical Value = 5. Default: 0.0
    :efdmin: Minimum open circuit exciter voltage (Efdmin).  Typical Value = -5. Default: 0.0
    :k: Steady state gain (K).  Typical Value = 300. Default: 0.0
    :switch: Supplementary signal routing selector (switch). true = Vs connected to 3rd summing point false =  Vs connected to 1st summing point (see diagram). Typical Value = true. Default: False
    :t1: Controller time constant (T1).  Typical Value = 6. Default: 0.0
    :t2: Controller time constant (T2).  Typical Value = 1. Default: 0.0
    :t3: Lead/lag time constant (T3).  Typical Value = 0.05. Default: 0.0
    :t4: Lead/lag time constant (T4).  Typical Value = 0.01. Default: 0.0
    :vrmax: Maximum control element output (Vrmax).  Typical Value = 5. Default: 0.0
    :vrmin: Minimum control element output (Vrmin).  Typical Value = -5. Default: 0.0
    :xe: Effective excitation transformer reactance (Xe).  Typical Value = 0.05. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "efdmax": [Profile.DY.value, ],
        "efdmin": [Profile.DY.value, ],
        "k": [Profile.DY.value, ],
        "switch": [Profile.DY.value, ],
        "t1": [Profile.DY.value, ],
        "t2": [Profile.DY.value, ],
        "t3": [Profile.DY.value, ],
        "t4": [Profile.DY.value, ],
        "vrmax": [Profile.DY.value, ],
        "vrmin": [Profile.DY.value, ],
        "xe": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, efdmax = 0.0, efdmin = 0.0, k = 0.0, switch = False, t1 = 0.0, t2 = 0.0, t3 = 0.0, t4 = 0.0, vrmax = 0.0, vrmin = 0.0, xe = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.efdmax = efdmax
        self.efdmin = efdmin
        self.k = k
        self.switch = switch
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.xe = xe

    def __str__(self):
        str = "class=ExcBBC\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
