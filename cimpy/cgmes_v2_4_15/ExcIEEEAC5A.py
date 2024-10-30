from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcIEEEAC5A(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type AC5A model. The model represents a simplified model for brushless excitation systems. The regulator is supplied from a source, such as a permanent magnet generator, which is not affected by system disturbances.  Unlike other ac models, this model uses loaded rather than open circuit exciter saturation data in the same way as it is used for the dc models.  Because the model has been widely implemented by the industry, it is sometimes used to represent other types of systems when either detailed data for them are not available or simplified models are required.   Reference: IEEE Standard 421.5-2005 Section 6.5.

    :efd1: Exciter voltage at which exciter saturation is defined (E).  Typical Value = 5.6. Default: 0.0
    :efd2: Exciter voltage at which exciter saturation is defined (E).  Typical Value = 4.2. Default: 0.0
    :ka: Voltage regulator gain (K).  Typical Value = 400. Default: 0.0
    :ke: Exciter constant related to self-excited field (K).  Typical Value = 1. Default: 0.0
    :kf: Excitation control system stabilizer gains (K).  Typical Value = 0.03. Default: 0.0
    :seefd1: Exciter saturation function value at the corresponding exciter voltage, E (S[E]).  Typical Value = 0.86. Default: 0.0
    :seefd2: Exciter saturation function value at the corresponding exciter voltage, E (S[E]).  Typical Value = 0.5. Default: 0.0
    :ta: Voltage regulator time constant (T).  Typical Value = 0.02. Default: 0.0
    :te: Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 0.8. Default: 0.0
    :tf1: Excitation control system stabilizer time constant (T).  Typical Value = 1. Default: 0.0
    :tf2: Excitation control system stabilizer time constant (T).  Typical Value = 1. Default: 0.0
    :tf3: Excitation control system stabilizer time constant (T).  Typical Value = 1. Default: 0.0
    :vrmax: Maximum voltage regulator output (V).  Typical Value = 7.3. Default: 0.0
    :vrmin: Minimum voltage regulator output (V).  Typical Value = -7.3. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "efd1": [Profile.DY.value, ],
        "efd2": [Profile.DY.value, ],
        "ka": [Profile.DY.value, ],
        "ke": [Profile.DY.value, ],
        "kf": [Profile.DY.value, ],
        "seefd1": [Profile.DY.value, ],
        "seefd2": [Profile.DY.value, ],
        "ta": [Profile.DY.value, ],
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

    def __init__(self, efd1 = 0.0, efd2 = 0.0, ka = 0.0, ke = 0.0, kf = 0.0, seefd1 = 0.0, seefd2 = 0.0, ta = 0.0, te = 0.0, tf1 = 0.0, tf2 = 0.0, tf3 = 0.0, vrmax = 0.0, vrmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.efd1 = efd1
        self.efd2 = efd2
        self.ka = ka
        self.ke = ke
        self.kf = kf
        self.seefd1 = seefd1
        self.seefd2 = seefd2
        self.ta = ta
        self.te = te
        self.tf1 = tf1
        self.tf2 = tf2
        self.tf3 = tf3
        self.vrmax = vrmax
        self.vrmin = vrmin

    def __str__(self):
        str = "class=ExcIEEEAC5A\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
