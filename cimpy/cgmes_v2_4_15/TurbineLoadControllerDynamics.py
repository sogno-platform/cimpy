from .DynamicsFunctionBlock import DynamicsFunctionBlock
from .CGMESProfile import Profile


class TurbineLoadControllerDynamics(DynamicsFunctionBlock):
    """
    Turbine load controller function block whose behavior is described by reference to a standard model

    :TurbineGovernorDynamics: Turbine-governor controlled by this turbine load controller. Default: None
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "TurbineGovernorDynamics": [Profile.DY.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class DynamicsFunctionBlock:\n" + DynamicsFunctionBlock.__doc__

    def __init__(self, TurbineGovernorDynamics = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.TurbineGovernorDynamics = TurbineGovernorDynamics

    def __str__(self):
        str = "class=TurbineLoadControllerDynamics\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
