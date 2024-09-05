from .IdentifiedObject import IdentifiedObject


class LoadStatic(IdentifiedObject):
    """
    General static load. This model represents the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage.

    :LoadAggregate: Aggregate load to which this aggregate static load belongs. Default: None
    :staticLoadModelType: Type of static load model.  Typical value = constantZ. Default: None
    :kp1: First term voltage coefficient for active power (<i>K</i><i><sub>p1</sub></i>).  Not used when .staticLoadModelType = constantZ. Default: 0.0
    :kp2: Second term voltage coefficient for active power (<i>K</i><i><sub>p2</sub></i>).  Not used when .staticLoadModelType = constantZ. Default: 0.0
    :kp3: Third term voltage coefficient for active power (<i>K</i><i><sub>p3</sub></i>).  Not used when .staticLoadModelType = constantZ. Default: 0.0
    :kp4: Frequency coefficient for active power (<i>K</i><i><sub>p4</sub></i>)  (not = 0 if .staticLoadModelType = zIP2).  Used only when .staticLoadModelType = zIP2. Default: 0.0
    :ep1: First term voltage exponent for active power (<i>Ep1</i>).  Used only when .staticLoadModelType = exponential. Default: 0.0
    :ep2: Second term voltage exponent for active power (<i>Ep2</i>).  Used only when .staticLoadModelType = exponential. Default: 0.0
    :ep3: Third term voltage exponent for active power (<i>Ep3</i>).  Used only when .staticLoadModelType = exponential. Default: 0.0
    :kpf: Frequency deviation coefficient for active power (<i>K</i><i><sub>pf</sub></i>).  Not used when .staticLoadModelType = constantZ. Default: 0.0
    :kq1: First term voltage coefficient for reactive power (<i>K</i><i><sub>q1</sub></i>).  Not used when .staticLoadModelType = constantZ. Default: 0.0
    :kq2: Second term voltage coefficient for reactive power (<i>K</i><i><sub>q2</sub></i>).  Not used when .staticLoadModelType = constantZ. Default: 0.0
    :kq3: Third term voltage coefficient for reactive power (<i>K</i><i><sub>q3</sub></i>).  Not used when .staticLoadModelType = constantZ. Default: 0.0
    :kq4: Frequency coefficient for reactive power (<i>K</i><i><sub>q4</sub></i>)  (not = 0 when .staticLoadModelType = zIP2).  Used only when .staticLoadModelType - zIP2. Default: 0.0
    :eq1: First term voltage exponent for reactive power (<i>Eq1</i>).  Used only when .staticLoadModelType = exponential. Default: 0.0
    :eq2: Second term voltage exponent for reactive power (<i>Eq2</i>).  Used only when .staticLoadModelType = exponential. Default: 0.0
    :eq3: Third term voltage exponent for reactive power (<i>Eq3</i>).  Used only when .staticLoadModelType = exponential. Default: 0.0
    :kqf: Frequency deviation coefficient for reactive power (<i>K</i><i><sub>qf</sub></i>).  Not used when .staticLoadModelType = constantZ. Default: 0.0
    """

    cgmesProfile = IdentifiedObject.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "LoadAggregate": [
            cgmesProfile.DY.value,
        ],
        "staticLoadModelType": [
            cgmesProfile.DY.value,
        ],
        "kp1": [
            cgmesProfile.DY.value,
        ],
        "kp2": [
            cgmesProfile.DY.value,
        ],
        "kp3": [
            cgmesProfile.DY.value,
        ],
        "kp4": [
            cgmesProfile.DY.value,
        ],
        "ep1": [
            cgmesProfile.DY.value,
        ],
        "ep2": [
            cgmesProfile.DY.value,
        ],
        "ep3": [
            cgmesProfile.DY.value,
        ],
        "kpf": [
            cgmesProfile.DY.value,
        ],
        "kq1": [
            cgmesProfile.DY.value,
        ],
        "kq2": [
            cgmesProfile.DY.value,
        ],
        "kq3": [
            cgmesProfile.DY.value,
        ],
        "kq4": [
            cgmesProfile.DY.value,
        ],
        "eq1": [
            cgmesProfile.DY.value,
        ],
        "eq2": [
            cgmesProfile.DY.value,
        ],
        "eq3": [
            cgmesProfile.DY.value,
        ],
        "kqf": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class IdentifiedObject: \n"
        + IdentifiedObject.__doc__
    )

    def __init__(
        self,
        LoadAggregate=None,
        staticLoadModelType=None,
        kp1=0.0,
        kp2=0.0,
        kp3=0.0,
        kp4=0.0,
        ep1=0.0,
        ep2=0.0,
        ep3=0.0,
        kpf=0.0,
        kq1=0.0,
        kq2=0.0,
        kq3=0.0,
        kq4=0.0,
        eq1=0.0,
        eq2=0.0,
        eq3=0.0,
        kqf=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.LoadAggregate = LoadAggregate
        self.staticLoadModelType = staticLoadModelType
        self.kp1 = kp1
        self.kp2 = kp2
        self.kp3 = kp3
        self.kp4 = kp4
        self.ep1 = ep1
        self.ep2 = ep2
        self.ep3 = ep3
        self.kpf = kpf
        self.kq1 = kq1
        self.kq2 = kq2
        self.kq3 = kq3
        self.kq4 = kq4
        self.eq1 = eq1
        self.eq2 = eq2
        self.eq3 = eq3
        self.kqf = kqf

    def __str__(self):
        str = "class=LoadStatic\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
