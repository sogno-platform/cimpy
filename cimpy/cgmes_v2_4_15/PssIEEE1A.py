from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics
from .CGMESProfile import Profile


class PssIEEE1A(PowerSystemStabilizerDynamics):
    """
    The class represents IEEE Std 421.5-2005 type PSS1A power system stabilizer model. PSS1A is the generalized form of a PSS with a single input. Some common stabilizer input signals are speed, frequency, and power.  Reference: IEEE 1A 421.5-2005 Section 8.1.

    :a1: PSS signal conditioning frequency filter constant (A1).  Typical Value = 0.061. Default: 0.0
    :a2: PSS signal conditioning frequency filter constant (A2).  Typical Value = 0.0017. Default: 0.0
    :inputSignalType: Type of input signal.  Typical Value = rotorAngularFrequencyDeviation. Default: None
    :ks: Stabilizer gain (Ks).  Typical Value = 5. Default: 0.0
    :t1: Lead/lag time constant (T1).  Typical Value = 0.3. Default: 0.0
    :t2: Lead/lag time constant (T2).  Typical Value = 0.03. Default: 0.0
    :t3: Lead/lag time constant (T3).  Typical Value = 0.3. Default: 0.0
    :t4: Lead/lag time constant (T4).  Typical Value = 0.03. Default: 0.0
    :t5: Washout time constant (T5).  Typical Value = 10. Default: 0.0
    :t6: Transducer time constant (T6).  Typical Value = 0.01. Default: 0.0
    :vrmax: Maximum stabilizer output (Vrmax).  Typical Value = 0.05. Default: 0.0
    :vrmin: Minimum stabilizer output (Vrmin).  Typical Value = -0.05. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "a1": [Profile.DY.value, ],
        "a2": [Profile.DY.value, ],
        "inputSignalType": [Profile.DY.value, ],
        "ks": [Profile.DY.value, ],
        "t1": [Profile.DY.value, ],
        "t2": [Profile.DY.value, ],
        "t3": [Profile.DY.value, ],
        "t4": [Profile.DY.value, ],
        "t5": [Profile.DY.value, ],
        "t6": [Profile.DY.value, ],
        "vrmax": [Profile.DY.value, ],
        "vrmin": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class PowerSystemStabilizerDynamics:\n" + PowerSystemStabilizerDynamics.__doc__

    def __init__(self, a1 = 0.0, a2 = 0.0, inputSignalType = None, ks = 0.0, t1 = 0.0, t2 = 0.0, t3 = 0.0, t4 = 0.0, t5 = 0.0, t6 = 0.0, vrmax = 0.0, vrmin = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.a1 = a1
        self.a2 = a2
        self.inputSignalType = inputSignalType
        self.ks = ks
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t5 = t5
        self.t6 = t6
        self.vrmax = vrmax
        self.vrmin = vrmin

    def __str__(self):
        str = "class=PssIEEE1A\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
