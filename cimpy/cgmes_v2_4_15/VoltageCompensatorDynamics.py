from .DynamicsFunctionBlock import DynamicsFunctionBlock
from .CGMESProfile import Profile


class VoltageCompensatorDynamics(DynamicsFunctionBlock):
    """
    Voltage compensator function block whose behaviour is described by reference to a standard model

    :ExcitationSystemDynamics: Excitation system model with which this voltage compensator is associated. Default: None
    :RemoteInputSignal: Remote input signal used by this voltage compensator model. Default: None
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "ExcitationSystemDynamics": [Profile.DY.value, ],
        "RemoteInputSignal": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class DynamicsFunctionBlock:\n" + DynamicsFunctionBlock.__doc__

    def __init__(self, ExcitationSystemDynamics = None, RemoteInputSignal = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ExcitationSystemDynamics = ExcitationSystemDynamics
        self.RemoteInputSignal = RemoteInputSignal

    def __str__(self):
        str = "class=VoltageCompensatorDynamics\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
