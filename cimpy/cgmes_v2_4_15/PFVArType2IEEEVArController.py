from .PFVArControllerType2Dynamics import PFVArControllerType2Dynamics
from .CGMESProfile import Profile


class PFVArType2IEEEVArController(PFVArControllerType2Dynamics):
    """
    The class represents IEEE VAR Controller Type 2 which is a summing point type controller. It makes up the outside loop of a two-loop system. This controller is implemented as a slow PI type controller, and the voltage regulator forms the inner loop and is implemented as a fast controller.  Reference: IEEE Standard 421.5-2005 Section 11.5.

    :exlon: Overexcitation or under excitation flag () true = 1 (not in the overexcitation or underexcitation state, integral action is active) false = 0 (in the overexcitation or underexcitation state, so integral action is disabled to allow the limiter to play its role). Default: False
    :ki: Integral gain of the pf controller (). Default: 0.0
    :kp: Proportional gain of the pf controller (). Default: 0.0
    :qref: Reactive power reference (). Default: 0.0
    :vclmt: Maximum output of the pf controller (). Default: 0.0
    :vref: Voltage regulator reference (). Default: 0.0
    :vs: Generator sensing voltage (). Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "exlon": [Profile.DY.value, ],
        "ki": [Profile.DY.value, ],
        "kp": [Profile.DY.value, ],
        "qref": [Profile.DY.value, ],
        "vclmt": [Profile.DY.value, ],
        "vref": [Profile.DY.value, ],
        "vs": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class PFVArControllerType2Dynamics:\n" + PFVArControllerType2Dynamics.__doc__

    def __init__(self, exlon = False, ki = 0.0, kp = 0.0, qref = 0.0, vclmt = 0.0, vref = 0.0, vs = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.exlon = exlon
        self.ki = ki
        self.kp = kp
        self.qref = qref
        self.vclmt = vclmt
        self.vref = vref
        self.vs = vs

    def __str__(self):
        str = "class=PFVArType2IEEEVArController\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
