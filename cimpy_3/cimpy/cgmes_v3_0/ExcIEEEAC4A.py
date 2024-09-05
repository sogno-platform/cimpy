from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEAC4A(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type AC4A model. The model represents type AC4A alternator-supplied controlled-rectifier excitation system which is quite different from the other types of AC systems. This high initial response excitation system utilizes a full thyristor bridge in the exciter output circuit.  The voltage regulator controls the firing of the thyristor bridges. The exciter alternator uses an independent voltage regulator to control its output voltage to a constant value. These effects are not modelled; however, transient loading effects on the exciter alternator are included. Reference: IEEE 421.5-2005, 6.4.

    :vimax: Maximum voltage regulator input limit (<i>V</i><i><sub>IMAX</sub></i>) (&gt; 0).  Typical value = 10. Default: 0.0
    :vimin: Minimum voltage regulator input limit (<i>V</i><i><sub>IMIN</sub></i>) (&lt; 0).  Typical value = -10. Default: 0.0
    :tc: Voltage regulator time constant (<i>T</i><i><sub>C</sub></i>) (&gt;= 0).  Typical value = 1. Default: 0
    :tb: Voltage regulator time constant (<i>T</i><i><sub>B</sub></i>) (&gt;= 0).  Typical value = 10. Default: 0
    :ka: Voltage regulator gain (<i>K</i><i><sub>A</sub></i>) (&gt; 0).  Typical value = 200. Default: 0.0
    :ta: Voltage regulator time constant (<i>T</i><i><sub>A</sub></i>) (&gt; 0).  Typical value = 0,015. Default: 0
    :vrmax: Maximum voltage regulator output (<i>V</i><i><sub>RMAX</sub></i>) (&gt; 0).  Typical value = 5,64. Default: 0.0
    :vrmin: Minimum voltage regulator output (<i>V</i><i><sub>RMIN</sub></i>) (&lt; 0).  Typical value = -4,53. Default: 0.0
    :kc: Rectifier loading factor proportional to commutating reactance (<i>K</i><i><sub>C</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0.0
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
        str = "class=ExcIEEEAC4A\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
