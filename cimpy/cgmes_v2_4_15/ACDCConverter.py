from .ConductingEquipment import ConductingEquipment
from .CGMESProfile import Profile


class ACDCConverter(ConductingEquipment):
    """
    A unit with valves for three phases, together with unit control equipment, essential protective and switching devices, DC storage capacitors, phase reactors and auxiliaries, if any, used for conversion.

    :DCTerminals:  Default: "list"
    :PccTerminal: All converters` DC sides linked to this point of common coupling terminal. Default: None
    :baseS: Base apparent power of the converter pole. Default: 0.0
    :idc: Converter DC current, also called Id. Converter state variable, result from power flow. Default: 0.0
    :idleLoss: Active power loss in pole at no power transfer. Converter configuration data used in power flow. Default: 0.0
    :maxUdc: The maximum voltage on the DC side at which the converter should operate. Converter configuration data used in power flow. Default: 0.0
    :minUdc: Min allowed converter DC voltage. Converter configuration data used in power flow. Default: 0.0
    :numberOfValves: Number of valves in the converter. Used in loss calculations. Default: 0
    :p: Active power at the point of common coupling. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution in the case a simplified power flow model is used. Default: 0.0
    :poleLossP: The active power loss at a DC Pole  = idleLoss + switchingLoss*|Idc| + resitiveLoss*Idc^2 For lossless operation Pdc=Pac For rectifier operation with losses Pdc=Pac-lossP For inverter operation with losses Pdc=Pac+lossP Converter state variable used in power flow. Default: 0.0
    :q: Reactive power at the point of common coupling. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution in the case a simplified power flow model is used. Default: 0.0
    :ratedUdc: Rated converter DC voltage, also called UdN. Converter configuration data used in power flow. Default: 0.0
    :resistiveLoss: Converter configuration data used in power flow. Refer to poleLossP. Default: 0.0
    :switchingLoss: Switching losses, relative to the base apparent power `baseS`. Refer to poleLossP. Default: 0.0
    :targetPpcc: Real power injection target in AC grid, at point of common coupling. Default: 0.0
    :targetUdc: Target value for DC voltage magnitude. Default: 0.0
    :uc: Converter voltage, the voltage at the AC side of the bridge. Converter state variable, result from power flow. Default: 0.0
    :udc: Converter voltage at the DC side, also called Ud. Converter state variable, result from power flow. Default: 0.0
    :valveU0: Valve threshold voltage. Forward voltage drop when the valve is conducting. Used in loss calculations, i.e. the switchLoss depend on numberOfValves * valveU0. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, Profile.SV.value, Profile.SSH.value, ],
        "DCTerminals": [Profile.EQ.value, ],
        "PccTerminal": [Profile.EQ.value, ],
        "baseS": [Profile.EQ.value, ],
        "idc": [Profile.SV.value, ],
        "idleLoss": [Profile.EQ.value, ],
        "maxUdc": [Profile.EQ.value, ],
        "minUdc": [Profile.EQ.value, ],
        "numberOfValves": [Profile.EQ.value, ],
        "p": [Profile.SSH.value, ],
        "poleLossP": [Profile.SV.value, ],
        "q": [Profile.SSH.value, ],
        "ratedUdc": [Profile.EQ.value, ],
        "resistiveLoss": [Profile.EQ.value, ],
        "switchingLoss": [Profile.EQ.value, ],
        "targetPpcc": [Profile.SSH.value, ],
        "targetUdc": [Profile.SSH.value, ],
        "uc": [Profile.SV.value, ],
        "udc": [Profile.SV.value, ],
        "valveU0": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class ConductingEquipment:\n" + ConductingEquipment.__doc__

    def __init__(self, DCTerminals = "list", PccTerminal = None, baseS = 0.0, idc = 0.0, idleLoss = 0.0, maxUdc = 0.0, minUdc = 0.0, numberOfValves = 0, p = 0.0, poleLossP = 0.0, q = 0.0, ratedUdc = 0.0, resistiveLoss = 0.0, switchingLoss = 0.0, targetPpcc = 0.0, targetUdc = 0.0, uc = 0.0, udc = 0.0, valveU0 = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.DCTerminals = DCTerminals
        self.PccTerminal = PccTerminal
        self.baseS = baseS
        self.idc = idc
        self.idleLoss = idleLoss
        self.maxUdc = maxUdc
        self.minUdc = minUdc
        self.numberOfValves = numberOfValves
        self.p = p
        self.poleLossP = poleLossP
        self.q = q
        self.ratedUdc = ratedUdc
        self.resistiveLoss = resistiveLoss
        self.switchingLoss = switchingLoss
        self.targetPpcc = targetPpcc
        self.targetUdc = targetUdc
        self.uc = uc
        self.udc = udc
        self.valveU0 = valveU0

    def __str__(self):
        str = "class=ACDCConverter\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
