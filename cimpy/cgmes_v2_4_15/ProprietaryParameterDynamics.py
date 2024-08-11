from .Base import Base
from .CGMESProfile import Profile


class ProprietaryParameterDynamics(Base):
    """
    Supports definition of one or more parameters of several different datatypes for use by proprietary user-defined models.  NOTE: This class does not inherit from IdentifiedObject since it is not intended that a single instance of it be referenced by more than one proprietary user-defined model instance.

    :AsynchronousMachineUserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
    :DiscontinuousExcitationControlUserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
    :ExcitationSystemUserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
    :LoadUserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
    :MechanicalLoadUserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
    :OverexcitationLimiterUserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
    :PFVArControllerType1UserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
    :PFVArControllerType2UserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
    :PowerSystemStabilizerUserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
    :SynchronousMachineUserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
    :TurbineGovernorUserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
    :TurbineLoadControllerUserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
    :UnderexcitationLimiterUserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
    :VoltageAdjusterUserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
    :VoltageCompensatorUserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
    :WindPlantUserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
    :WindType1or2UserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
    :WindType3or4UserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
    :booleanParameterValue: Used for boolean parameter value. If this attribute is populated, integerParameterValue and floatParameterValue will not be. Default: False
    :floatParameterValue: Used for floating point parameter value.  If this attribute is populated, booleanParameterValue and integerParameterValue will not be. Default: 0.0
    :integerParameterValue: Used for integer parameter value.  If this attribute is populated, booleanParameterValue and floatParameterValue will not be. Default: 0
    :parameterNumber: Sequence number of the parameter among the set of parameters associated with the related proprietary user-defined model. Default: 0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "AsynchronousMachineUserDefined": [Profile.DY.value, ],
        "DiscontinuousExcitationControlUserDefined": [Profile.DY.value, ],
        "ExcitationSystemUserDefined": [Profile.DY.value, ],
        "LoadUserDefined": [Profile.DY.value, ],
        "MechanicalLoadUserDefined": [Profile.DY.value, ],
        "OverexcitationLimiterUserDefined": [Profile.DY.value, ],
        "PFVArControllerType1UserDefined": [Profile.DY.value, ],
        "PFVArControllerType2UserDefined": [Profile.DY.value, ],
        "PowerSystemStabilizerUserDefined": [Profile.DY.value, ],
        "SynchronousMachineUserDefined": [Profile.DY.value, ],
        "TurbineGovernorUserDefined": [Profile.DY.value, ],
        "TurbineLoadControllerUserDefined": [Profile.DY.value, ],
        "UnderexcitationLimiterUserDefined": [Profile.DY.value, ],
        "VoltageAdjusterUserDefined": [Profile.DY.value, ],
        "VoltageCompensatorUserDefined": [Profile.DY.value, ],
        "WindPlantUserDefined": [Profile.DY.value, ],
        "WindType1or2UserDefined": [Profile.DY.value, ],
        "WindType3or4UserDefined": [Profile.DY.value, ],
        "booleanParameterValue": [Profile.DY.value, ],
        "floatParameterValue": [Profile.DY.value, ],
        "integerParameterValue": [Profile.DY.value, ],
        "parameterNumber": [Profile.DY.value, ],
    }

    serializationProfile = {}


    def __init__(self, AsynchronousMachineUserDefined = None, DiscontinuousExcitationControlUserDefined = None, ExcitationSystemUserDefined = None, LoadUserDefined = None, MechanicalLoadUserDefined = None, OverexcitationLimiterUserDefined = None, PFVArControllerType1UserDefined = None, PFVArControllerType2UserDefined = None, PowerSystemStabilizerUserDefined = None, SynchronousMachineUserDefined = None, TurbineGovernorUserDefined = None, TurbineLoadControllerUserDefined = None, UnderexcitationLimiterUserDefined = None, VoltageAdjusterUserDefined = None, VoltageCompensatorUserDefined = None, WindPlantUserDefined = None, WindType1or2UserDefined = None, WindType3or4UserDefined = None, booleanParameterValue = False, floatParameterValue = 0.0, integerParameterValue = 0, parameterNumber = 0):

        self.AsynchronousMachineUserDefined = AsynchronousMachineUserDefined
        self.DiscontinuousExcitationControlUserDefined = DiscontinuousExcitationControlUserDefined
        self.ExcitationSystemUserDefined = ExcitationSystemUserDefined
        self.LoadUserDefined = LoadUserDefined
        self.MechanicalLoadUserDefined = MechanicalLoadUserDefined
        self.OverexcitationLimiterUserDefined = OverexcitationLimiterUserDefined
        self.PFVArControllerType1UserDefined = PFVArControllerType1UserDefined
        self.PFVArControllerType2UserDefined = PFVArControllerType2UserDefined
        self.PowerSystemStabilizerUserDefined = PowerSystemStabilizerUserDefined
        self.SynchronousMachineUserDefined = SynchronousMachineUserDefined
        self.TurbineGovernorUserDefined = TurbineGovernorUserDefined
        self.TurbineLoadControllerUserDefined = TurbineLoadControllerUserDefined
        self.UnderexcitationLimiterUserDefined = UnderexcitationLimiterUserDefined
        self.VoltageAdjusterUserDefined = VoltageAdjusterUserDefined
        self.VoltageCompensatorUserDefined = VoltageCompensatorUserDefined
        self.WindPlantUserDefined = WindPlantUserDefined
        self.WindType1or2UserDefined = WindType1or2UserDefined
        self.WindType3or4UserDefined = WindType3or4UserDefined
        self.booleanParameterValue = booleanParameterValue
        self.floatParameterValue = floatParameterValue
        self.integerParameterValue = integerParameterValue
        self.parameterNumber = parameterNumber

    def __str__(self):
        str = "class=ProprietaryParameterDynamics\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
