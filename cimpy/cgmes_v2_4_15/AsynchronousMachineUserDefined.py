from .AsynchronousMachineDynamics import AsynchronousMachineDynamics
from .CGMESProfile import Profile


class AsynchronousMachineUserDefined(AsynchronousMachineDynamics):
    """
    Asynchronous machine whose dynamic behaviour is described by a user-defined model.

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

    __doc__ += "\nDocumentation of parent class AsynchronousMachineDynamics:\n" + AsynchronousMachineDynamics.__doc__

    def __init__(self, ProprietaryParameterDynamics = "list", proprietary = False, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ProprietaryParameterDynamics = ProprietaryParameterDynamics
        self.proprietary = proprietary

    def __str__(self):
        str = "class=AsynchronousMachineUserDefined\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
