from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics
from .CGMESProfile import Profile


class Pss1A(PowerSystemStabilizerDynamics):
    """
    Single input power system stabilizer. It is a modified version in order to allow representation of various vendors' implementations on PSS type 1A.

    :a1: Notch filter parameter (A1). Default: 0.0
    :a2: Notch filter parameter (A2). Default: 0.0
    :a3: Notch filter parameter (A3). Default: 0.0
    :a4: Notch filter parameter (A4). Default: 0.0
    :a5: Notch filter parameter (A5). Default: 0.0
    :a6: Notch filter parameter (A6). Default: 0.0
    :a7: Notch filter parameter (A7). Default: 0.0
    :a8: Notch filter parameter (A8). Default: 0.0
    :inputSignalType: Type of input signal. Default: None
    :kd: Selector (Kd).  true = e used false = e not used. Default: False
    :ks: Stabilizer gain (Ks). Default: 0.0
    :t1: Lead/lag time constant (T1). Default: 0.0
    :t2: Lead/lag time constant (T2). Default: 0.0
    :t3: Lead/lag time constant (T3). Default: 0.0
    :t4: Lead/lag time constant (T4). Default: 0.0
    :t5: Washout time constant (T5). Default: 0.0
    :t6: Transducer time constant (T6). Default: 0.0
    :tdelay: Time constant (Tdelay). Default: 0.0
    :vcl: Stabilizer input cutoff threshold (Vcl). Default: 0.0
    :vcu: Stabilizer input cutoff threshold (Vcu). Default: 0.0
    :vrmax: Maximum stabilizer output (Vrmax). Default: 0.0
    :vrmin: Minimum stabilizer output (Vrmin). Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "a1": [Profile.DY.value, ],
        "a2": [Profile.DY.value, ],
        "a3": [Profile.DY.value, ],
        "a4": [Profile.DY.value, ],
        "a5": [Profile.DY.value, ],
        "a6": [Profile.DY.value, ],
        "a7": [Profile.DY.value, ],
        "a8": [Profile.DY.value, ],
        "inputSignalType": [Profile.DY.value, ],
        "kd": [Profile.DY.value, ],
        "ks": [Profile.DY.value, ],
        "t1": [Profile.DY.value, ],
        "t2": [Profile.DY.value, ],
        "t3": [Profile.DY.value, ],
        "t4": [Profile.DY.value, ],
        "t5": [Profile.DY.value, ],
        "t6": [Profile.DY.value, ],
        "tdelay": [Profile.DY.value, ],
        "vcl": [Profile.DY.value, ],
        "vcu": [Profile.DY.value, ],
        "vrmax": [Profile.DY.value, ],
        "vrmin": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class PowerSystemStabilizerDynamics:\n" + PowerSystemStabilizerDynamics.__doc__

    def __init__(self, a1 = 0.0, a2 = 0.0, a3 = 0.0, a4 = 0.0, a5 = 0.0, a6 = 0.0, a7 = 0.0, a8 = 0.0, inputSignalType = None, kd = False, ks = 0.0, t1 = 0.0, t2 = 0.0, t3 = 0.0, t4 = 0.0, t5 = 0.0, t6 = 0.0, tdelay = 0.0, vcl = 0.0, vcu = 0.0, vrmax = 0.0, vrmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.a6 = a6
        self.a7 = a7
        self.a8 = a8
        self.inputSignalType = inputSignalType
        self.kd = kd
        self.ks = ks
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t5 = t5
        self.t6 = t6
        self.tdelay = tdelay
        self.vcl = vcl
        self.vcu = vcu
        self.vrmax = vrmax
        self.vrmin = vrmin

    def __str__(self):
        str = "class=Pss1A\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
