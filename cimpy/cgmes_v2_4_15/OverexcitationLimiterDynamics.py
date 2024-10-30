from .DynamicsFunctionBlock import DynamicsFunctionBlock
from .CGMESProfile import Profile


class OverexcitationLimiterDynamics(DynamicsFunctionBlock):
    """
    Overexcitation limiter function block whose behaviour is described by reference to a standard model

    :ExcitationSystemDynamics: Excitation system model with which this overexcitation limiter model is associated. Default: None
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "ExcitationSystemDynamics": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class DynamicsFunctionBlock:\n" + DynamicsFunctionBlock.__doc__

    def __init__(self, ExcitationSystemDynamics = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ExcitationSystemDynamics = ExcitationSystemDynamics

    def __str__(self):
        str = "class=OverexcitationLimiterDynamics\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str