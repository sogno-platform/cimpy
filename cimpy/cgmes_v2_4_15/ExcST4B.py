from .ExcitationSystemDynamics import ExcitationSystemDynamics
from .CGMESProfile import Profile


class ExcST4B(ExcitationSystemDynamics):
    """
    Modified IEEE ST4B static excitation system with maximum inner loop feedback gain .

    :kc: Rectifier loading factor proportional to commutating reactance (Kc). Typical Value = 0.113. Default: 0.0
    :kg: Feedback gain constant of the inner loop field regulator (Kg). Typical Value = 0. Default: 0.0
    :ki: Potential circuit gain coefficient (Ki).  Typical Value = 0. Default: 0.0
    :kim: Voltage regulator integral gain output (Kim).  Typical Value = 0. Default: 0.0
    :kir: Voltage regulator integral gain (Kir).  Typical Value = 10.75. Default: 0.0
    :kp: Potential circuit gain coefficient (Kp).  Typical Value = 9.3. Default: 0.0
    :kpm: Voltage regulator proportional gain output (Kpm).  Typical Value = 1. Default: 0.0
    :kpr: Voltage regulator proportional gain (Kpr).  Typical Value = 10.75. Default: 0.0
    :lvgate: Selector (LVgate). true = LVgate is part of the block diagram false = LVgate is not part of the block diagram.  Typical Value = false. Default: False
    :ta: Voltage regulator time constant (Ta).  Typical Value = 0.02. Default: 0.0
    :thetap: Potential circuit phase angle (thetap).  Typical Value = 0. Default: 0.0
    :uel: Selector (Uel). true = UEL is part of block diagram false = UEL is not part of block diagram.  Typical Value = false. Default: False
    :vbmax: Maximum excitation voltage (Vbmax).  Typical Value = 11.63. Default: 0.0
    :vgmax: Maximum inner loop feedback voltage (Vgmax).  Typical Value = 5.8. Default: 0.0
    :vmmax: Maximum inner loop output (Vmmax).  Typical Value = 99. Default: 0.0
    :vmmin: Minimum inner loop output (Vmmin).  Typical Value = -99. Default: 0.0
    :vrmax: Maximum voltage regulator output (Vrmax).  Typical Value = 1. Default: 0.0
    :vrmin: Minimum voltage regulator output (Vrmin).  Typical Value = -0.87. Default: 0.0
    :xl: Reactance associated with potential source (Xl).  Typical Value = 0.124. Default: 0.0
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
        "lvgate": [Profile.DY.value, ],
        "ta": [Profile.DY.value, ],
        "thetap": [Profile.DY.value, ],
        "uel": [Profile.DY.value, ],
        "vbmax": [Profile.DY.value, ],
        "vgmax": [Profile.DY.value, ],
        "vmmax": [Profile.DY.value, ],
        "vmmin": [Profile.DY.value, ],
        "vrmax": [Profile.DY.value, ],
        "vrmin": [Profile.DY.value, ],
        "xl": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class ExcitationSystemDynamics:\n" + ExcitationSystemDynamics.__doc__

    def __init__(self, kc = 0.0, kg = 0.0, ki = 0.0, kim = 0.0, kir = 0.0, kp = 0.0, kpm = 0.0, kpr = 0.0, lvgate = False, ta = 0.0, thetap = 0.0, uel = False, vbmax = 0.0, vgmax = 0.0, vmmax = 0.0, vmmin = 0.0, vrmax = 0.0, vrmin = 0.0, xl = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.kc = kc
        self.kg = kg
        self.ki = ki
        self.kim = kim
        self.kir = kir
        self.kp = kp
        self.kpm = kpm
        self.kpr = kpr
        self.lvgate = lvgate
        self.ta = ta
        self.thetap = thetap
        self.uel = uel
        self.vbmax = vbmax
        self.vgmax = vgmax
        self.vmmax = vmmax
        self.vmmin = vmmin
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.xl = xl

    def __str__(self):
        str = "class=ExcST4B\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
