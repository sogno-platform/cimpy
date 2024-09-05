from .ConductingEquipment import ConductingEquipment


class ACDCConverter(ConductingEquipment):
    """
    A unit with valves for three phases, together with unit control equipment, essential protective and switching devices, DC storage capacitors, phase reactors and auxiliaries, if any, used for conversion.

    :p: Active power at the point of common coupling. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution in the case a simplified power flow model is used. Default: 0.0
    :q: Reactive power at the point of common coupling. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution in the case a simplified power flow model is used. Default: 0.0
    :targetPpcc: Real power injection target in AC grid, at point of common coupling.  Load sign convention is used, i.e. positive sign means flow out from a node. Default: 0.0
    :targetUdc: Target value for DC voltage magnitude. The attribute shall be a positive value. Default: 0.0
    :baseS: Base apparent power of the converter pole. The attribute shall be a positive value. Default: 0.0
    :idleLoss: Active power loss in pole at no power transfer. It is converter`s configuration data used in power flow. The attribute shall be a positive value. Default: 0.0
    :maxUdc: The maximum voltage on the DC side at which the converter should operate. It is converter`s configuration data used in power flow. The attribute shall be a positive value. Default: 0.0
    :minUdc: The minimum voltage on the DC side at which the converter should operate. It is converter`s configuration data used in power flow. The attribute shall be a positive value. Default: 0.0
    :numberOfValves: Number of valves in the converter. Used in loss calculations. Default: 0
    :ratedUdc: Rated converter DC voltage, also called UdN. The attribute shall be a positive value. It is converter`s configuration data used in power flow. For instance a bipolar HVDC link with value  200 kV has a 400kV difference between the dc lines. Default: 0.0
    :resistiveLoss: It is converter`s configuration data used in power flow. Refer to poleLossP. The attribute shall be a positive value. Default: 0.0
    :switchingLoss: Switching losses, relative to the base apparent power `baseS`. Refer to poleLossP. The attribute shall be a positive value. Default: 0.0
    :valveU0: Valve threshold voltage, also called Uvalve. Forward voltage drop when the valve is conducting. Used in loss calculations, i.e. the switchLoss depend on numberOfValves * valveU0. Default: 0.0
    :maxP: Maximum active power limit. The value is overwritten by values of VsCapabilityCurve, if present. Default: 0.0
    :minP: Minimum active power limit. The value is overwritten by values of VsCapabilityCurve, if present. Default: 0.0
    :PccTerminal: Point of common coupling terminal for this converter DC side. It is typically the terminal on the power transformer (or switch) closest to the AC network. Default: None
    :DCTerminals: A DC converter have DC converter terminals. A converter has two DC converter terminals. Default: "list"
    :idc: Converter DC current, also called Id. It is converter`s state variable, result from power flow. Default: 0.0
    :poleLossP: The active power loss at a DC Pole  = idleLoss + switchingLoss*|Idc| + resitiveLoss*Idc^2. For lossless operation Pdc=Pac. For rectifier operation with losses Pdc=Pac-lossP. For inverter operation with losses Pdc=Pac+lossP. It is converter`s state variable used in power flow. The attribute shall be a positive value. Default: 0.0
    :uc: Line-to-line converter voltage, the voltage at the AC side of the valve. It is converter`s state variable, result from power flow. The attribute shall be a positive value. Default: 0.0
    :udc: Converter voltage at the DC side, also called Ud. It is converter`s state variable, result from power flow. The attribute shall be a positive value. Default: 0.0
    """

    cgmesProfile = ConductingEquipment.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
            cgmesProfile.SV.value,
        ],
        "p": [
            cgmesProfile.SSH.value,
        ],
        "q": [
            cgmesProfile.SSH.value,
        ],
        "targetPpcc": [
            cgmesProfile.SSH.value,
        ],
        "targetUdc": [
            cgmesProfile.SSH.value,
        ],
        "baseS": [
            cgmesProfile.EQ.value,
        ],
        "idleLoss": [
            cgmesProfile.EQ.value,
        ],
        "maxUdc": [
            cgmesProfile.EQ.value,
        ],
        "minUdc": [
            cgmesProfile.EQ.value,
        ],
        "numberOfValves": [
            cgmesProfile.EQ.value,
        ],
        "ratedUdc": [
            cgmesProfile.EQ.value,
        ],
        "resistiveLoss": [
            cgmesProfile.EQ.value,
        ],
        "switchingLoss": [
            cgmesProfile.EQ.value,
        ],
        "valveU0": [
            cgmesProfile.EQ.value,
        ],
        "maxP": [
            cgmesProfile.EQ.value,
        ],
        "minP": [
            cgmesProfile.EQ.value,
        ],
        "PccTerminal": [
            cgmesProfile.EQ.value,
        ],
        "DCTerminals": [
            cgmesProfile.EQ.value,
        ],
        "idc": [
            cgmesProfile.SV.value,
        ],
        "poleLossP": [
            cgmesProfile.SV.value,
        ],
        "uc": [
            cgmesProfile.SV.value,
        ],
        "udc": [
            cgmesProfile.SV.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class ConductingEquipment: \n"
        + ConductingEquipment.__doc__
    )

    def __init__(
        self,
        p=0.0,
        q=0.0,
        targetPpcc=0.0,
        targetUdc=0.0,
        baseS=0.0,
        idleLoss=0.0,
        maxUdc=0.0,
        minUdc=0.0,
        numberOfValves=0,
        ratedUdc=0.0,
        resistiveLoss=0.0,
        switchingLoss=0.0,
        valveU0=0.0,
        maxP=0.0,
        minP=0.0,
        PccTerminal=None,
        DCTerminals="list",
        idc=0.0,
        poleLossP=0.0,
        uc=0.0,
        udc=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.p = p
        self.q = q
        self.targetPpcc = targetPpcc
        self.targetUdc = targetUdc
        self.baseS = baseS
        self.idleLoss = idleLoss
        self.maxUdc = maxUdc
        self.minUdc = minUdc
        self.numberOfValves = numberOfValves
        self.ratedUdc = ratedUdc
        self.resistiveLoss = resistiveLoss
        self.switchingLoss = switchingLoss
        self.valveU0 = valveU0
        self.maxP = maxP
        self.minP = minP
        self.PccTerminal = PccTerminal
        self.DCTerminals = DCTerminals
        self.idc = idc
        self.poleLossP = poleLossP
        self.uc = uc
        self.udc = udc

    def __str__(self):
        str = "class=ACDCConverter\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
