from .DynamicsFunctionBlock import DynamicsFunctionBlock
from .CGMESProfile import Profile


class ExcitationSystemDynamics(DynamicsFunctionBlock):
    """
    Excitation system function block whose behavior is described by reference to a standard model

    :DiscontinuousExcitationControlDynamics: Discontinuous excitation control model associated with this excitation system model. Default: None
    :OverexcitationLimiterDynamics: Overexcitation limiter model associated with this excitation system model. Default: None
    :PFVArControllerType1Dynamics: Power Factor or VAr controller Type I model associated with this excitation system model. Default: None
    :PFVArControllerType2Dynamics: Power Factor or VAr controller Type II model associated with this excitation system model. Default: None
    :PowerSystemStabilizerDynamics: Power system stabilizer model associated with this excitation system model. Default: None
    :SynchronousMachineDynamics: Synchronous machine model with which this excitation system model is associated. Default: None
    :UnderexcitationLimiterDynamics: Undrexcitation limiter model associated with this excitation system model. Default: None
    :VoltageCompensatorDynamics: Voltage compensator model associated with this excitation system model. Default: None
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "DiscontinuousExcitationControlDynamics": [Profile.DY.value, ],
        "OverexcitationLimiterDynamics": [Profile.DY.value, ],
        "PFVArControllerType1Dynamics": [Profile.DY.value, ],
        "PFVArControllerType2Dynamics": [Profile.DY.value, ],
        "PowerSystemStabilizerDynamics": [Profile.DY.value, ],
        "SynchronousMachineDynamics": [Profile.DY.value, ],
        "UnderexcitationLimiterDynamics": [Profile.DY.value, ],
        "VoltageCompensatorDynamics": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class DynamicsFunctionBlock:\n" + DynamicsFunctionBlock.__doc__

    def __init__(self, DiscontinuousExcitationControlDynamics = None, OverexcitationLimiterDynamics = None, PFVArControllerType1Dynamics = None, PFVArControllerType2Dynamics = None, PowerSystemStabilizerDynamics = None, SynchronousMachineDynamics = None, UnderexcitationLimiterDynamics = None, VoltageCompensatorDynamics = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.DiscontinuousExcitationControlDynamics = DiscontinuousExcitationControlDynamics
        self.OverexcitationLimiterDynamics = OverexcitationLimiterDynamics
        self.PFVArControllerType1Dynamics = PFVArControllerType1Dynamics
        self.PFVArControllerType2Dynamics = PFVArControllerType2Dynamics
        self.PowerSystemStabilizerDynamics = PowerSystemStabilizerDynamics
        self.SynchronousMachineDynamics = SynchronousMachineDynamics
        self.UnderexcitationLimiterDynamics = UnderexcitationLimiterDynamics
        self.VoltageCompensatorDynamics = VoltageCompensatorDynamics

    def __str__(self):
        str = "class=ExcitationSystemDynamics\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
