from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAC4A(ExcitationSystemDynamics):
    """
    Modified IEEE AC4A alternator-supplied rectifier excitation system with different minimum controller output.

    :vimax: Maximum voltage regulator input limit (<i>Vimax</i>)  (&gt; 0).  Typical value = 10. Default: 0.0
    :vimin: Minimum voltage regulator input limit (<i>Vimin</i>) (&lt; 0).  Typical value = -10. Default: 0.0
    :tc: Voltage regulator time constant (<i>Tc</i>) (&gt;= 0).  Typical value = 1. Default: 0
    :tb: Voltage regulator time constant (<i>Tb</i>) (&gt;= 0).  Typical value = 10. Default: 0
    :ka: Voltage regulator gain (<i>Ka</i>) (&gt; 0).  Typical value = 200. Default: 0.0
    :ta: Voltage regulator time constant (<i>Ta</i>) (&gt; 0).  Typical value = 0,015. Default: 0
    :vrmax: Maximum voltage regulator output (<i>Vrmax</i>) (&gt; 0).  Typical value = 5,64. Default: 0.0
    :vrmin: Minimum voltage regulator output (<i>Vrmin</i>) (&lt; 0).  Typical value = -4,53. Default: 0.0
    :kc: Rectifier loading factor proportional to commutating reactance (<i>Kc</i>) (&gt;= 0).  Typical value = 0. Default: 0.0
    """

    cgmesProfile = ExcitationSystemDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "vimax": [
            cgmesProfile.DY.value,
        ],
        "vimin": [
            cgmesProfile.DY.value,
        ],
        "tc": [
            cgmesProfile.DY.value,
        ],
        "tb": [
            cgmesProfile.DY.value,
        ],
        "ka": [
            cgmesProfile.DY.value,
        ],
        "ta": [
            cgmesProfile.DY.value,
        ],
        "vrmax": [
            cgmesProfile.DY.value,
        ],
        "vrmin": [
            cgmesProfile.DY.value,
        ],
        "kc": [
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
        vimax=0.0,
        vimin=0.0,
        tc=0,
        tb=0,
        ka=0.0,
        ta=0,
        vrmax=0.0,
        vrmin=0.0,
        kc=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.vimax = vimax
        self.vimin = vimin
        self.tc = tc
        self.tb = tb
        self.ka = ka
        self.ta = ta
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.kc = kc

    def __str__(self):
        str = "class=ExcAC4A\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
