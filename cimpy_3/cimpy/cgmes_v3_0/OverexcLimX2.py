from .OverexcitationLimiterDynamics import OverexcitationLimiterDynamics


class OverexcLimX2(OverexcitationLimiterDynamics):
    """
    Field voltage or current overexcitation limiter designed to protect the generator field of an AC machine with automatic excitation control from overheating due to prolonged overexcitation.

    :m: (<i>m</i>). true = IFD limiting false = EFD limiting. Default: False
    :efdrated: Rated field voltage if m = false or rated field current if m = true (<i>EFD</i><i><sub>RATED</sub></i>).  Typical value = 1,05. Default: 0.0
    :efd1: Low voltage or current point on the inverse time characteristic (<i>EFD</i><i><sub>1</sub></i>).  Typical value = 1,1. Default: 0.0
    :t1: Time to trip the exciter at the low voltage or current point on the inverse time characteristic (<i>TIME</i><i><sub>1</sub></i>) (&gt;= 0).  Typical value = 120. Default: 0
    :efd2: Mid voltage or current point on the inverse time characteristic (<i>EFD</i><i><sub>2</sub></i>).  Typical value = 1,2. Default: 0.0
    :t2: Time to trip the exciter at the mid voltage or current point on the inverse time characteristic (<i>TIME</i><i><sub>2</sub></i>) (&gt;= 0).  Typical value = 40. Default: 0
    :efd3: High voltage or current point on the inverse time characteristic (<i>EFD</i><i><sub>3</sub></i>).  Typical value = 1,5. Default: 0.0
    :t3: Time to trip the exciter at the high voltage or current point on the inverse time characteristic (<i>TIME</i><i><sub>3</sub></i>) (&gt;= 0).  Typical value = 15. Default: 0
    :efddes: Desired field voltage if <i>m</i> = false or desired field current if <i>m </i>= true (<i>EFD</i><i><sub>DES</sub></i>).  Typical value = 1. Default: 0.0
    :kmx: Gain (<i>K</i><i><sub>MX</sub></i>).  Typical value = 0,002. Default: 0.0
    :vlow: Low voltage limit (<i>V</i><i><sub>LOW</sub></i>) (&gt; 0). Default: 0.0
    """

    cgmesProfile = OverexcitationLimiterDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "m": [
            cgmesProfile.DY.value,
        ],
        "efdrated": [
            cgmesProfile.DY.value,
        ],
        "efd1": [
            cgmesProfile.DY.value,
        ],
        "t1": [
            cgmesProfile.DY.value,
        ],
        "efd2": [
            cgmesProfile.DY.value,
        ],
        "t2": [
            cgmesProfile.DY.value,
        ],
        "efd3": [
            cgmesProfile.DY.value,
        ],
        "t3": [
            cgmesProfile.DY.value,
        ],
        "efddes": [
            cgmesProfile.DY.value,
        ],
        "kmx": [
            cgmesProfile.DY.value,
        ],
        "vlow": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class OverexcitationLimiterDynamics: \n"
        + OverexcitationLimiterDynamics.__doc__
    )

    def __init__(
        self,
        m=False,
        efdrated=0.0,
        efd1=0.0,
        t1=0,
        efd2=0.0,
        t2=0,
        efd3=0.0,
        t3=0,
        efddes=0.0,
        kmx=0.0,
        vlow=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.m = m
        self.efdrated = efdrated
        self.efd1 = efd1
        self.t1 = t1
        self.efd2 = efd2
        self.t2 = t2
        self.efd3 = efd3
        self.t3 = t3
        self.efddes = efddes
        self.kmx = kmx
        self.vlow = vlow

    def __str__(self):
        str = "class=OverexcLimX2\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
