from .EquivalentEquipment import EquivalentEquipment
from .CGMESProfile import Profile


class EquivalentInjection(EquivalentEquipment):
    """
    This class represents equivalent injections (generation or load).  Voltage regulation is allowed only at the point of connection.

    :ReactiveCapabilityCurve: The equivalent injection using this reactive capability curve. Default: None
    :maxP: Maximum active power of the injection. Default: 0.0
    :maxQ: Used for modeling of infeed for load flow exchange. Not used for short circuit modeling.  If maxQ and minQ are not used ReactiveCapabilityCurve can be used. Default: 0.0
    :minP: Minimum active power of the injection. Default: 0.0
    :minQ: Used for modeling of infeed for load flow exchange. Not used for short circuit modeling.  If maxQ and minQ are not used ReactiveCapabilityCurve can be used. Default: 0.0
    :p: Equivalent active power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for steady state solutions. Default: 0.0
    :q: Equivalent reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for steady state solutions. Default: 0.0
    :r: Positive sequence resistance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of network reduction prior to the data exchange. Default: 0.0
    :r0: Zero sequence resistance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of network reduction prior to the data exchange. Default: 0.0
    :r2: Negative sequence resistance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of network reduction prior to the data exchange. Default: 0.0
    :regulationCapability: Specifies whether or not the EquivalentInjection has the capability to regulate the local voltage. Default: False
    :regulationStatus: Specifies the default regulation status of the EquivalentInjection.  True is regulating.  False is not regulating. Default: False
    :regulationTarget: The target voltage for voltage regulation. Default: 0.0
    :x: Positive sequence reactance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of network reduction prior to the data exchange. Default: 0.0
    :x0: Zero sequence reactance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of network reduction prior to the data exchange. Default: 0.0
    :x2: Negative sequence reactance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of network reduction prior to the data exchange. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, Profile.SSH.value, ],
        "ReactiveCapabilityCurve": [Profile.EQ.value, ],
        "maxP": [Profile.EQ.value, ],
        "maxQ": [Profile.EQ.value, ],
        "minP": [Profile.EQ.value, ],
        "minQ": [Profile.EQ.value, ],
        "p": [Profile.SSH.value, ],
        "q": [Profile.SSH.value, ],
        "r": [Profile.EQ.value, ],
        "r0": [Profile.EQ.value, ],
        "r2": [Profile.EQ.value, ],
        "regulationCapability": [Profile.EQ.value, ],
        "regulationStatus": [Profile.SSH.value, ],
        "regulationTarget": [Profile.SSH.value, ],
        "x": [Profile.EQ.value, ],
        "x0": [Profile.EQ.value, ],
        "x2": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class EquivalentEquipment:\n" + EquivalentEquipment.__doc__

    def __init__(self, ReactiveCapabilityCurve = None, maxP = 0.0, maxQ = 0.0, minP = 0.0, minQ = 0.0, p = 0.0, q = 0.0, r = 0.0, r0 = 0.0, r2 = 0.0, regulationCapability = False, regulationStatus = False, regulationTarget = 0.0, x = 0.0, x0 = 0.0, x2 = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ReactiveCapabilityCurve = ReactiveCapabilityCurve
        self.maxP = maxP
        self.maxQ = maxQ
        self.minP = minP
        self.minQ = minQ
        self.p = p
        self.q = q
        self.r = r
        self.r0 = r0
        self.r2 = r2
        self.regulationCapability = regulationCapability
        self.regulationStatus = regulationStatus
        self.regulationTarget = regulationTarget
        self.x = x
        self.x0 = x0
        self.x2 = x2

    def __str__(self):
        str = "class=EquivalentInjection\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
