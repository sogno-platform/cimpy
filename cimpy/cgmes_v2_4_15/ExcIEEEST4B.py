from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcIEEEST4B(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type ST4B model. This model is a variation of the Type ST3A model, with a proportional plus integral (PI) regulator block replacing the lag-lead regulator characteristic that is in the ST3A model. Both potential and compound source rectifier excitation systems are modeled.  The PI regulator blocks have non-windup limits that are represented. The voltage regulator of this model is typically implemented digitally.  Reference: IEEE Standard 421.5-2005 Section 7.4.

    :kc: Rectifier loading factor proportional to commutating reactance (K). Typical Value = 0.113. Default: 0.0
    :kg: Feedback gain constant of the inner loop field regulator (K).  Typical Value = 0. Default: 0.0
    :ki: Potential circuit gain coefficient (K).  Typical Value = 0. Default: 0.0
    :kim: Voltage regulator integral gain output (K).  Typical Value = 0. Default: 0.0
    :kir: Voltage regulator integral gain (K).  Typical Value = 10.75. Default: 0.0
    :kp: Potential circuit gain coefficient (K).  Typical Value = 9.3. Default: 0.0
    :kpm: Voltage regulator proportional gain output (K).  Typical Value = 1. Default: 0.0
    :kpr: Voltage regulator proportional gain (K).  Typical Value = 10.75. Default: 0.0
    :ta: Voltage regulator time constant (T).  Typical Value = 0.02. Default: 0.0
    :thetap: Potential circuit phase angle (thetap).  Typical Value = 0. Default: 0.0
    :vbmax: Maximum excitation voltage (V).  Typical Value = 11.63. Default: 0.0
    :vmmax: Maximum inner loop output (V).  Typical Value = 99. Default: 0.0
    :vmmin: Minimum inner loop output (V).  Typical Value = -99. Default: 0.0
    :vrmax: Maximum voltage regulator output (V).  Typical Value = 1. Default: 0.0
    :vrmin: Minimum voltage regulator output (V).  Typical Value = -0.87. Default: 0.0
    :xl: Reactance associated with potential source (X).  Typical Value = 0.124. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "kc": [Profile.DY.value, ],
        "kg": [Profile.DY.value, ],
        "ki": [Profile.DY.value, ],
        "kim": [Profile.DY.value, ],
        "kir": [Profile.DY.value, ],
        "kp": [Profile.DY.value, ],
        "kpm": [Profile.DY.value, ],
        "kpr": [Profile.DY.value, ],
        "ta": [Profile.DY.value, ],
        "thetap": [Profile.DY.value, ],
        "vbmax": [Profile.DY.value, ],
        "vmmax": [Profile.DY.value, ],
        "vmmin": [Profile.DY.value, ],
        "vrmax": [Profile.DY.value, ],
        "vrmin": [Profile.DY.value, ],
        "xl": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, kc = 0.0, kg = 0.0, ki = 0.0, kim = 0.0, kir = 0.0, kp = 0.0, kpm = 0.0, kpr = 0.0, ta = 0.0, thetap = 0.0, vbmax = 0.0, vmmax = 0.0, vmmin = 0.0, vrmax = 0.0, vrmin = 0.0, xl = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.kc = kc
        self.kg = kg
        self.ki = ki
        self.kim = kim
        self.kir = kir
        self.kp = kp
        self.kpm = kpm
        self.kpr = kpr
        self.ta = ta
        self.thetap = thetap
        self.vbmax = vbmax
        self.vmmax = vmmax
        self.vmmin = vmmin
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.xl = xl

    def __str__(self):
        str = "class=ExcIEEEST4B\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
