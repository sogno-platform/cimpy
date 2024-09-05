from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEAC8B(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type AC8B model. This model represents a PID voltage regulator with either a brushless exciter or DC exciter. The AVR in this model consists of PID control, with separate constants for the proportional (<i>K</i><i><sub>PR</sub></i>), integral (<i>K</i><i><sub>IR</sub></i>), and derivative (<i>K</i><i><sub>DR</sub></i>) gains. The representation of the brushless exciter (<i>T</i><i><sub>E</sub></i>, <i>K</i><i><sub>E</sub></i>, <i>S</i><i><sub>E</sub></i>, <i>K</i><i><sub>C</sub></i>, <i>K</i><i><sub>D</sub></i>) is similar to the model type AC2A. The type AC8B model can be used to represent static voltage regulators applied to brushless excitation systems. Digitally based voltage regulators feeding DC rotating main exciters can be represented with the AC type AC8B model with the parameters <i>K</i><i><sub>C</sub></i> and <i>K</i><i><sub>D</sub></i> set to 0.  For thyristor power stages fed from the generator terminals, the limits <i>V</i><i><sub>RMAX</sub></i> and <i>V</i><i><sub>RMIN</sub></i><i> </i>should be a function of terminal voltage: V<i><sub>T</sub></i> x <i>V</i><i><sub>RMAX</sub></i><sub> </sub>and <i>V</i><i><sub>T</sub></i> x <i>V</i><i><sub>RMIN</sub></i>. Reference: IEEE 421.5-2005, 6.8.

    :kpr: Voltage regulator proportional gain (<i>K</i><i><sub>PR</sub></i>) (&gt; 0 if ExcIEEEAC8B.kir = 0).  Typical value = 80. Default: 0.0
    :kir: Voltage regulator integral gain (<i>K</i><i><sub>IR</sub></i>) (&gt;= 0).  Typical value = 5. Default: 0.0
    :kdr: Voltage regulator derivative gain (<i>K</i><i><sub>DR</sub></i>) (&gt;= 0).  Typical value = 10. Default: 0.0
    :tdr: Lag time constant (<i>T</i><i><sub>DR</sub></i>) (&gt; 0).  Typical value = 0,1. Default: 0
    :vrmax: Maximum voltage regulator output (<i>V</i><i><sub>RMAX</sub></i>) (&gt; 0).  Typical value = 35. Default: 0.0
    :vrmin: Minimum voltage regulator output (<i>V</i><i><sub>RMIN</sub></i>) (&lt;= 0).  Typical value = 0. Default: 0.0
    :ka: Voltage regulator gain (<i>K</i><i><sub>A</sub></i>) (&gt; 0).  Typical value = 1. Default: 0.0
    :ta: Voltage regulator time constant (<i>T</i><i><sub>A</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
    :te: Exciter time constant, integration rate associated with exciter control (<i>T</i><i><sub>E</sub></i>) (&gt; 0).  Typical value = 1,2. Default: 0
    :vfemax: Exciter field current limit reference (<i>V</i><i><sub>FEMAX</sub></i>).  Typical value = 6. Default: 0.0
    :vemin: Minimum exciter voltage output (<i>V</i><i><sub>EMIN</sub></i>) (&lt;= 0).  Typical value = 0. Default: 0.0
    :ke: Exciter constant related to self-excited field (<i>K</i><i><sub>E</sub></i>).  Typical value = 1. Default: 0.0
    :kc: Rectifier loading factor proportional to commutating reactance (<i>K</i><i><sub>C</sub></i>) (&gt;= 0). Typical value = 0,55. Default: 0.0
    :kd: Demagnetizing factor, a function of exciter alternator reactances (<i>K</i><i><sub>D</sub></i>) (&gt;= 0).  Typical value = 1,1. Default: 0.0
    :ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (<i>V</i><i><sub>E1</sub></i>) (&gt; 0).  Typical value = 6,5. Default: 0.0
    :seve1: Exciter saturation function value at the corresponding exciter voltage, <i>V</i><i><sub>E1</sub></i>, back of commutating reactance (<i>S</i><i><sub>E</sub></i><i>[V</i><i><sub>E1</sub></i><i>]</i>) (&gt;= 0).  Typical value = 0,3. Default: 0.0
    :ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (<i>V</i><i><sub>E2</sub></i>) (&gt; 0).  Typical value = 9. Default: 0.0
    :seve2: Exciter saturation function value at the corresponding exciter voltage, <i>V</i><i><sub>E2</sub></i>, back of commutating reactance (<i>S</i><i><sub>E</sub></i><i>[V</i><i><sub>E2</sub></i><i>]</i>) (&gt;= 0).  Typical value = 3. Default: 0.0
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
        "ka": [
            cgmesProfile.DY.value,
        ],
        "ta": [
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
        ka=0.0,
        ta=0,
        te=0,
        vfemax=0.0,
        vemin=0.0,
        ke=0.0,
        kc=0.0,
        kd=0.0,
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
        self.ka = ka
        self.ta = ta
        self.te = te
        self.vfemax = vfemax
        self.vemin = vemin
        self.ke = ke
        self.kc = kc
        self.kd = kd
        self.ve1 = ve1
        self.seve1 = seve1
        self.ve2 = ve2
        self.seve2 = seve2

    def __str__(self):
        str = "class=ExcIEEEAC8B\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
