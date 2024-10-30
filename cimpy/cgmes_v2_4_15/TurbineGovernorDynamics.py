from .DynamicsFunctionBlock import DynamicsFunctionBlock
from .CGMESProfile import Profile


class TurbineGovernorDynamics(DynamicsFunctionBlock):
    """
    Turbine-governor function block whose behavior is described by reference to a standard model

    :AsynchronousMachineDynamics: Asynchronous machine model with which this turbine-governor model is associated. Default: None
    :SynchronousMachineDynamics: Turbine-governor model associated with this synchronous machine model. Default: "list"
    :TurbineLoadControllerDynamics: Turbine load controller providing input to this turbine-governor. Default: None
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "AsynchronousMachineDynamics": [Profile.DY.value, ],
        "SynchronousMachineDynamics": [Profile.DY.value, ],
        "TurbineLoadControllerDynamics": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class DynamicsFunctionBlock:\n" + DynamicsFunctionBlock.__doc__

    def __init__(self, AsynchronousMachineDynamics = None, SynchronousMachineDynamics = "list", TurbineLoadControllerDynamics = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.AsynchronousMachineDynamics = AsynchronousMachineDynamics
        self.SynchronousMachineDynamics = SynchronousMachineDynamics
        self.TurbineLoadControllerDynamics = TurbineLoadControllerDynamics

    def __str__(self):
        str = "class=TurbineGovernorDynamics\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
