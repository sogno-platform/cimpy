from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcAC5A(ExcitationSystemDynamics):
    """
    Modified IEEE AC5A alternator-supplied rectifier excitation system with different minimum controller output.

    :a: Coefficient to allow different usage of the model (a).  Typical Value = 1. Default: 0.0
    :efd1: Exciter voltage at which exciter saturation is defined (Efd1).  Typical Value = 5.6. Default: 0.0
    :efd2: Exciter voltage at which exciter saturation is defined (Efd2).  Typical Value = 4.2. Default: 0.0
    :ka: Voltage regulator gain (Ka).  Typical Value = 400. Default: 0.0
    :ke: Exciter constant related to self-excited field (Ke).  Typical Value = 1. Default: 0.0
    :kf: Excitation control system stabilizer gains (Kf).  Typical Value = 0.03. Default: 0.0
    :ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0. Default: 0.0
    :seefd1: Exciter saturation function value at the corresponding exciter voltage, Efd1 (S[Efd1]).  Typical Value = 0.86. Default: 0.0
    :seefd2: Exciter saturation function value at the corresponding exciter voltage, Efd2 (S[Efd2]).  Typical Value = 0.5. Default: 0.0
    :ta: Voltage regulator time constant (Ta).  Typical Value = 0.02. Default: 0.0
    :tb: Voltage regulator time constant (Tb).  Typical Value = 0. Default: 0.0
    :tc: Voltage regulator time constant (Tc).  Typical Value = 0. Default: 0.0
    :te: Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 0.8. Default: 0.0
    :tf1: Excitation control system stabilizer time constant (Tf1).  Typical Value  = 1. Default: 0.0
    :tf2: Excitation control system stabilizer time constant (Tf2).  Typical Value = 0.8. Default: 0.0
    :tf3: Excitation control system stabilizer time constant (Tf3).  Typical Value = 0. Default: 0.0
    :vrmax: Maximum voltage regulator output (Vrmax).  Typical Value = 7.3. Default: 0.0
    :vrmin: Minimum voltage regulator output (Vrmin).  Typical Value =-7.3. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "a": [Profile.DY.value, ],
        "efd1": [Profile.DY.value, ],
        "efd2": [Profile.DY.value, ],
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
        "tf1": [Profile.DY.value, ],
        "tf2": [Profile.DY.value, ],
        "tf3": [Profile.DY.value, ],
        "vrmax": [Profile.DY.value, ],
        "vrmin": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, a = 0.0, efd1 = 0.0, efd2 = 0.0, ka = 0.0, ke = 0.0, kf = 0.0, ks = 0.0, seefd1 = 0.0, seefd2 = 0.0, ta = 0.0, tb = 0.0, tc = 0.0, te = 0.0, tf1 = 0.0, tf2 = 0.0, tf3 = 0.0, vrmax = 0.0, vrmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.a = a
        self.efd1 = efd1
        self.efd2 = efd2
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
        self.tf1 = tf1
        self.tf2 = tf2
        self.tf3 = tf3
        self.vrmax = vrmax
        self.vrmin = vrmin

    def __str__(self):
        str = "class=ExcAC5A\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
