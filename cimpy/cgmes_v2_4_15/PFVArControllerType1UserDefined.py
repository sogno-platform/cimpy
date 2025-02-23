from .PFVArControllerType1Dynamics import PFVArControllerType1Dynamics
from .CGMESProfile import Profile


class PFVArControllerType1UserDefined(PFVArControllerType1Dynamics):
    """
    Power Factor or VAr controller Type I function block whose dynamic behaviour is described by

    :ProprietaryParameterDynamics: Parameter of this proprietary user-defined model. Default: "list"
    :proprietary: Behaviour is based on proprietary model as opposed to detailed model. true = user-defined model is proprietary with behaviour mutually understood by sending and receiving applications and parameters passed as general attributes false = user-defined model is explicitly defined in terms of control blocks and their input and output signals. Default: False
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "ProprietaryParameterDynamics": [Profile.DY.value, ],
        "proprietary": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class PFVArControllerType1Dynamics:\n" + PFVArControllerType1Dynamics.__doc__

    def __init__(self, ProprietaryParameterDynamics = "list", proprietary = False, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ProprietaryParameterDynamics = ProprietaryParameterDynamics
        self.proprietary = proprietary

    def __str__(self):
        str = "class=PFVArControllerType1UserDefined\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
