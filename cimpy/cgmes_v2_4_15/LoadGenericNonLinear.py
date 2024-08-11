from .LoadDynamics import LoadDynamics
from .CGMESProfile import Profile


class LoadGenericNonLinear(LoadDynamics):
    """
    These load models (known also as generic non-linear dynamic (GNLD) load models) can be used in mid-term and long-term voltage stability simulations (i.e., to study voltage collapse), as they can replace a more detailed representation of aggregate load, including induction motors, thermostatically controlled and static loads.

    :bs: Steady state voltage index for reactive power (BS). Default: 0.0
    :bt: Transient voltage index for reactive power (BT). Default: 0.0
    :genericNonLinearLoadModelType: Type of generic non-linear load model. Default: None
    :ls: Steady state voltage index for active power (LS). Default: 0.0
    :lt: Transient voltage index for active power (LT). Default: 0.0
    :pt: Dynamic portion of active load (P). Default: 0.0
    :qt: Dynamic portion of reactive load (Q). Default: 0.0
    :tp: Time constant of lag function of active power (T). Default: 0.0
    :tq: Time constant of lag function of reactive power (T). Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "bs": [Profile.DY.value, ],
        "bt": [Profile.DY.value, ],
        "genericNonLinearLoadModelType": [Profile.DY.value, ],
        "ls": [Profile.DY.value, ],
        "lt": [Profile.DY.value, ],
        "pt": [Profile.DY.value, ],
        "qt": [Profile.DY.value, ],
        "tp": [Profile.DY.value, ],
        "tq": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class LoadDynamics:\n" + LoadDynamics.__doc__

    def __init__(self, bs = 0.0, bt = 0.0, genericNonLinearLoadModelType = None, ls = 0.0, lt = 0.0, pt = 0.0, qt = 0.0, tp = 0.0, tq = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.bs = bs
        self.bt = bt
        self.genericNonLinearLoadModelType = genericNonLinearLoadModelType
        self.ls = ls
        self.lt = lt
        self.pt = pt
        self.qt = qt
        self.tp = tp
        self.tq = tq

    def __str__(self):
        str = "class=LoadGenericNonLinear\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
