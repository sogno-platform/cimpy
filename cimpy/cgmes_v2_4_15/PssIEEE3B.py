from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics
from .CGMESProfile import Profile


class PssIEEE3B(PowerSystemStabilizerDynamics):
    """
    The class represents IEEE Std 421.5-2005 type PSS3B power system stabilizer model. The PSS model PSS3B has dual inputs of electrical power and rotor angular frequency deviation. The signals are used to derive an equivalent mechanical power signal.  Reference: IEEE 3B 421.5-2005 Section 8.3.

    :a1: Notch filter parameter (A1).  Typical Value = 0.359. Default: 0.0
    :a2: Notch filter parameter (A2).  Typical Value = 0.586. Default: 0.0
    :a3: Notch filter parameter (A3).  Typical Value = 0.429. Default: 0.0
    :a4: Notch filter parameter (A4).  Typical Value = 0.564. Default: 0.0
    :a5: Notch filter parameter (A5).  Typical Value = 0.001. Default: 0.0
    :a6: Notch filter parameter (A6).  Typical Value = 0. Default: 0.0
    :a7: Notch filter parameter (A7).  Typical Value = 0.031. Default: 0.0
    :a8: Notch filter parameter (A8).  Typical Value = 0. Default: 0.0
    :inputSignal1Type: Type of input signal #1.  Typical Value = generatorElectricalPower. Default: None
    :inputSignal2Type: Type of input signal #2.  Typical Value = rotorSpeed. Default: None
    :ks1: Gain on signal # 1 (Ks1).  Typical Value = -0.602. Default: 0.0
    :ks2: Gain on signal # 2 (Ks2).  Typical Value = 30.12. Default: 0.0
    :t1: Transducer time constant (T1).  Typical Value = 0.012. Default: 0.0
    :t2: Transducer time constant (T2).  Typical Value = 0.012. Default: 0.0
    :tw1: Washout time constant (Tw1).  Typical Value = 0.3. Default: 0.0
    :tw2: Washout time constant (Tw2).  Typical Value = 0.3. Default: 0.0
    :tw3: Washout time constant (Tw3).  Typical Value = 0.6. Default: 0.0
    :vstmax: Stabilizer output max limit (Vstmax).  Typical Value = 0.1. Default: 0.0
    :vstmin: Stabilizer output min limit (Vstmin).  Typical Value = -0.1. Default: 0.0
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
        "inputSignal1Type": [Profile.DY.value, ],
        "inputSignal2Type": [Profile.DY.value, ],
        "ks1": [Profile.DY.value, ],
        "ks2": [Profile.DY.value, ],
        "t1": [Profile.DY.value, ],
        "t2": [Profile.DY.value, ],
        "tw1": [Profile.DY.value, ],
        "tw2": [Profile.DY.value, ],
        "tw3": [Profile.DY.value, ],
        "vstmax": [Profile.DY.value, ],
        "vstmin": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class PowerSystemStabilizerDynamics:\n" + PowerSystemStabilizerDynamics.__doc__

    def __init__(self, a1 = 0.0, a2 = 0.0, a3 = 0.0, a4 = 0.0, a5 = 0.0, a6 = 0.0, a7 = 0.0, a8 = 0.0, inputSignal1Type = None, inputSignal2Type = None, ks1 = 0.0, ks2 = 0.0, t1 = 0.0, t2 = 0.0, tw1 = 0.0, tw2 = 0.0, tw3 = 0.0, vstmax = 0.0, vstmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.a6 = a6
        self.a7 = a7
        self.a8 = a8
        self.inputSignal1Type = inputSignal1Type
        self.inputSignal2Type = inputSignal2Type
        self.ks1 = ks1
        self.ks2 = ks2
        self.t1 = t1
        self.t2 = t2
        self.tw1 = tw1
        self.tw2 = tw2
        self.tw3 = tw3
        self.vstmax = vstmax
        self.vstmin = vstmin

    def __str__(self):
        str = "class=PssIEEE3B\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
