from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcREXS(ExcitationSystemDynamics):
    """
    General purpose rotating excitation system.  This model can be used to represent a wide range of excitation systems whose DC power source is an AC or DC generator. It encompasses IEEE type AC1, AC2, DC1, and DC2 excitation system models.

    :e1: Field voltage value 1 (<i>E</i><i><sub>1</sub></i>).  Typical value = 3. Default: 0.0
    :e2: Field voltage value 2 (<i>E</i><i><sub>2</sub></i>).  Typical value = 4. Default: 0.0
    :fbf: Rate feedback signal flag (<i>fbf</i>). Typical value = fieldCurrent. Default: None
    :flimf: Limit type flag (<i>Flimf</i>).  Typical value = 0. Default: 0.0
    :kc: Rectifier regulation factor (<i>Kc</i>).  Typical value = 0,05. Default: 0.0
    :kd: Exciter regulation factor (<i>Kd</i>).  Typical value = 2. Default: 0.0
    :ke: Exciter field proportional constant (<i>Ke</i>).  Typical value = 1. Default: 0.0
    :kefd: Field voltage feedback gain (<i>Kefd</i>).  Typical value = 0. Default: 0.0
    :kf: Rate feedback gain (<i>Kf</i>) (&gt;= 0).  Typical value = 0,05. Default: 0
    :kh: Field voltage controller feedback gain (<i>Kh</i>).  Typical value = 0. Default: 0.0
    :kii: Field current regulator integral gain (<i>Kii</i>).  Typical value = 0. Default: 0.0
    :kip: Field current regulator proportional gain (<i>Kip</i>).  Typical value = 1. Default: 0.0
    :ks: Coefficient to allow different usage of the model-speed coefficient (<i>Ks</i>).  Typical value = 0. Default: 0.0
    :kvi: Voltage regulator integral gain (<i>Kvi</i>).  Typical value = 0. Default: 0.0
    :kvp: Voltage regulator proportional gain (<i>Kvp</i>).  Typical value = 2800. Default: 0.0
    :kvphz: V/Hz limiter gain (<i>Kvphz</i>).  Typical value = 0. Default: 0.0
    :nvphz: Pickup speed of V/Hz limiter (<i>Nvphz</i>).  Typical value = 0. Default: 0.0
    :se1: Saturation factor at <i>E</i><i><sub>1</sub></i><i> </i>(<i>Se</i><i><sub>1</sub></i>).  Typical value = 0,0001. Default: 0.0
    :se2: Saturation factor at <i>E</i><i><sub>2</sub></i> (<i>Se</i><i><sub>2</sub></i>).  Typical value = 0,001. Default: 0.0
    :ta: Voltage regulator time constant (<i>Ta</i>) (&gt;= 0).  If = 0, block is bypassed.  Typical value = 0,01. Default: 0
    :tb1: Lag time constant (<i>Tb1</i>) (&gt;= 0).  If = 0, block is bypassed.  Typical value = 0. Default: 0
    :tb2: Lag time constant (<i>Tb2</i>) (&gt;= 0).  If = 0, block is bypassed.  Typical value = 0. Default: 0
    :tc1: Lead time constant (<i>Tc1</i>) (&gt;= 0).  Typical value = 0. Default: 0
    :tc2: Lead time constant (<i>Tc2</i>) (&gt;= 0).  Typical value = 0. Default: 0
    :te: Exciter field time constant (<i>Te</i>) (&gt; 0).  Typical value = 1,2. Default: 0
    :tf: Rate feedback time constant (<i>Tf</i>) (&gt;= 0).  If = 0, the feedback path is not used.  Typical value = 1. Default: 0
    :tf1: Feedback lead time constant (<i>Tf1</i>) (&gt;= 0).  Typical value = 0. Default: 0
    :tf2: Feedback lag time constant (<i>Tf2</i>) (&gt;= 0).  If = 0, block is bypassed.  Typical value = 0. Default: 0
    :tp: Field current bridge time constant (<i>Tp</i>) (&gt;= 0).  Typical value = 0. Default: 0
    :vcmax: Maximum compounding voltage (<i>Vcmax</i>).  Typical value = 0. Default: 0.0
    :vfmax: Maximum exciter field current (<i>Vfmax</i>) (&gt; ExcREXS.vfmin).  Typical value = 47. Default: 0.0
    :vfmin: Minimum exciter field current (<i>Vfmin</i>) (&lt; ExcREXS.vfmax).  Typical value = -20. Default: 0.0
    :vimax: Voltage regulator input limit (<i>Vimax</i>).  Typical value = 0,1. Default: 0.0
    :vrmax: Maximum controller output (V<i>rmax</i>) (&gt; ExcREXS.vrmin).  Typical value = 47. Default: 0.0
    :vrmin: Minimum controller output (<i>Vrmin</i>) (&lt; ExcREXS.vrmax).  Typical value = -20. Default: 0.0
    :xc: Exciter compounding reactance (<i>Xc</i>).  Typical value = 0. Default: 0.0
    """

    cgmesProfile = ExcitationSystemDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "e1": [
            cgmesProfile.DY.value,
        ],
        "e2": [
            cgmesProfile.DY.value,
        ],
        "fbf": [
            cgmesProfile.DY.value,
        ],
        "flimf": [
            cgmesProfile.DY.value,
        ],
        "kc": [
            cgmesProfile.DY.value,
        ],
        "kd": [
            cgmesProfile.DY.value,
        ],
        "ke": [
            cgmesProfile.DY.value,
        ],
        "kefd": [
            cgmesProfile.DY.value,
        ],
        "kf": [
            cgmesProfile.DY.value,
        ],
        "kh": [
            cgmesProfile.DY.value,
        ],
        "kii": [
            cgmesProfile.DY.value,
        ],
        "kip": [
            cgmesProfile.DY.value,
        ],
        "ks": [
            cgmesProfile.DY.value,
        ],
        "kvi": [
            cgmesProfile.DY.value,
        ],
        "kvp": [
            cgmesProfile.DY.value,
        ],
        "kvphz": [
            cgmesProfile.DY.value,
        ],
        "nvphz": [
            cgmesProfile.DY.value,
        ],
        "se1": [
            cgmesProfile.DY.value,
        ],
        "se2": [
            cgmesProfile.DY.value,
        ],
        "ta": [
            cgmesProfile.DY.value,
        ],
        "tb1": [
            cgmesProfile.DY.value,
        ],
        "tb2": [
            cgmesProfile.DY.value,
        ],
        "tc1": [
            cgmesProfile.DY.value,
        ],
        "tc2": [
            cgmesProfile.DY.value,
        ],
        "te": [
            cgmesProfile.DY.value,
        ],
        "tf": [
            cgmesProfile.DY.value,
        ],
        "tf1": [
            cgmesProfile.DY.value,
        ],
        "tf2": [
            cgmesProfile.DY.value,
        ],
        "tp": [
            cgmesProfile.DY.value,
        ],
        "vcmax": [
            cgmesProfile.DY.value,
        ],
        "vfmax": [
            cgmesProfile.DY.value,
        ],
        "vfmin": [
            cgmesProfile.DY.value,
        ],
        "vimax": [
            cgmesProfile.DY.value,
        ],
        "vrmax": [
            cgmesProfile.DY.value,
        ],
        "vrmin": [
            cgmesProfile.DY.value,
        ],
        "xc": [
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
        e1=0.0,
        e2=0.0,
        fbf=None,
        flimf=0.0,
        kc=0.0,
        kd=0.0,
        ke=0.0,
        kefd=0.0,
        kf=0,
        kh=0.0,
        kii=0.0,
        kip=0.0,
        ks=0.0,
        kvi=0.0,
        kvp=0.0,
        kvphz=0.0,
        nvphz=0.0,
        se1=0.0,
        se2=0.0,
        ta=0,
        tb1=0,
        tb2=0,
        tc1=0,
        tc2=0,
        te=0,
        tf=0,
        tf1=0,
        tf2=0,
        tp=0,
        vcmax=0.0,
        vfmax=0.0,
        vfmin=0.0,
        vimax=0.0,
        vrmax=0.0,
        vrmin=0.0,
        xc=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.e1 = e1
        self.e2 = e2
        self.fbf = fbf
        self.flimf = flimf
        self.kc = kc
        self.kd = kd
        self.ke = ke
        self.kefd = kefd
        self.kf = kf
        self.kh = kh
        self.kii = kii
        self.kip = kip
        self.ks = ks
        self.kvi = kvi
        self.kvp = kvp
        self.kvphz = kvphz
        self.nvphz = nvphz
        self.se1 = se1
        self.se2 = se2
        self.ta = ta
        self.tb1 = tb1
        self.tb2 = tb2
        self.tc1 = tc1
        self.tc2 = tc2
        self.te = te
        self.tf = tf
        self.tf1 = tf1
        self.tf2 = tf2
        self.tp = tp
        self.vcmax = vcmax
        self.vfmax = vfmax
        self.vfmin = vfmin
        self.vimax = vimax
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.xc = xc

    def __str__(self):
        str = "class=ExcREXS\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
