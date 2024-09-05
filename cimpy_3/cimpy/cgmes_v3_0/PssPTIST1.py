from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class PssPTIST1(PowerSystemStabilizerDynamics):
    """
    PTI microprocessor-based stabilizer type 1.

    :m: (<i>M</i>).  <i>M </i>= 2 x <i>H</i>.  Typical value = 5. Default: 0.0
    :tf: Time constant (<i>Tf</i>) (&gt;= 0).  Typical value = 0,2. Default: 0
    :tp: Time constant (<i>Tp</i>) (&gt;= 0).  Typical value = 0,2. Default: 0
    :t1: Time constant (<i>T1</i>) (&gt;= 0).  Typical value = 0,3. Default: 0
    :t2: Time constant (<i>T2</i>) (&gt;= 0).  Typical value = 1. Default: 0
    :t3: Time constant (<i>T3</i>) (&gt;= 0).  Typical value = 0,2. Default: 0
    :t4: Time constant (<i>T4</i>) (&gt;= 0).  Typical value = 0,05. Default: 0
    :k: Gain (<i>K</i>).  Typical value = 9. Default: 0.0
    :dtf: Time step frequency calculation (<i>deltatf</i>) (&gt;= 0).  Typical value = 0,025. Default: 0
    :dtc: Time step related to activation of controls (<i>deltatc</i>) (&gt;= 0).  Typical value = 0,025. Default: 0
    :dtp: Time step active power calculation (<i>deltatp</i>) (&gt;= 0).  Typical value = 0,0125. Default: 0
    """

    cgmesProfile = PowerSystemStabilizerDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "m": [
            cgmesProfile.DY.value,
        ],
        "tf": [
            cgmesProfile.DY.value,
        ],
        "tp": [
            cgmesProfile.DY.value,
        ],
        "t1": [
            cgmesProfile.DY.value,
        ],
        "t2": [
            cgmesProfile.DY.value,
        ],
        "t3": [
            cgmesProfile.DY.value,
        ],
        "t4": [
            cgmesProfile.DY.value,
        ],
        "k": [
            cgmesProfile.DY.value,
        ],
        "dtf": [
            cgmesProfile.DY.value,
        ],
        "dtc": [
            cgmesProfile.DY.value,
        ],
        "dtp": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class PowerSystemStabilizerDynamics: \n"
        + PowerSystemStabilizerDynamics.__doc__
    )

    def __init__(
        self,
        m=0.0,
        tf=0,
        tp=0,
        t1=0,
        t2=0,
        t3=0,
        t4=0,
        k=0.0,
        dtf=0,
        dtc=0,
        dtp=0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.m = m
        self.tf = tf
        self.tp = tp
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.k = k
        self.dtf = dtf
        self.dtc = dtc
        self.dtp = dtp

    def __str__(self):
        str = "class=PssPTIST1\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
