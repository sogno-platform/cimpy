from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class PssSH(PowerSystemStabilizerDynamics):
    """
    Siemens<sup>TM</sup> "H infinity" power system stabilizer with generator electrical power input. [Footnote: Siemens "H infinity" power system stabilizers are an example of suitable products available commercially. This information is given for the convenience of users of this document and does not constitute an endorsement by IEC of these products.]

    :k: Main gain (<i>K</i>).  Typical value = 1. Default: 0.0
    :k0: Gain 0 (<i>K0</i>).  Typical value = 0,012. Default: 0.0
    :k1: Gain 1 (<i>K1</i>).  Typical value = 0,488. Default: 0.0
    :k2: Gain 2 (<i>K2</i>).  Typical value = 0,064. Default: 0.0
    :k3: Gain 3 (<i>K3</i>).  Typical value = 0,224. Default: 0.0
    :k4: Gain 4 (<i>K4</i>).  Typical value = 0,1. Default: 0.0
    :td: Input time constant (<i>T</i><i><sub>d</sub></i>) (&gt;= 0).  Typical value = 10. Default: 0
    :t1: Time constant 1 (<i>T1</i>) (&gt; 0).  Typical value = 0,076. Default: 0
    :t2: Time constant 2 (<i>T2</i>) (&gt; 0).  Typical value = 0,086. Default: 0
    :t3: Time constant 3 (<i>T3</i>) (&gt; 0).   Typical value = 1,068. Default: 0
    :t4: Time constant 4 (<i>T4</i>) (&gt; 0).  Typical value = 1,913. Default: 0
    :vsmax: Output maximum limit (<i>Vsmax</i>) (&gt; PssSH.vsmin).  Typical value = 0,1. Default: 0.0
    :vsmin: Output minimum limit (<i>Vsmin</i>) (&lt; PssSH.vsmax).  Typical value = -0,1. Default: 0.0
    """

    cgmesProfile = PowerSystemStabilizerDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "k": [
            cgmesProfile.DY.value,
        ],
        "k0": [
            cgmesProfile.DY.value,
        ],
        "k1": [
            cgmesProfile.DY.value,
        ],
        "k2": [
            cgmesProfile.DY.value,
        ],
        "k3": [
            cgmesProfile.DY.value,
        ],
        "k4": [
            cgmesProfile.DY.value,
        ],
        "td": [
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
        "vsmax": [
            cgmesProfile.DY.value,
        ],
        "vsmin": [
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
        k=0.0,
        k0=0.0,
        k1=0.0,
        k2=0.0,
        k3=0.0,
        k4=0.0,
        td=0,
        t1=0,
        t2=0,
        t3=0,
        t4=0,
        vsmax=0.0,
        vsmin=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.k = k
        self.k0 = k0
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.k4 = k4
        self.td = td
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.vsmax = vsmax
        self.vsmin = vsmin

    def __str__(self):
        str = "class=PssSH\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
