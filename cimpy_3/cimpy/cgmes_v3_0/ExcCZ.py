from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcCZ(ExcitationSystemDynamics):
    """
    Czech proportion/integral exciter.

    :kp: Regulator proportional gain (<i>Kp</i>). Default: 0.0
    :tc: Regulator integral time constant (<i>Tc</i>) (&gt;= 0). Default: 0
    :vrmax: Voltage regulator maximum limit (<i>Vrmax</i>) (&gt; ExcCZ.vrmin). Default: 0.0
    :vrmin: Voltage regulator minimum limit (<i>Vrmin</i>) (&lt; ExcCZ.vrmax). Default: 0.0
    :ka: Regulator gain (<i>Ka</i>). Default: 0.0
    :ta: Regulator time constant (<i>Ta</i>) (&gt;= 0). Default: 0
    :ke: Exciter constant related to self-excited field (<i>Ke</i>). Default: 0.0
    :te: Exciter time constant, integration rate associated with exciter control (<i>Te</i>) (&gt;= 0). Default: 0
    :efdmax: Exciter output maximum limit (<i>Efdmax</i>) (&gt; ExcCZ.efdmin). Default: 0.0
    :efdmin: Exciter output minimum limit (<i>Efdmin</i>) (&lt; ExcCZ.efdmax). Default: 0.0
    """

    cgmesProfile = ExcitationSystemDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "kp": [
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
        "ka": [
            cgmesProfile.DY.value,
        ],
        "ta": [
            cgmesProfile.DY.value,
        ],
        "ke": [
            cgmesProfile.DY.value,
        ],
        "te": [
            cgmesProfile.DY.value,
        ],
        "efdmax": [
            cgmesProfile.DY.value,
        ],
        "efdmin": [
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
        kp=0.0,
        tc=0,
        vrmax=0.0,
        vrmin=0.0,
        ka=0.0,
        ta=0,
        ke=0.0,
        te=0,
        efdmax=0.0,
        efdmin=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.kp = kp
        self.tc = tc
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.ka = ka
        self.ta = ta
        self.ke = ke
        self.te = te
        self.efdmax = efdmax
        self.efdmin = efdmin

    def __str__(self):
        str = "class=ExcCZ\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
