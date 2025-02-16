from .DynamicsFunctionBlock import DynamicsFunctionBlock
from .CGMESProfile import Profile


class PFVArControllerType1Dynamics(DynamicsFunctionBlock):
    """
    Power Factor or VAr controller Type I function block whose behaviour is described by reference to a standard model

    :ExcitationSystemDynamics: Excitation system model with which this Power Factor or VAr controller Type I model is associated. Default: None
    :RemoteInputSignal: Remote input signal used by this Power Factor or VAr controller Type I model. Default: None
    :VoltageAdjusterDynamics: Voltage adjuster model associated with this Power Factor or VA controller Type I model. Default: None
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "ExcitationSystemDynamics": [Profile.DY.value, ],
        "RemoteInputSignal": [Profile.DY.value, ],
        "VoltageAdjusterDynamics": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class DynamicsFunctionBlock:\n" + DynamicsFunctionBlock.__doc__

    def __init__(self, ExcitationSystemDynamics = None, RemoteInputSignal = None, VoltageAdjusterDynamics = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ExcitationSystemDynamics = ExcitationSystemDynamics
        self.RemoteInputSignal = RemoteInputSignal
        self.VoltageAdjusterDynamics = VoltageAdjusterDynamics

    def __str__(self):
        str = "class=PFVArControllerType1Dynamics\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
