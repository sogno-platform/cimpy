from .ConductingEquipment import ConductingEquipment
from .CGMESProfile import Profile


class EnergyConsumer(ConductingEquipment):
    """
    Generic user of energy - a  point of consumption on the power system model.

    :LoadDynamics: Load dynamics model used to describe dynamic behavior of this energy consumer. Default: None
    :LoadResponse: The load response characteristic of this load.  If missing, this load is assumed to be constant power. Default: None
    :p: Active power of the load. Load sign convention is used, i.e. positive sign means flow out from a node. For voltage dependent loads the value is at rated voltage. Starting value for a steady state solution. Default: 0.0
    :pfixed: Active power of the load that is a fixed quantity. Load sign convention is used, i.e. positive sign means flow out from a node. Default: 0.0
    :pfixedPct: Fixed active power as per cent of load group fixed active power. Load sign convention is used, i.e. positive sign means flow out from a node. Default: 0.0
    :q: Reactive power of the load. Load sign convention is used, i.e. positive sign means flow out from a node. For voltage dependent loads the value is at rated voltage. Starting value for a steady state solution. Default: 0.0
    :qfixed: Reactive power of the load that is a fixed quantity. Load sign convention is used, i.e. positive sign means flow out from a node. Default: 0.0
    :qfixedPct: Fixed reactive power as per cent of load group fixed reactive power. Load sign convention is used, i.e. positive sign means flow out from a node. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, Profile.EQ.value, Profile.SSH.value, ],
        "LoadDynamics": [Profile.DY.value, ],
        "LoadResponse": [Profile.EQ.value, ],
        "p": [Profile.SSH.value, ],
        "pfixed": [Profile.EQ.value, ],
        "pfixedPct": [Profile.EQ.value, ],
        "q": [Profile.SSH.value, ],
        "qfixed": [Profile.EQ.value, ],
        "qfixedPct": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class ConductingEquipment:\n" + ConductingEquipment.__doc__

    def __init__(self, LoadDynamics = None, LoadResponse = None, p = 0.0, pfixed = 0.0, pfixedPct = 0.0, q = 0.0, qfixed = 0.0, qfixedPct = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.LoadDynamics = LoadDynamics
        self.LoadResponse = LoadResponse
        self.p = p
        self.pfixed = pfixed
        self.pfixedPct = pfixedPct
        self.q = q
        self.qfixed = qfixed
        self.qfixedPct = qfixedPct

    def __str__(self):
        str = "class=EnergyConsumer\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
