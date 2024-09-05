from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcST7B(ExcitationSystemDynamics):
    """
    Modified IEEE ST7B static excitation system without stator current limiter (SCL) and current compensator (DROOP) inputs.

    :kh: High-value gate feedback gain (<i>Kh</i>) (&gt;= 0).  Typical value = 1. Default: 0.0
    :kia: Voltage regulator integral gain (<i>Kia</i>) (&gt;= 0).  Typical value = 1. Default: 0.0
    :kl: Low-value gate feedback gain (<i>Kl</i>) (&gt;= 0).  Typical value = 1. Default: 0.0
    :kpa: Voltage regulator proportional gain (<i>Kpa</i>) (&gt; 0).  Typical value = 40. Default: 0.0
    :oelin: OEL input selector (<i>OELin</i>). Typical value = noOELinput. Default: None
    :tb: Regulator lag time constant (<i>Tb</i>) (&gt;= 0).  Typical value = 1. Default: 0
    :tc: Regulator lead time constant (<i>Tc</i>) (&gt;= 0).  Typical value = 1. Default: 0
    :tf: Excitation control system stabilizer time constant (<i>Tf</i>) (&gt;= 0).  Typical value = 1. Default: 0
    :tg: Feedback time constant of inner loop field voltage regulator (<i>Tg</i>) (&gt;= 0).  Typical value = 1. Default: 0
    :tia: Feedback time constant (<i>Tia</i>) (&gt;= 0).  Typical value = 3. Default: 0
    :ts: Rectifier firing time constant (<i>Ts</i>) (&gt;= 0).  Typical value = 0. Default: 0
    :uelin: UEL input selector (<i>UELin</i>). Typical value = noUELinput. Default: None
    :vmax: Maximum voltage reference signal (<i>Vmax</i>) (&gt; 0 and &gt; ExcST7B.vmin)).  Typical value = 1,1. Default: 0.0
    :vmin: Minimum voltage reference signal (<i>Vmin</i>) (&gt; 0 and &lt; ExcST7B.vmax).  Typical value = 0,9. Default: 0.0
    :vrmax: Maximum voltage regulator output (<i>Vrmax</i>) (&gt; 0).  Typical value = 5. Default: 0.0
    :vrmin: Minimum voltage regulator output (<i>Vrmin</i>) (&lt; 0).  Typical value = -4,5. Default: 0.0
    """

    cgmesProfile = ExcitationSystemDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "kh": [
            cgmesProfile.DY.value,
        ],
        "kia": [
            cgmesProfile.DY.value,
        ],
        "kl": [
            cgmesProfile.DY.value,
        ],
        "kpa": [
            cgmesProfile.DY.value,
        ],
        "oelin": [
            cgmesProfile.DY.value,
        ],
        "tb": [
            cgmesProfile.DY.value,
        ],
        "tc": [
            cgmesProfile.DY.value,
        ],
        "tf": [
            cgmesProfile.DY.value,
        ],
        "tg": [
            cgmesProfile.DY.value,
        ],
        "tia": [
            cgmesProfile.DY.value,
        ],
        "ts": [
            cgmesProfile.DY.value,
        ],
        "uelin": [
            cgmesProfile.DY.value,
        ],
        "vmax": [
            cgmesProfile.DY.value,
        ],
        "vmin": [
            cgmesProfile.DY.value,
        ],
        "vrmax": [
            cgmesProfile.DY.value,
        ],
        "vrmin": [
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
        kh=0.0,
        kia=0.0,
        kl=0.0,
        kpa=0.0,
        oelin=None,
        tb=0,
        tc=0,
        tf=0,
        tg=0,
        tia=0,
        ts=0,
        uelin=None,
        vmax=0.0,
        vmin=0.0,
        vrmax=0.0,
        vrmin=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.kh = kh
        self.kia = kia
        self.kl = kl
        self.kpa = kpa
        self.oelin = oelin
        self.tb = tb
        self.tc = tc
        self.tf = tf
        self.tg = tg
        self.tia = tia
        self.ts = ts
        self.uelin = uelin
        self.vmax = vmax
        self.vmin = vmin
        self.vrmax = vrmax
        self.vrmin = vrmin

    def __str__(self):
        str = "class=ExcST7B\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
