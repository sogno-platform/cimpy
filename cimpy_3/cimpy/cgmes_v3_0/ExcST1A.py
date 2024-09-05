from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcST1A(ExcitationSystemDynamics):
    """
    Modification of an old IEEE ST1A static excitation system without overexcitation limiter (OEL) and underexcitation limiter (UEL).

    :vimax: Maximum voltage regulator input limit (<i>Vimax</i>) (&gt; 0).  Typical value = 999. Default: 0.0
    :vimin: Minimum voltage regulator input limit (<i>Vimin</i>) (&lt; 0).  Typical value = -999. Default: 0.0
    :tc: Voltage regulator time constant (<i>Tc</i>) (&gt;= 0).  Typical value = 1. Default: 0
    :tb: Voltage regulator time constant (<i>Tb</i>) (&gt;= 0).  Typical value = 10. Default: 0
    :ka: Voltage regulator gain (<i>Ka</i>) (&gt; 0).  Typical value = 190. Default: 0.0
    :ta: Voltage regulator time constant (<i>Ta</i>) (&gt;= 0).  Typical value = 0,02. Default: 0
    :vrmax: Maximum voltage regulator outputs (<i>Vrmax</i>) (&gt; 0) .  Typical value = 7,8. Default: 0.0
    :vrmin: Minimum voltage regulator outputs (<i>Vrmin</i>) (&lt; 0).  Typical value = -6,7. Default: 0.0
    :kc: Rectifier loading factor proportional to commutating reactance (<i>Kc</i>) (&gt;= 0). Typical value = 0,05. Default: 0.0
    :kf: Excitation control system stabilizer gains (<i>Kf</i>) (&gt;= 0).  Typical value = 0. Default: 0.0
    :tf: Excitation control system stabilizer time constant (<i>Tf</i>) (&gt;= 0).  Typical value = 1. Default: 0
    :tc1: Voltage regulator time constant (<i>Tc1</i>) (&gt;= 0).  Typical value = 0. Default: 0
    :tb1: Voltage regulator time constant (<i>Tb1</i>) (&gt;= 0).  Typical value = 0. Default: 0
    :vamax: Maximum voltage regulator output (<i>Vamax</i>) (&gt; 0).  Typical value = 999. Default: 0.0
    :vamin: Minimum voltage regulator output (<i>Vamin</i>) (&lt; 0).  Typical value = -999. Default: 0.0
    :ilr: Exciter output current limit reference (<i>Ilr</i>).  Typical value = 0. Default: 0.0
    :klr: Exciter output current limiter gain (<i>Klr</i>).  Typical value = 0. Default: 0.0
    :xe: Excitation xfmr effective reactance (<i>Xe</i>).  Typical value = 0,04. Default: 0.0
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
        "kf": [
            cgmesProfile.DY.value,
        ],
        "tf": [
            cgmesProfile.DY.value,
        ],
        "tc1": [
            cgmesProfile.DY.value,
        ],
        "tb1": [
            cgmesProfile.DY.value,
        ],
        "vamax": [
            cgmesProfile.DY.value,
        ],
        "vamin": [
            cgmesProfile.DY.value,
        ],
        "ilr": [
            cgmesProfile.DY.value,
        ],
        "klr": [
            cgmesProfile.DY.value,
        ],
        "xe": [
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
        kf=0.0,
        tf=0,
        tc1=0,
        tb1=0,
        vamax=0.0,
        vamin=0.0,
        ilr=0.0,
        klr=0.0,
        xe=0.0,
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
        self.kf = kf
        self.tf = tf
        self.tc1 = tc1
        self.tb1 = tb1
        self.vamax = vamax
        self.vamin = vamin
        self.ilr = ilr
        self.klr = klr
        self.xe = xe

    def __str__(self):
        str = "class=ExcST1A\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
