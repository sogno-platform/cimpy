from .ACDCConverter import ACDCConverter
from .CGMESProfile import Profile


class VsConverter(ACDCConverter):
    """
    DC side of the voltage source converter (VSC).

    :CapabilityCurve: All converters with this capability curve. Default: None
    :delta: Angle between uf and uc. Converter state variable used in power flow. Default: 0.0
    :droop: Droop constant; pu value is obtained as D [kV^2 / MW] x Sb / Ubdc^2. Default: 0.0
    :droopCompensation: Compensation (resistance) constant. Used to compensate for voltage drop when controlling voltage at a distant bus. Default: 0.0
    :maxModulationIndex: The max quotient between the AC converter voltage (Uc) and DC voltage (Ud). A factor typically less than 1. VSC configuration data used in power flow. Default: 0.0
    :maxValveCurrent: The maximum current through a valve. This current limit is the basis for calculating the capability diagram. VSC  configuration data. Default: 0.0
    :pPccControl: Kind of control of real power and/or DC voltage. Default: None
    :qPccControl:  Default: None
    :qShare: Reactive power sharing factor among parallel converters on Uac control. Default: 0.0
    :targetQpcc: Reactive power injection target in AC grid, at point of common coupling. Default: 0.0
    :targetUpcc: Voltage target in AC grid, at point of common coupling. Default: 0.0
    :uf: Filter bus voltage. Converter state variable, result from power flow. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, Profile.SV.value, Profile.SSH.value, ],
        "CapabilityCurve": [Profile.EQ.value, ],
        "delta": [Profile.SV.value, ],
        "droop": [Profile.SSH.value, ],
        "droopCompensation": [Profile.SSH.value, ],
        "maxModulationIndex": [Profile.EQ.value, ],
        "maxValveCurrent": [Profile.EQ.value, ],
        "pPccControl": [Profile.SSH.value, ],
        "qPccControl": [Profile.SSH.value, ],
        "qShare": [Profile.SSH.value, ],
        "targetQpcc": [Profile.SSH.value, ],
        "targetUpcc": [Profile.SSH.value, ],
        "uf": [Profile.SV.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class ACDCConverter:\n" + ACDCConverter.__doc__

    def __init__(self, CapabilityCurve = None, delta = 0.0, droop = 0.0, droopCompensation = 0.0, maxModulationIndex = 0.0, maxValveCurrent = 0.0, pPccControl = None, qPccControl = None, qShare = 0.0, targetQpcc = 0.0, targetUpcc = 0.0, uf = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.CapabilityCurve = CapabilityCurve
        self.delta = delta
        self.droop = droop
        self.droopCompensation = droopCompensation
        self.maxModulationIndex = maxModulationIndex
        self.maxValveCurrent = maxValveCurrent
        self.pPccControl = pPccControl
        self.qPccControl = qPccControl
        self.qShare = qShare
        self.targetQpcc = targetQpcc
        self.targetUpcc = targetUpcc
        self.uf = uf

    def __str__(self):
        str = "class=VsConverter\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
