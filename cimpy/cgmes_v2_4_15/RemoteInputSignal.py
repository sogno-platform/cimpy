from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class RemoteInputSignal(IdentifiedObject):
    """
    Supports connection to a terminal associated with a remote bus from which an input signal of a specific type is coming.

    :DiscontinuousExcitationControlDynamics: Discontinuous excitation control model using this remote input signal. Default: None
    :PFVArControllerType1Dynamics: Power Factor or VAr controller Type I model using this remote input signal. Default: None
    :PowerSystemStabilizerDynamics: Power system stabilizer model using this remote input signal. Default: None
    :Terminal: Remote terminal with which this input signal is associated. Default: None
    :UnderexcitationLimiterDynamics: Underexcitation limiter model using this remote input signal. Default: None
    :VoltageCompensatorDynamics: Voltage compensator model using this remote input signal. Default: None
    :WindPlantDynamics: The remote signal with which this power plant is associated. Default: None
    :WindTurbineType1or2Dynamics: Wind generator Type 1 or Type 2 model using this remote input signal. Default: None
    :WindTurbineType3or4Dynamics: Remote input signal used by these wind turbine Type 3 or 4 models. Default: None
    :remoteSignalType: Type of input signal. Default: None
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "DiscontinuousExcitationControlDynamics": [Profile.DY.value, ],
        "PFVArControllerType1Dynamics": [Profile.DY.value, ],
        "PowerSystemStabilizerDynamics": [Profile.DY.value, ],
        "Terminal": [Profile.DY.value, ],
        "UnderexcitationLimiterDynamics": [Profile.DY.value, ],
        "VoltageCompensatorDynamics": [Profile.DY.value, ],
        "WindPlantDynamics": [Profile.DY.value, ],
        "WindTurbineType1or2Dynamics": [Profile.DY.value, ],
        "WindTurbineType3or4Dynamics": [Profile.DY.value, ],
        "remoteSignalType": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, DiscontinuousExcitationControlDynamics = None, PFVArControllerType1Dynamics = None, PowerSystemStabilizerDynamics = None, Terminal = None, UnderexcitationLimiterDynamics = None, VoltageCompensatorDynamics = None, WindPlantDynamics = None, WindTurbineType1or2Dynamics = None, WindTurbineType3or4Dynamics = None, remoteSignalType = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.DiscontinuousExcitationControlDynamics = DiscontinuousExcitationControlDynamics
        self.PFVArControllerType1Dynamics = PFVArControllerType1Dynamics
        self.PowerSystemStabilizerDynamics = PowerSystemStabilizerDynamics
        self.Terminal = Terminal
        self.UnderexcitationLimiterDynamics = UnderexcitationLimiterDynamics
        self.VoltageCompensatorDynamics = VoltageCompensatorDynamics
        self.WindPlantDynamics = WindPlantDynamics
        self.WindTurbineType1or2Dynamics = WindTurbineType1or2Dynamics
        self.WindTurbineType3or4Dynamics = WindTurbineType3or4Dynamics
        self.remoteSignalType = remoteSignalType

    def __str__(self):
        str = "class=RemoteInputSignal\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
