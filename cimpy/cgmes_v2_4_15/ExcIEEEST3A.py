from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcIEEEST3A(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type ST3A model.  Some static systems utilize a field voltage control loop to linearize the exciter control characteristic. This also makes the output independent of supply source variations until supply limitations are reached.  These systems utilize a variety of controlled-rectifier designs: full thyristor complements or hybrid bridges in either series or shunt configurations. The power source may consist of only a potential source, either fed from the machine terminals or from internal windings. Some designs may have compound power sources utilizing both machine potential and current. These power sources are represented as phasor combinations of machine terminal current and voltage and are accommodated by suitable parameters in model Type ST3A which is represented by ExcIEEEST3A.   Reference: IEEE Standard 421.5-2005 Section 7.3.

    :ka: Voltage regulator gain (K). This is parameter K in the IEEE Std. Typical Value = 200. Default: 0.0
    :kc: Rectifier loading factor proportional to commutating reactance (K). Typical Value = 0.2. Default: 0.0
    :kg: Feedback gain constant of the inner loop field regulator (K).  Typical Value = 1. Default: 0.0
    :ki: Potential circuit gain coefficient (K).  Typical Value = 0. Default: 0.0
    :km: Forward gain constant of the inner loop field regulator (K).  Typical Value = 7.93. Default: 0.0
    :kp: Potential circuit gain coefficient (K).  Typical Value = 6.15. Default: 0.0
    :ta: Voltage regulator time constant (T).  Typical Value = 0. Default: 0.0
    :tb: Voltage regulator time constant (T).  Typical Value = 10. Default: 0.0
    :tc: Voltage regulator time constant (T).  Typical Value = 1. Default: 0.0
    :thetap: Potential circuit phase angle (thetap).  Typical Value = 0. Default: 0.0
    :tm: Forward time constant of inner loop field regulator (T).  Typical Value = 0.4. Default: 0.0
    :vbmax: Maximum excitation voltage (V).  Typical Value = 6.9. Default: 0.0
    :vgmax: Maximum inner loop feedback voltage (V).  Typical Value = 5.8. Default: 0.0
    :vimax: Maximum voltage regulator input limit (V).  Typical Value = 0.2. Default: 0.0
    :vimin: Minimum voltage regulator input limit (V).  Typical Value = -0.2. Default: 0.0
    :vmmax: Maximum inner loop output (V).  Typical Value = 1. Default: 0.0
    :vmmin: Minimum inner loop output (V).  Typical Value = 0. Default: 0.0
    :vrmax: Maximum voltage regulator output (V).  Typical Value = 10. Default: 0.0
    :vrmin: Minimum voltage regulator output (V).  Typical Value = -10. Default: 0.0
    :xl: Reactance associated with potential source (X).  Typical Value = 0.081. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "ka": [Profile.DY.value, ],
        "kc": [Profile.DY.value, ],
        "kg": [Profile.DY.value, ],
        "ki": [Profile.DY.value, ],
        "km": [Profile.DY.value, ],
        "kp": [Profile.DY.value, ],
        "ta": [Profile.DY.value, ],
        "tb": [Profile.DY.value, ],
        "tc": [Profile.DY.value, ],
        "thetap": [Profile.DY.value, ],
        "tm": [Profile.DY.value, ],
        "vbmax": [Profile.DY.value, ],
        "vgmax": [Profile.DY.value, ],
        "vimax": [Profile.DY.value, ],
        "vimin": [Profile.DY.value, ],
        "vmmax": [Profile.DY.value, ],
        "vmmin": [Profile.DY.value, ],
        "vrmax": [Profile.DY.value, ],
        "vrmin": [Profile.DY.value, ],
        "xl": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, ka = 0.0, kc = 0.0, kg = 0.0, ki = 0.0, km = 0.0, kp = 0.0, ta = 0.0, tb = 0.0, tc = 0.0, thetap = 0.0, tm = 0.0, vbmax = 0.0, vgmax = 0.0, vimax = 0.0, vimin = 0.0, vmmax = 0.0, vmmin = 0.0, vrmax = 0.0, vrmin = 0.0, xl = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ka = ka
        self.kc = kc
        self.kg = kg
        self.ki = ki
        self.km = km
        self.kp = kp
        self.ta = ta
        self.tb = tb
        self.tc = tc
        self.thetap = thetap
        self.tm = tm
        self.vbmax = vbmax
        self.vgmax = vgmax
        self.vimax = vimax
        self.vimin = vimin
        self.vmmax = vmmax
        self.vmmin = vmmin
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.xl = xl

    def __str__(self):
        str = "class=ExcIEEEST3A\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
