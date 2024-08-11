from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class LoadStatic(IdentifiedObject):
    """
    General static load model representing the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage.

    :LoadAggregate: Aggregate load to which this aggregate static load belongs. Default: None
    :ep1: First term voltage exponent for active power (Ep1).  Used only when .staticLoadModelType = exponential. Default: 0.0
    :ep2: Second term voltage exponent for active power (Ep2).  Used only when .staticLoadModelType = exponential. Default: 0.0
    :ep3: Third term voltage exponent for active power (Ep3).  Used only when .staticLoadModelType = exponential. Default: 0.0
    :eq1: First term voltage exponent for reactive power (Eq1).  Used only when .staticLoadModelType = exponential. Default: 0.0
    :eq2: Second term voltage exponent for reactive power (Eq2).  Used only when .staticLoadModelType = exponential. Default: 0.0
    :eq3: Third term voltage exponent for reactive power (Eq3).  Used only when .staticLoadModelType = exponential. Default: 0.0
    :kp1: First term voltage coefficient for active power (Kp1).  Not used when .staticLoadModelType = constantZ. Default: 0.0
    :kp2: Second term voltage coefficient for active power (Kp2).  Not used when .staticLoadModelType = constantZ. Default: 0.0
    :kp3: Third term voltage coefficient for active power (Kp3).  Not used when .staticLoadModelType = constantZ. Default: 0.0
    :kp4: Frequency coefficient for active power (Kp4).  Must be non-zero when .staticLoadModelType = ZIP2.  Not used for all other values of .staticLoadModelType. Default: 0.0
    :kpf: Frequency deviation coefficient for active power (Kpf).  Not used when .staticLoadModelType = constantZ. Default: 0.0
    :kq1: First term voltage coefficient for reactive power (Kq1).  Not used when .staticLoadModelType = constantZ. Default: 0.0
    :kq2: Second term voltage coefficient for reactive power (Kq2).  Not used when .staticLoadModelType = constantZ. Default: 0.0
    :kq3: Third term voltage coefficient for reactive power (Kq3).  Not used when .staticLoadModelType = constantZ. Default: 0.0
    :kq4: Frequency coefficient for reactive power (Kq4).  Must be non-zero when .staticLoadModelType = ZIP2.  Not used for all other values of .staticLoadModelType. Default: 0.0
    :kqf: Frequency deviation coefficient for reactive power (Kqf).  Not used when .staticLoadModelType = constantZ. Default: 0.0
    :staticLoadModelType: Type of static load model.  Typical Value = constantZ. Default: None
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "LoadAggregate": [Profile.DY.value, ],
        "ep1": [Profile.DY.value, ],
        "ep2": [Profile.DY.value, ],
        "ep3": [Profile.DY.value, ],
        "eq1": [Profile.DY.value, ],
        "eq2": [Profile.DY.value, ],
        "eq3": [Profile.DY.value, ],
        "kp1": [Profile.DY.value, ],
        "kp2": [Profile.DY.value, ],
        "kp3": [Profile.DY.value, ],
        "kp4": [Profile.DY.value, ],
        "kpf": [Profile.DY.value, ],
        "kq1": [Profile.DY.value, ],
        "kq2": [Profile.DY.value, ],
        "kq3": [Profile.DY.value, ],
        "kq4": [Profile.DY.value, ],
        "kqf": [Profile.DY.value, ],
        "staticLoadModelType": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, LoadAggregate = None, ep1 = 0.0, ep2 = 0.0, ep3 = 0.0, eq1 = 0.0, eq2 = 0.0, eq3 = 0.0, kp1 = 0.0, kp2 = 0.0, kp3 = 0.0, kp4 = 0.0, kpf = 0.0, kq1 = 0.0, kq2 = 0.0, kq3 = 0.0, kq4 = 0.0, kqf = 0.0, staticLoadModelType = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.LoadAggregate = LoadAggregate
        self.ep1 = ep1
        self.ep2 = ep2
        self.ep3 = ep3
        self.eq1 = eq1
        self.eq2 = eq2
        self.eq3 = eq3
        self.kp1 = kp1
        self.kp2 = kp2
        self.kp3 = kp3
        self.kp4 = kp4
        self.kpf = kpf
        self.kq1 = kq1
        self.kq2 = kq2
        self.kq3 = kq3
        self.kq4 = kq4
        self.kqf = kqf
        self.staticLoadModelType = staticLoadModelType

    def __str__(self):
        str = "class=LoadStatic\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
