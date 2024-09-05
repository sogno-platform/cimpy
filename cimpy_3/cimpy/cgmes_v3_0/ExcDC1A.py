from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcDC1A(ExcitationSystemDynamics):
    """
    Modified IEEE DC1A direct current commutator exciter with speed input and without underexcitation limiters (UEL) inputs.

    :ka: Voltage regulator gain (<i>Ka</i>) (&gt; 0).  Typical value = 46. Default: 0.0
    :ks: Coefficient to allow different usage of the model-speed coefficient (<i>Ks</i>).  Typical value = 0. Default: 0.0
    :ta: Voltage regulator time constant (<i>Ta</i>) (&gt; 0).  Typical value = 0,06. Default: 0
    :tb: Voltage regulator time constant (<i>Tb</i>) (&gt;= 0).  Typical value = 0. Default: 0
    :tc: Voltage regulator time constant (<i>Tc</i>) (&gt;= 0).  Typical value = 0. Default: 0
    :vrmax: Maximum voltage regulator output (<i>Vrmax</i>) (&gt; ExcDC1A.vrmin).  Typical value = 1. Default: 0.0
    :vrmin: Minimum voltage regulator output (<i>Vrmin</i>) (&lt; 0 and &lt; ExcDC1A.vrmax).  Typical value = -0,9. Default: 0.0
    :ke: Exciter constant related to self-excited field (<i>Ke</i>).  Typical value = 0. Default: 0.0
    :te: Exciter time constant, integration rate associated with exciter control (<i>Te</i>) (&gt; 0).  Typical value = 0,46. Default: 0
    :kf: Excitation control system stabilizer gain (<i>Kf</i>) (&gt;= 0).  Typical value = 0,1. Default: 0.0
    :tf: Excitation control system stabilizer time constant (<i>Tf</i>) (&gt; 0).  Typical value = 1. Default: 0
    :efd1: Exciter voltage at which exciter saturation is defined (<i>Efd</i><i><sub>1</sub></i>) (&gt; 0).  Typical value = 3,1. Default: 0.0
    :seefd1: Exciter saturation function value at the corresponding exciter voltage, <i>Efd</i><i><sub>1</sub></i> (<i>Se[Eefd</i><i><sub>1</sub></i><i>]</i>) (&gt;= 0).  Typical value = 0,33. Default: 0.0
    :efd2: Exciter voltage at which exciter saturation is defined (<i>Efd</i><i><sub>2</sub></i>) (&gt; 0).  Typical value = 2,3. Default: 0.0
    :seefd2: Exciter saturation function value at the corresponding exciter voltage, <i>Efd</i><i><sub>2</sub></i> (<i>Se[Eefd</i><i><sub>2</sub></i><i>]</i>) (&gt;= 0).  Typical value = 0,1. Default: 0.0
    :exclim: (<i>exclim</i>).  IEEE standard is ambiguous about lower limit on exciter output.  true = a lower limit of zero is applied to integrator output false = a lower limit of zero is not applied to integrator output. Typical value = true. Default: False
    :efdmin: Minimum voltage exciter output limiter (<i>Efdmin</i>) (&lt; ExcDC1A.edfmax).  Typical value = -99. Default: 0.0
    :efdmax: Maximum voltage exciter output limiter (<i>Efdmax</i>) (&gt; ExcDC1A.efdmin).  Typical value = 99. Default: 0.0
    """

    cgmesProfile = ExcitationSystemDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "ka": [
            cgmesProfile.DY.value,
        ],
        "ks": [
            cgmesProfile.DY.value,
        ],
        "ta": [
            cgmesProfile.DY.value,
        ],
        "tb": [
            cgmesProfile.DY.value,
        ],
        "tc": [
            cgmesProfile.DY.value,
        ],
        "vrmax": [
            cgmesProfile.DY.value,
        ],
        "vrmin": [
            cgmesProfile.DY.value,
        ],
        "ke": [
            cgmesProfile.DY.value,
        ],
        "te": [
            cgmesProfile.DY.value,
        ],
        "kf": [
            cgmesProfile.DY.value,
        ],
        "tf": [
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
        "efdmin": [
            cgmesProfile.DY.value,
        ],
        "efdmax": [
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
        ka=0.0,
        ks=0.0,
        ta=0,
        tb=0,
        tc=0,
        vrmax=0.0,
        vrmin=0.0,
        ke=0.0,
        te=0,
        kf=0.0,
        tf=0,
        efd1=0.0,
        seefd1=0.0,
        efd2=0.0,
        seefd2=0.0,
        exclim=False,
        efdmin=0.0,
        efdmax=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.ka = ka
        self.ks = ks
        self.ta = ta
        self.tb = tb
        self.tc = tc
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.ke = ke
        self.te = te
        self.kf = kf
        self.tf = tf
        self.efd1 = efd1
        self.seefd1 = seefd1
        self.efd2 = efd2
        self.seefd2 = seefd2
        self.exclim = exclim
        self.efdmin = efdmin
        self.efdmax = efdmax

    def __str__(self):
        str = "class=ExcDC1A\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
