from .DynamicsFunctionBlock import DynamicsFunctionBlock
from .CGMESProfile import Profile


class MechanicalLoadDynamics(DynamicsFunctionBlock):
    """
    Mechanical load function block whose behavior is described by reference to a standard model

    :AsynchronousMachineDynamics: Asynchronous machine model with which this mechanical load model is associated. Default: None
    :SynchronousMachineDynamics: Synchronous machine model with which this mechanical load model is associated. Default: None
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "AsynchronousMachineDynamics": [Profile.DY.value, ],
        "SynchronousMachineDynamics": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class DynamicsFunctionBlock:\n" + DynamicsFunctionBlock.__doc__

    def __init__(self, AsynchronousMachineDynamics = None, SynchronousMachineDynamics = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.AsynchronousMachineDynamics = AsynchronousMachineDynamics
        self.SynchronousMachineDynamics = SynchronousMachineDynamics

    def __str__(self):
        str = "class=MechanicalLoadDynamics\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
