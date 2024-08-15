from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcELIN2(ExcitationSystemDynamics):
    """
    Detailed Excitation System Model - ELIN (VATECH).  This model represents an all-static excitation system. A PI voltage controller establishes a desired field current set point for a proportional current controller. The integrator of the PI controller has a follow-up input to match its signal to the present field current.  Power system stabilizer models used in conjunction with this excitation system model: PssELIN2, PssIEEE2B, Pss2B.

    :efdbas: Gain (Efdbas).  Typical Value = 0.1. Default: 0.0
    :iefmax: Limiter (Iefmax).  Typical Value = 1. Default: 0.0
    :iefmax2: Minimum open circuit excitation voltage (Iefmax2).  Typical Value = -5. Default: 0.0
    :iefmin: Limiter (Iefmin).  Typical Value = 1. Default: 0.0
    :k1: Voltage regulator input gain (K1).  Typical Value = 0. Default: 0.0
    :k1ec: Voltage regulator input limit (K1ec).  Typical Value = 2. Default: 0.0
    :k2: Gain (K2).  Typical Value = 5. Default: 0.0
    :k3: Gain (K3).  Typical Value = 0.1. Default: 0.0
    :k4: Gain (K4).  Typical Value = 0. Default: 0.0
    :kd1: Voltage controller derivative gain (Kd1).  Typical Value = 34.5. Default: 0.0
    :ke2: Gain (Ke2).  Typical Value = 0.1. Default: 0.0
    :ketb: Gain (Ketb).  Typical Value = 0.06. Default: 0.0
    :pid1max: Controller follow up gain (PID1max).  Typical Value = 2. Default: 0.0
    :seve1: Exciter saturation function value at the corresponding exciter voltage, Ve1, back of commutating reactance (Se[Ve1]).  Typical Value = 0. Default: 0.0
    :seve2: Exciter saturation function value at the corresponding exciter voltage, Ve2, back of commutating reactance (Se[Ve2]).  Typical Value = 1. Default: 0.0
    :tb1: Voltage controller derivative washout time constant (Tb1).  Typical Value = 12.45. Default: 0.0
    :te: Time constant (Te).  Typical Value = 0. Default: 0.0
    :te2: Time Constant (Te2).  Typical Value = 1. Default: 0.0
    :ti1: Controller follow up dead band (Ti1).  Typical Value = 0. Default: 0.0
    :ti3: Time constant (Ti3).  Typical Value = 3. Default: 0.0
    :ti4: Time constant (Ti4).  Typical Value = 0. Default: 0.0
    :tr4: Time constant (Tr4).  Typical Value = 1. Default: 0.0
    :upmax: Limiter (Upmax).  Typical Value = 3. Default: 0.0
    :upmin: Limiter (Upmin).  Typical Value = 0. Default: 0.0
    :ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1).  Typical Value = 3. Default: 0.0
    :ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve2).  Typical Value = 0. Default: 0.0
    :xp: Excitation transformer effective reactance (Xp).  Typical Value = 1. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "efdbas": [Profile.DY.value, ],
        "iefmax": [Profile.DY.value, ],
        "iefmax2": [Profile.DY.value, ],
        "iefmin": [Profile.DY.value, ],
        "k1": [Profile.DY.value, ],
        "k1ec": [Profile.DY.value, ],
        "k2": [Profile.DY.value, ],
        "k3": [Profile.DY.value, ],
        "k4": [Profile.DY.value, ],
        "kd1": [Profile.DY.value, ],
        "ke2": [Profile.DY.value, ],
        "ketb": [Profile.DY.value, ],
        "pid1max": [Profile.DY.value, ],
        "seve1": [Profile.DY.value, ],
        "seve2": [Profile.DY.value, ],
        "tb1": [Profile.DY.value, ],
        "te": [Profile.DY.value, ],
        "te2": [Profile.DY.value, ],
        "ti1": [Profile.DY.value, ],
        "ti3": [Profile.DY.value, ],
        "ti4": [Profile.DY.value, ],
        "tr4": [Profile.DY.value, ],
        "upmax": [Profile.DY.value, ],
        "upmin": [Profile.DY.value, ],
        "ve1": [Profile.DY.value, ],
        "ve2": [Profile.DY.value, ],
        "xp": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, efdbas = 0.0, iefmax = 0.0, iefmax2 = 0.0, iefmin = 0.0, k1 = 0.0, k1ec = 0.0, k2 = 0.0, k3 = 0.0, k4 = 0.0, kd1 = 0.0, ke2 = 0.0, ketb = 0.0, pid1max = 0.0, seve1 = 0.0, seve2 = 0.0, tb1 = 0.0, te = 0.0, te2 = 0.0, ti1 = 0.0, ti3 = 0.0, ti4 = 0.0, tr4 = 0.0, upmax = 0.0, upmin = 0.0, ve1 = 0.0, ve2 = 0.0, xp = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.efdbas = efdbas
        self.iefmax = iefmax
        self.iefmax2 = iefmax2
        self.iefmin = iefmin
        self.k1 = k1
        self.k1ec = k1ec
        self.k2 = k2
        self.k3 = k3
        self.k4 = k4
        self.kd1 = kd1
        self.ke2 = ke2
        self.ketb = ketb
        self.pid1max = pid1max
        self.seve1 = seve1
        self.seve2 = seve2
        self.tb1 = tb1
        self.te = te
        self.te2 = te2
        self.ti1 = ti1
        self.ti3 = ti3
        self.ti4 = ti4
        self.tr4 = tr4
        self.upmax = upmax
        self.upmin = upmin
        self.ve1 = ve1
        self.ve2 = ve2
        self.xp = xp

    def __str__(self):
        str = "class=ExcELIN2\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
