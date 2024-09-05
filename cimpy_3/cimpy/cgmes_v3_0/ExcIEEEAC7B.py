from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEAC7B(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type AC7B model. The model represents excitation systems which consist of an AC alternator with either stationary or rotating rectifiers to produce the DC field requirements. It is an upgrade to earlier AC excitation systems, which replace only the controls but retain the AC alternator and diode rectifier bridge. Reference: IEEE 421.5-2005, 6.7. Note, however, that in IEEE 421.5-2005, the [1 / <i>sT</i><i><sub>E</sub></i>] block is shown as [1 / (1 + <i>sT</i><i><sub>E</sub></i>)], which is incorrect.

    :kpr: Voltage regulator proportional gain (<i>K</i><i><sub>PR</sub></i>) (&gt; 0 if ExcIEEEAC7B.kir = 0).  Typical value = 4,24. Default: 0.0
    :kir: Voltage regulator integral gain (<i>K</i><i><sub>IR</sub></i>) (&gt;= 0).  Typical value = 4,24. Default: 0.0
    :kdr: Voltage regulator derivative gain (<i>K</i><i><sub>DR</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0.0
    :tdr: Lag time constant (<i>T</i><i><sub>DR</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
    :vrmax: Maximum voltage regulator output (<i>V</i><i><sub>RMAX</sub></i>) (&gt; 0).  Typical value = 5,79. Default: 0.0
    :vrmin: Minimum voltage regulator output (<i>V</i><i><sub>RMIN</sub></i>) (&lt; 0).  Typical value = -5,79. Default: 0.0
    :kpa: Voltage regulator proportional gain (<i>K</i><i><sub>PA</sub></i>) (&gt; 0 if ExcIEEEAC7B.kia = 0).  Typical value = 65,36. Default: 0.0
    :kia: Voltage regulator integral gain (<i>K</i><i><sub>IA</sub></i>) (&gt;= 0).  Typical value = 59,69. Default: 0.0
    :vamax: Maximum voltage regulator output (<i>V</i><i><sub>AMAX</sub></i>) (&gt; 0).  Typical value = 1. Default: 0.0
    :vamin: Minimum voltage regulator output (<i>V</i><i><sub>AMIN</sub></i>) (&lt; 0).  Typical value = -0,95. Default: 0.0
    :kp: Potential circuit gain coefficient (<i>K</i><i><sub>P</sub></i>) (&gt; 0).  Typical value = 4,96. Default: 0.0
    :kl: Exciter field voltage lower limit parameter (<i>K</i><i><sub>L</sub></i>).  Typical value = 10. Default: 0.0
    :te: Exciter time constant, integration rate associated with exciter control (<i>T</i><i><sub>E</sub></i>) (&gt; 0).  Typical value = 1,1. Default: 0
    :vfemax: Exciter field current limit reference (<i>V</i><i><sub>FEMAX</sub></i>).  Typical value = 6,9. Default: 0.0
    :vemin: Minimum exciter voltage output (<i>V</i><i><sub>EMIN</sub></i>) (&lt;= 0).  Typical value = 0. Default: 0.0
    :ke: Exciter constant related to self-excited field (<i>K</i><i><sub>E</sub></i>).  Typical value = 1. Default: 0.0
    :kc: Rectifier loading factor proportional to commutating reactance (<i>K</i><i><sub>C</sub></i>) (&gt;= 0). Typical value = 0,18. Default: 0.0
    :kd: Demagnetizing factor, a function of exciter alternator reactances (<i>K</i><i><sub>D</sub></i>) (&gt;= 0).  Typical value = 0,02. Default: 0.0
    :kf1: Excitation control system stabilizer gain (<i>K</i><i><sub>F1</sub></i>) (&gt;= 0).  Typical value = 0,212. Default: 0.0
    :kf2: Excitation control system stabilizer gain (<i>K</i><i><sub>F2</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0.0
    :kf3: Excitation control system stabilizer gain (<i>K</i><i><sub>F3</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0.0
    :tf: Excitation control system stabilizer time constant (<i>T</i><i><sub>F</sub></i>) (&gt; 0).  Typical value = 1. Default: 0
    :ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (<i>V</i><i><sub>E1</sub></i>) (&gt; 0).  Typical value = 6,3. Default: 0.0
    :seve1: Exciter saturation function value at the corresponding exciter voltage, <i>V</i><i><sub>E1</sub></i>, back of commutating reactance (<i>S</i><i><sub>E</sub></i><i>[V</i><i><sub>E1</sub></i><i>]</i>) (&gt;= 0).  Typical value = 0,44. Default: 0.0
    :ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (<i>V</i><i><sub>E2</sub></i>) (&gt; 0).  Typical value = 3,02. Default: 0.0
    :seve2: Exciter saturation function value at the corresponding exciter voltage, <i>V</i><i><sub>E2</sub></i>, back of commutating reactance (<i>S</i><i><sub>E</sub></i><i>[V</i><i><sub>E2</sub></i><i>]</i>) (&gt;= 0).  Typical value = 0,075. Default: 0.0
    """

    cgmesProfile = ExcitationSystemDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "kpr": [
            cgmesProfile.DY.value,
        ],
        "kir": [
            cgmesProfile.DY.value,
        ],
        "kdr": [
            cgmesProfile.DY.value,
        ],
        "tdr": [
            cgmesProfile.DY.value,
        ],
        "vrmax": [
            cgmesProfile.DY.value,
        ],
        "vrmin": [
            cgmesProfile.DY.value,
        ],
        "kpa": [
            cgmesProfile.DY.value,
        ],
        "kia": [
            cgmesProfile.DY.value,
        ],
        "vamax": [
            cgmesProfile.DY.value,
        ],
        "vamin": [
            cgmesProfile.DY.value,
        ],
        "kp": [
            cgmesProfile.DY.value,
        ],
        "kl": [
            cgmesProfile.DY.value,
        ],
        "te": [
            cgmesProfile.DY.value,
        ],
        "vfemax": [
            cgmesProfile.DY.value,
        ],
        "vemin": [
            cgmesProfile.DY.value,
        ],
        "ke": [
            cgmesProfile.DY.value,
        ],
        "kc": [
            cgmesProfile.DY.value,
        ],
        "kd": [
            cgmesProfile.DY.value,
        ],
        "kf1": [
            cgmesProfile.DY.value,
        ],
        "kf2": [
            cgmesProfile.DY.value,
        ],
        "kf3": [
            cgmesProfile.DY.value,
        ],
        "tf": [
            cgmesProfile.DY.value,
        ],
        "ve1": [
            cgmesProfile.DY.value,
        ],
        "seve1": [
            cgmesProfile.DY.value,
        ],
        "ve2": [
            cgmesProfile.DY.value,
        ],
        "seve2": [
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
        kpr=0.0,
        kir=0.0,
        kdr=0.0,
        tdr=0,
        vrmax=0.0,
        vrmin=0.0,
        kpa=0.0,
        kia=0.0,
        vamax=0.0,
        vamin=0.0,
        kp=0.0,
        kl=0.0,
        te=0,
        vfemax=0.0,
        vemin=0.0,
        ke=0.0,
        kc=0.0,
        kd=0.0,
        kf1=0.0,
        kf2=0.0,
        kf3=0.0,
        tf=0,
        ve1=0.0,
        seve1=0.0,
        ve2=0.0,
        seve2=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.kpr = kpr
        self.kir = kir
        self.kdr = kdr
        self.tdr = tdr
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.kpa = kpa
        self.kia = kia
        self.vamax = vamax
        self.vamin = vamin
        self.kp = kp
        self.kl = kl
        self.te = te
        self.vfemax = vfemax
        self.vemin = vemin
        self.ke = ke
        self.kc = kc
        self.kd = kd
        self.kf1 = kf1
        self.kf2 = kf2
        self.kf3 = kf3
        self.tf = tf
        self.ve1 = ve1
        self.seve1 = seve1
        self.ve2 = ve2
        self.seve2 = seve2

    def __str__(self):
        str = "class=ExcIEEEAC7B\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
