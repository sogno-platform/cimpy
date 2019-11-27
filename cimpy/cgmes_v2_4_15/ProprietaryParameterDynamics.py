from cimpy.cgmes_v2_4_15.Base import Base


class ProprietaryParameterDynamics(Base):
	'''
	Supports definition of one or more parameters of several different datatypes for use by proprietary user-defined models.  NOTE: This class does not inherit from IdentifiedObject since it is not intended that a single instance of it be referenced by more than one proprietary user-defined model instance.

	:WindPlantUserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
	:WindType1or2UserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
	:WindType3or4UserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
	:SynchronousMachineUserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
	:AsynchronousMachineUserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
	:TurbineGovernorUserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
	:TurbineLoadControllerUserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
	:MechanicalLoadUserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
	:ExcitationSystemUserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
	:OverexcitationLimiterUserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
	:UnderexcitationLimiterUserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
	:PowerSystemStabilizerUserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
	:DiscontinuousExcitationControlUserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
	:PFVArControllerType1UserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
	:VoltageAdjusterUserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
	:PFVArControllerType2UserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
	:VoltageCompensatorUserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
	:LoadUserDefined: Proprietary user-defined model with which this parameter is associated. Default: None
	:parameterNumber: Sequence number of the parameter among the set of parameters associated with the related proprietary user-defined model. Default: 0
	:booleanParameterValue: Used for boolean parameter value. If this attribute is populated, integerParameterValue and floatParameterValue will not be. Default: False
	:integerParameterValue: Used for integer parameter value.  If this attribute is populated, booleanParameterValue and floatParameterValue will not be. Default: 0
	:floatParameterValue: Used for floating point parameter value.  If this attribute is populated, booleanParameterValue and integerParameterValue will not be. Default: 0.0
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'WindPlantUserDefined': [cgmesProfile.DY.value, ],
						'WindType1or2UserDefined': [cgmesProfile.DY.value, ],
						'WindType3or4UserDefined': [cgmesProfile.DY.value, ],
						'SynchronousMachineUserDefined': [cgmesProfile.DY.value, ],
						'AsynchronousMachineUserDefined': [cgmesProfile.DY.value, ],
						'TurbineGovernorUserDefined': [cgmesProfile.DY.value, ],
						'TurbineLoadControllerUserDefined': [cgmesProfile.DY.value, ],
						'MechanicalLoadUserDefined': [cgmesProfile.DY.value, ],
						'ExcitationSystemUserDefined': [cgmesProfile.DY.value, ],
						'OverexcitationLimiterUserDefined': [cgmesProfile.DY.value, ],
						'UnderexcitationLimiterUserDefined': [cgmesProfile.DY.value, ],
						'PowerSystemStabilizerUserDefined': [cgmesProfile.DY.value, ],
						'DiscontinuousExcitationControlUserDefined': [cgmesProfile.DY.value, ],
						'PFVArControllerType1UserDefined': [cgmesProfile.DY.value, ],
						'VoltageAdjusterUserDefined': [cgmesProfile.DY.value, ],
						'PFVArControllerType2UserDefined': [cgmesProfile.DY.value, ],
						'VoltageCompensatorUserDefined': [cgmesProfile.DY.value, ],
						'LoadUserDefined': [cgmesProfile.DY.value, ],
						'parameterNumber': [cgmesProfile.DY.value, ],
						'booleanParameterValue': [cgmesProfile.DY.value, ],
						'integerParameterValue': [cgmesProfile.DY.value, ],
						'floatParameterValue': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	

	def __init__(self, WindPlantUserDefined = None, WindType1or2UserDefined = None, WindType3or4UserDefined = None, SynchronousMachineUserDefined = None, AsynchronousMachineUserDefined = None, TurbineGovernorUserDefined = None, TurbineLoadControllerUserDefined = None, MechanicalLoadUserDefined = None, ExcitationSystemUserDefined = None, OverexcitationLimiterUserDefined = None, UnderexcitationLimiterUserDefined = None, PowerSystemStabilizerUserDefined = None, DiscontinuousExcitationControlUserDefined = None, PFVArControllerType1UserDefined = None, VoltageAdjusterUserDefined = None, PFVArControllerType2UserDefined = None, VoltageCompensatorUserDefined = None, LoadUserDefined = None, parameterNumber = 0, booleanParameterValue = False, integerParameterValue = 0, floatParameterValue = 0.0,  ):
	
		self.WindPlantUserDefined = WindPlantUserDefined
		self.WindType1or2UserDefined = WindType1or2UserDefined
		self.WindType3or4UserDefined = WindType3or4UserDefined
		self.SynchronousMachineUserDefined = SynchronousMachineUserDefined
		self.AsynchronousMachineUserDefined = AsynchronousMachineUserDefined
		self.TurbineGovernorUserDefined = TurbineGovernorUserDefined
		self.TurbineLoadControllerUserDefined = TurbineLoadControllerUserDefined
		self.MechanicalLoadUserDefined = MechanicalLoadUserDefined
		self.ExcitationSystemUserDefined = ExcitationSystemUserDefined
		self.OverexcitationLimiterUserDefined = OverexcitationLimiterUserDefined
		self.UnderexcitationLimiterUserDefined = UnderexcitationLimiterUserDefined
		self.PowerSystemStabilizerUserDefined = PowerSystemStabilizerUserDefined
		self.DiscontinuousExcitationControlUserDefined = DiscontinuousExcitationControlUserDefined
		self.PFVArControllerType1UserDefined = PFVArControllerType1UserDefined
		self.VoltageAdjusterUserDefined = VoltageAdjusterUserDefined
		self.PFVArControllerType2UserDefined = PFVArControllerType2UserDefined
		self.VoltageCompensatorUserDefined = VoltageCompensatorUserDefined
		self.LoadUserDefined = LoadUserDefined
		self.parameterNumber = parameterNumber
		self.booleanParameterValue = booleanParameterValue
		self.integerParameterValue = integerParameterValue
		self.floatParameterValue = floatParameterValue
		
	def __str__(self):
		str = 'class=ProprietaryParameterDynamics\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
