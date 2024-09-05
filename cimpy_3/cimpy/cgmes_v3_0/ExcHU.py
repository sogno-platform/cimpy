from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcHU(ExcitationSystemDynamics):
    """
    Hungarian excitation system, with built-in voltage transducer.

    :tr: Filter time constant (<i>Tr</i>) (&gt;= 0). If a voltage compensator is used in conjunction with this excitation system model, <i>Tr </i>should be set to 0.  Typical value = 0,01. Default: 0
    :te: Major loop PI tag integration time constant (<i>Te</i>) (&gt;= 0).  Typical value = 0,154. Default: 0
    :imin: Major loop PI tag output signal lower limit (<i>Imin</i>) (&lt; ExcHU.imax).  Typical value = 0,1. Default: 0.0
    :imax: Major loop PI tag output signal upper limit (<i>Imax</i>) (&gt; ExcHU.imin).  Typical value = 2,19. Default: 0.0
    :ae: Major loop PI tag gain factor (<i>Ae</i>).  Typical value = 3. Default: 0.0
    :emin: Field voltage control signal lower limit on AVR base (<i>Emin</i>) (&lt; ExcHU.emax).  Typical value = -0,866. Default: 0.0
    :emax: Field voltage control signal upper limit on AVR base (<i>Emax</i>) (&gt; ExcHU.emin).  Typical value = 0,996. Default: 0.0
    :ki: Current base conversion constant (<i>Ki</i>).  Typical value = 0,21428. Default: 0.0
    :ai: Minor loop PI tag gain factor (<i>Ai</i>).  Typical value = 22. Default: 0.0
    :ti: Minor loop PI control tag integration time constant (<i>Ti</i>) (&gt;= 0).  Typical value = 0,01333. Default: 0
    :atr: AVR constant (<i>Atr</i>).  Typical value = 2,19. Default: 0.0
    :ke: Voltage base conversion constant (<i>Ke</i>).  Typical value = 4,666. Default: 0.0
    """

    cgmesProfile = ExcitationSystemDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "tr": [
            cgmesProfile.DY.value,
        ],
        "te": [
            cgmesProfile.DY.value,
        ],
        "imin": [
            cgmesProfile.DY.value,
        ],
        "imax": [
            cgmesProfile.DY.value,
        ],
        "ae": [
            cgmesProfile.DY.value,
        ],
        "emin": [
            cgmesProfile.DY.value,
        ],
        "emax": [
            cgmesProfile.DY.value,
        ],
        "ki": [
            cgmesProfile.DY.value,
        ],
        "ai": [
            cgmesProfile.DY.value,
        ],
        "ti": [
            cgmesProfile.DY.value,
        ],
        "atr": [
            cgmesProfile.DY.value,
        ],
        "ke": [
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
        tr=0,
        te=0,
        imin=0.0,
        imax=0.0,
        ae=0.0,
        emin=0.0,
        emax=0.0,
        ki=0.0,
        ai=0.0,
        ti=0,
        atr=0.0,
        ke=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.tr = tr
        self.te = te
        self.imin = imin
        self.imax = imax
        self.ae = ae
        self.emin = emin
        self.emax = emax
        self.ki = ki
        self.ai = ai
        self.ti = ti
        self.atr = atr
        self.ke = ke

    def __str__(self):
        str = "class=ExcHU\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
