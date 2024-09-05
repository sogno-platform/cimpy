from .ACDCConverter import ACDCConverter


class VsConverter(ACDCConverter):
    """
    DC side of the voltage source converter (VSC).

    :VSCDynamics: Voltage source converter dynamics model used to describe dynamic behaviour of this converter. Default: None
    :droop: Droop constant. The pu value is obtained as D [kV/MW] x Sb / Ubdc. The attribute shall be a positive value. Default: 0.0
    :droopCompensation: Compensation constant. Used to compensate for voltage drop when controlling voltage at a distant bus. The attribute shall be a positive value. Default: 0.0
    :pPccControl: Kind of control of real power and/or DC voltage. Default: None
    :qPccControl: Kind of reactive power control. Default: None
    :qShare: Reactive power sharing factor among parallel converters on Uac control. The attribute shall be a positive value or zero. Default: 0.0
    :targetQpcc: Reactive power injection target in AC grid, at point of common coupling.  Load sign convention is used, i.e. positive sign means flow out from a node. Default: 0.0
    :targetUpcc: Voltage target in AC grid, at point of common coupling. The attribute shall be a positive value. Default: 0.0
    :targetPowerFactorPcc: Power factor target at the AC side, at point of common coupling. The attribute shall be a positive value. Default: 0.0
    :targetPhasePcc: Phase target at AC side, at point of common coupling. The attribute shall be a positive value. Default: 0.0
    :targetPWMfactor: Magnitude of pulse-modulation factor. The attribute shall be a positive value. Default: 0.0
    :CapabilityCurve: Capability curve of this converter. Default: None
    :maxModulationIndex: The maximum quotient between the AC converter voltage (Uc) and DC voltage (Ud). A factor typically less than 1. It is converter`s configuration data used in power flow. Default: 0.0
    :delta: Angle between VsConverter.uv and ACDCConverter.uc. It is converter`s state variable used in power flow. The attribute shall be a positive value or zero. Default: 0.0
    :uv: Line-to-line voltage on the valve side of the converter transformer. It is converter`s state variable, result from power flow. The attribute shall be a positive value. Default: 0.0
    """

    cgmesProfile = ACDCConverter.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
            cgmesProfile.SV.value,
        ],
        "VSCDynamics": [
            cgmesProfile.DY.value,
        ],
        "droop": [
            cgmesProfile.SSH.value,
        ],
        "droopCompensation": [
            cgmesProfile.SSH.value,
        ],
        "pPccControl": [
            cgmesProfile.SSH.value,
        ],
        "qPccControl": [
            cgmesProfile.SSH.value,
        ],
        "qShare": [
            cgmesProfile.SSH.value,
        ],
        "targetQpcc": [
            cgmesProfile.SSH.value,
        ],
        "targetUpcc": [
            cgmesProfile.SSH.value,
        ],
        "targetPowerFactorPcc": [
            cgmesProfile.SSH.value,
        ],
        "targetPhasePcc": [
            cgmesProfile.SSH.value,
        ],
        "targetPWMfactor": [
            cgmesProfile.SSH.value,
        ],
        "CapabilityCurve": [
            cgmesProfile.EQ.value,
        ],
        "maxModulationIndex": [
            cgmesProfile.EQ.value,
        ],
        "delta": [
            cgmesProfile.SV.value,
        ],
        "uv": [
            cgmesProfile.SV.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class ACDCConverter: \n" + ACDCConverter.__doc__
    )

    def __init__(
        self,
        VSCDynamics=None,
        droop=0.0,
        droopCompensation=0.0,
        pPccControl=None,
        qPccControl=None,
        qShare=0.0,
        targetQpcc=0.0,
        targetUpcc=0.0,
        targetPowerFactorPcc=0.0,
        targetPhasePcc=0.0,
        targetPWMfactor=0.0,
        CapabilityCurve=None,
        maxModulationIndex=0.0,
        delta=0.0,
        uv=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.VSCDynamics = VSCDynamics
        self.droop = droop
        self.droopCompensation = droopCompensation
        self.pPccControl = pPccControl
        self.qPccControl = qPccControl
        self.qShare = qShare
        self.targetQpcc = targetQpcc
        self.targetUpcc = targetUpcc
        self.targetPowerFactorPcc = targetPowerFactorPcc
        self.targetPhasePcc = targetPhasePcc
        self.targetPWMfactor = targetPWMfactor
        self.CapabilityCurve = CapabilityCurve
        self.maxModulationIndex = maxModulationIndex
        self.delta = delta
        self.uv = uv

    def __str__(self):
        str = "class=VsConverter\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
