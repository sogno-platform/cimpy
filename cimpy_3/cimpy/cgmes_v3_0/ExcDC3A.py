from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcDC3A(ExcitationSystemDynamics):
    """
    Modified IEEE DC3A direct current commutator exciter with speed input, and deadband.  DC old type 4.

    :trh: Rheostat travel time (<i>Trh</i>) (&gt; 0).  Typical value = 20. Default: 0
    :ks: Coefficient to allow different usage of the model-speed coefficient (<i>Ks</i>).  Typical value = 0. Default: 0.0
    :kr: Deadband (<i>Kr</i>).  Typical value = 0. Default: 0.0
    :kv: Fast raise/lower contact setting (<i>Kv</i>) (&gt; 0).  Typical value = 0,05. Default: 0.0
    :vrmax: Maximum voltage regulator output (<i>Vrmax</i>) (&gt; 0).  Typical value = 5. Default: 0.0
    :vrmin: Minimum voltage regulator output (<i>Vrmin</i>) (&lt;= 0).  Typical value = 0. Default: 0.0
    :te: Exciter time constant, integration rate associated with exciter control (<i>Te</i>) (&gt; 0).  Typical value = 1,83. Default: 0
    :ke: Exciter constant related to self-excited field (<i>Ke</i>).  Typical value = 1. Default: 0.0
    :efd1: Exciter voltage at which exciter saturation is defined (<i>Efd</i><i><sub>1</sub></i>) (&gt; 0).  Typical value = 2,6. Default: 0.0
    :seefd1: Exciter saturation function value at the corresponding exciter voltage, <i>Efd</i><i><sub>1</sub></i> (<i>Se[Efd</i><i><sub>1</sub></i><i>]</i>) (&gt;= 0).  Typical value = 0,1. Default: 0.0
    :efd2: Exciter voltage at which exciter saturation is defined (<i>Efd</i><i><sub>2</sub></i>) (&gt; 0).  Typical value = 3,45. Default: 0.0
    :seefd2: Exciter saturation function value at the corresponding exciter voltage, <i>Efd</i><i><sub>2</sub></i> (<i>Se[Efd</i><i><sub>2</sub></i><i>]</i>) (&gt;= 0).  Typical value = 0,35. Default: 0.0
    :exclim: (<i>exclim</i>).  IEEE standard is ambiguous about lower limit on exciter output. true = a lower limit of zero is applied to integrator output false = a lower limit of zero not applied to integrator output. Typical value = true. Default: False
    :efdmax: Maximum voltage exciter output limiter (<i>Efdmax</i>) (&gt; ExcDC3A.efdmin).  Typical value = 99. Default: 0.0
    :efdmin: Minimum voltage exciter output limiter (<i>Efdmin</i>) (&lt; ExcDC3A.efdmax).  Typical value = -99. Default: 0.0
    :efdlim: (<i>Efdlim</i>). true = exciter output limiter is active false = exciter output limiter not active. Typical value = true. Default: False
    """

    cgmesProfile = ExcitationSystemDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "trh": [
            cgmesProfile.DY.value,
        ],
        "ks": [
            cgmesProfile.DY.value,
        ],
        "kr": [
            cgmesProfile.DY.value,
        ],
        "kv": [
            cgmesProfile.DY.value,
        ],
        "vrmax": [
            cgmesProfile.DY.value,
        ],
        "vrmin": [
            cgmesProfile.DY.value,
        ],
        "te": [
            cgmesProfile.DY.value,
        ],
        "ke": [
            cgmesProfile.DY.value,
        ],
        "efd1": [
            cgmesProfile.DY.value,
        ],
        "seefd1": [
            cgmesProfile.DY.value,
        ],
        "efd2": [
            cgmesProfile.DY.value,
        ],
        "seefd2": [
            cgmesProfile.DY.value,
        ],
        "exclim": [
            cgmesProfile.DY.value,
        ],
        "efdmax": [
            cgmesProfile.DY.value,
        ],
        "efdmin": [
            cgmesProfile.DY.value,
        ],
        "efdlim": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class ExcitationSystemDynamics: \n"
        + ExcitationSystemDynamics.__doc__
    )

    def __init__(
        self,
        trh=0,
        ks=0.0,
        kr=0.0,
        kv=0.0,
        vrmax=0.0,
        vrmin=0.0,
        te=0,
        ke=0.0,
        efd1=0.0,
        seefd1=0.0,
        efd2=0.0,
        seefd2=0.0,
        exclim=False,
        efdmax=0.0,
        efdmin=0.0,
        efdlim=False,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.trh = trh
        self.ks = ks
        self.kr = kr
        self.kv = kv
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.te = te
        self.ke = ke
        self.efd1 = efd1
        self.seefd1 = seefd1
        self.efd2 = efd2
        self.seefd2 = seefd2
        self.exclim = exclim
        self.efdmax = efdmax
        self.efdmin = efdmin
        self.efdlim = efdlim

    def __str__(self):
        str = "class=ExcDC3A\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
