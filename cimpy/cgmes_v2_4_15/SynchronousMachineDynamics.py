from .RotatingMachineDynamics import RotatingMachineDynamics
from .CGMESProfile import Profile


class SynchronousMachineDynamics(RotatingMachineDynamics):
    """
    Synchronous machine whose behaviour is described by reference to a standard model expressed in one of the following forms:

    :ExcitationSystemDynamics: Excitation system model associated with this synchronous machine model. Default: None
    :GenICompensationForGenJ: Compensation of voltage compensator`s generator for current flow out of this  generator. Default: "list"
    :MechanicalLoadDynamics: Mechanical load model associated with this synchronous machine model. Default: None
    :SynchronousMachine: Synchronous machine to which synchronous machine dynamics model applies. Default: None
    :TurbineGovernorDynamics: Synchronous machine model with which this turbine-governor model is associated. Default: "list"
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "ExcitationSystemDynamics": [Profile.DY.value, ],
        "GenICompensationForGenJ": [Profile.DY.value, ],
        "MechanicalLoadDynamics": [Profile.DY.value, ],
        "SynchronousMachine": [Profile.DY.value, ],
        "TurbineGovernorDynamics": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class RotatingMachineDynamics:\n" + RotatingMachineDynamics.__doc__

    def __init__(self, ExcitationSystemDynamics = None, GenICompensationForGenJ = "list", MechanicalLoadDynamics = None, SynchronousMachine = None, TurbineGovernorDynamics = "list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ExcitationSystemDynamics = ExcitationSystemDynamics
        self.GenICompensationForGenJ = GenICompensationForGenJ
        self.MechanicalLoadDynamics = MechanicalLoadDynamics
        self.SynchronousMachine = SynchronousMachine
        self.TurbineGovernorDynamics = TurbineGovernorDynamics

    def __str__(self):
        str = "class=SynchronousMachineDynamics\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
