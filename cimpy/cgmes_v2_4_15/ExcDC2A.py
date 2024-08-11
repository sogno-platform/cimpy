from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcDC2A(ExcitationSystemDynamics):
    """
    Modified IEEE DC2A direct current commutator exciters with speed input, one more leg block in feedback loop and without underexcitation limiters (UEL) inputs.  DC type 2 excitation system model with added speed multiplier, added lead-lag, and voltage-dependent limits.

    :efd1: Exciter voltage at which exciter saturation is defined (Efd1).  Typical Value = 3.05. Default: 0.0
    :efd2: Exciter voltage at which exciter saturation is defined (Efd2).  Typical Value = 2.29. Default: 0.0
    :exclim: (exclim).  IEEE standard is ambiguous about lower limit on exciter output. true = a lower limit of zero is applied to integrator output false = a lower limit of zero is not applied to integrator output. Typical Value = true. Default: False
    :ka: Voltage regulator gain (Ka).  Typical Value = 300. Default: 0.0
    :ke: Exciter constant related to self-excited field (Ke).  If Ke is entered as zero, the model calculates an effective value of Ke such that the initial condition value of Vr is zero. The zero value of Ke is not changed.  If Ke is entered as non-zero, its value is used directly, without change.  Typical Value = 1. Default: 0.0
    :kf: Excitation control system stabilizer gain (Kf).  Typical Value = 0.1. Default: 0.0
    :ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0. Default: 0.0
    :seefd1: Exciter saturation function value at the corresponding exciter voltage, Efd1 (Se[Eefd1]).  Typical Value = 0.279. Default: 0.0
    :seefd2: Exciter saturation function value at the corresponding exciter voltage, Efd2 (Se[Efd2]).  Typical Value = 0.117. Default: 0.0
    :ta: Voltage regulator time constant (Ta).  Typical Value = 0.01. Default: 0.0
    :tb: Voltage regulator time constant (Tb).  Typical Value = 0. Default: 0.0
    :tc: Voltage regulator time constant (Tc).  Typical Value = 0. Default: 0.0
    :te: Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 1.33. Default: 0.0
    :tf: Excitation control system stabilizer time constant (Tf).  Typical Value = 0.675. Default: 0.0
    :tf1: Excitation control system stabilizer time constant (Tf1).  Typical Value = 0. Default: 0.0
    :vrmax: Maximum voltage regulator output (Vrmax).  Typical Value = 4.95. Default: 0.0
    :vrmin: Minimum voltage regulator output (Vrmin).  Typical Value = -4.9. Default: 0.0
    :vtlim: (Vtlim). true = limiter at the block [Ka/(1+sTa)] is dependent on Vt  false = limiter at the block is not dependent on Vt. Typical Value = true. Default: False
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "efd1": [Profile.DY.value, ],
        "efd2": [Profile.DY.value, ],
        "exclim": [Profile.DY.value, ],
        "ka": [Profile.DY.value, ],
        "ke": [Profile.DY.value, ],
        "kf": [Profile.DY.value, ],
        "ks": [Profile.DY.value, ],
        "seefd1": [Profile.DY.value, ],
        "seefd2": [Profile.DY.value, ],
        "ta": [Profile.DY.value, ],
        "tb": [Profile.DY.value, ],
        "tc": [Profile.DY.value, ],
        "te": [Profile.DY.value, ],
        "tf": [Profile.DY.value, ],
        "tf1": [Profile.DY.value, ],
        "vrmax": [Profile.DY.value, ],
        "vrmin": [Profile.DY.value, ],
        "vtlim": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, efd1 = 0.0, efd2 = 0.0, exclim = False, ka = 0.0, ke = 0.0, kf = 0.0, ks = 0.0, seefd1 = 0.0, seefd2 = 0.0, ta = 0.0, tb = 0.0, tc = 0.0, te = 0.0, tf = 0.0, tf1 = 0.0, vrmax = 0.0, vrmin = 0.0, vtlim = False, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.efd1 = efd1
        self.efd2 = efd2
        self.exclim = exclim
        self.ka = ka
        self.ke = ke
        self.kf = kf
        self.ks = ks
        self.seefd1 = seefd1
        self.seefd2 = seefd2
        self.ta = ta
        self.tb = tb
        self.tc = tc
        self.te = te
        self.tf = tf
        self.tf1 = tf1
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.vtlim = vtlim

    def __str__(self):
        str = "class=ExcDC2A\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
