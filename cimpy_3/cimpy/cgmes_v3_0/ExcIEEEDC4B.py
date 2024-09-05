from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEDC4B(ExcitationSystemDynamics):
    """
    IEEE 421.5-2005 type DC4B model. These excitation systems utilize a field-controlled DC commutator exciter with a continuously acting voltage regulator having supplies obtained from the generator or auxiliary bus. Reference: IEEE 421.5-2005, 5.4.

    :ka: Voltage regulator gain (<i>K</i><i><sub>A</sub></i>) (&gt; 0).  Typical value = 1. Default: 0.0
    :ta: Voltage regulator time constant (<i>T</i><i><sub>A</sub></i>) (&gt; 0).  Typical value = 0,2. Default: 0
    :kp: Regulator proportional gain (<i>K</i><i><sub>P</sub></i>) (&gt;= 0).  Typical value = 20. Default: 0.0
    :ki: Regulator integral gain (<i>K</i><i><sub>I</sub></i>) (&gt;= 0).  Typical value = 20. Default: 0.0
    :kd: Regulator derivative gain (<i>K</i><i><sub>D</sub></i>) (&gt;= 0).  Typical value = 20. Default: 0.0
    :td: Regulator derivative filter time constant (<i>T</i><i><sub>D</sub></i>) (&gt; 0 if ExcIEEEDC4B.kd &gt; 0).  Typical value = 0,01. Default: 0
    :vrmax: Maximum voltage regulator output (<i>V</i><i><sub>RMAX</sub></i>) (&gt; ExcIEEEDC4B.vrmin).  Typical value = 2,7. Default: 0.0
    :vrmin: Minimum voltage regulator output (<i>V</i><i><sub>RMIN</sub></i>) (&lt;= 0 and &lt; ExcIEEEDC4B.vrmax).  Typical value = -0,9. Default: 0.0
    :ke: Exciter constant related to self-excited field (<i>K</i><i><sub>E</sub></i>).  Typical value = 1. Default: 0.0
    :te: Exciter time constant, integration rate associated with exciter control (<i>T</i><i><sub>E</sub></i>) (&gt; 0).  Typical value = 0,8. Default: 0
    :kf: Excitation control system stabilizer gain (<i>K</i><i><sub>F</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0.0
    :tf: Excitation control system stabilizer time constant (<i>T</i><i><sub>F</sub></i>) (&gt;= 0).  Typical value = 1. Default: 0
    :efd1: Exciter voltage at which exciter saturation is defined (<i>E</i><i><sub>FD1</sub></i>) (&gt; 0).  Typical value = 1,75. Default: 0.0
    :seefd1: Exciter saturation function value at the corresponding exciter voltage, <i>E</i><i><sub>FD1</sub></i> (<i>S</i><i><sub>E</sub></i><i>[E</i><i><sub>FD1</sub></i><i>]</i>) (&gt;= 0).  Typical value = 0,08. Default: 0.0
    :efd2: Exciter voltage at which exciter saturation is defined (<i>E</i><i><sub>FD2</sub></i>) (&gt; 0).  Typical value = 2,33. Default: 0.0
    :seefd2: Exciter saturation function value at the corresponding exciter voltage, <i>E</i><i><sub>FD2</sub></i> (<i>S</i><i><sub>E</sub></i><i>[E</i><i><sub>FD2</sub></i><i>]</i>) (&gt;= 0).  Typical value = 0,27. Default: 0.0
    :vemin: Minimum exciter voltage output (<i>V</i><i><sub>EMIN</sub></i>) (&lt;= 0).  Typical value = 0. Default: 0.0
    :oelin: OEL input (<i>OELin</i>). true = LV gate false = subtract from error signal. Typical value = true. Default: False
    :uelin: UEL input (<i>UELin</i>). true = HV gate false = add to error signal. Typical value = true. Default: False
    """

    cgmesProfile = ExcitationSystemDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "ka": [
            cgmesProfile.DY.value,
        ],
        "ta": [
            cgmesProfile.DY.value,
        ],
        "kp": [
            cgmesProfile.DY.value,
        ],
        "ki": [
            cgmesProfile.DY.value,
        ],
        "kd": [
            cgmesProfile.DY.value,
        ],
        "td": [
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
        "vemin": [
            cgmesProfile.DY.value,
        ],
        "oelin": [
            cgmesProfile.DY.value,
        ],
        "uelin": [
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
        ta=0,
        kp=0.0,
        ki=0.0,
        kd=0.0,
        td=0,
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
        vemin=0.0,
        oelin=False,
        uelin=False,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.ka = ka
        self.ta = ta
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.td = td
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
        self.vemin = vemin
        self.oelin = oelin
        self.uelin = uelin

    def __str__(self):
        str = "class=ExcIEEEDC4B\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
