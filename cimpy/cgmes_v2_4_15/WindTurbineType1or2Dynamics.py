from .DynamicsFunctionBlock import DynamicsFunctionBlock
from .CGMESProfile import Profile


class WindTurbineType1or2Dynamics(DynamicsFunctionBlock):
    """
    Parent class supporting relationships to wind turbines Type 1 and 2 and their control models.

    :AsynchronousMachineDynamics: Asynchronous machine model with which this wind generator type 1 or 2 model is associated. Default: None
    :RemoteInputSignal: Remote input signal used by this wind generator Type 1 or Type 2 model. Default: None
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "AsynchronousMachineDynamics": [Profile.DY.value, ],
        "RemoteInputSignal": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class DynamicsFunctionBlock:\n" + DynamicsFunctionBlock.__doc__

    def __init__(self, AsynchronousMachineDynamics = None, RemoteInputSignal = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.AsynchronousMachineDynamics = AsynchronousMachineDynamics
        self.RemoteInputSignal = RemoteInputSignal

    def __str__(self):
        str = "class=WindTurbineType1or2Dynamics\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
