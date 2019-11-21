from cimpy.cgmes_v2_4_15_flat.DynamicsFunctionBlock import DynamicsFunctionBlock


class ExcitationSystemDynamics(DynamicsFunctionBlock):
	'''
	Excitation system function block whose behavior is described by reference to a standard model

	:SynchronousMachineDynamics: Synchronous machine model with which this excitation system model is associated. Default: None
	:PowerSystemStabilizerDynamics: Power system stabilizer model associated with this excitation system model. Default: None
	:PFVArControllerType1Dynamics: Power Factor or VAr controller Type I model associated with this excitation system model. Default: None
	:VoltageCompensatorDynamics: Voltage compensator model associated with this excitation system model. Default: None
	:DiscontinuousExcitationControlDynamics: Discontinuous excitation control model associated with this excitation system model. Default: None
	:UnderexcitationLimiterDynamics: Undrexcitation limiter model associated with this excitation system model. Default: None
	:PFVArControllerType2Dynamics: Power Factor or VAr controller Type II model associated with this excitation system model. Default: None
	:OverexcitationLimiterDynamics: Overexcitation limiter model associated with this excitation system model. Default: None
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'SynchronousMachineDynamics': [cgmesProfile.DY.value, ],
						'PowerSystemStabilizerDynamics': [cgmesProfile.DY.value, ],
						'PFVArControllerType1Dynamics': [cgmesProfile.DY.value, ],
						'VoltageCompensatorDynamics': [cgmesProfile.DY.value, ],
						'DiscontinuousExcitationControlDynamics': [cgmesProfile.DY.value, ],
						'UnderexcitationLimiterDynamics': [cgmesProfile.DY.value, ],
						'PFVArControllerType2Dynamics': [cgmesProfile.DY.value, ],
						'OverexcitationLimiterDynamics': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class DynamicsFunctionBlock: \n' + DynamicsFunctionBlock.__doc__ 

	def __init__(self, SynchronousMachineDynamics = None, PowerSystemStabilizerDynamics = None, PFVArControllerType1Dynamics = None, VoltageCompensatorDynamics = None, DiscontinuousExcitationControlDynamics = None, UnderexcitationLimiterDynamics = None, PFVArControllerType2Dynamics = None, OverexcitationLimiterDynamics = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.SynchronousMachineDynamics = SynchronousMachineDynamics
		self.PowerSystemStabilizerDynamics = PowerSystemStabilizerDynamics
		self.PFVArControllerType1Dynamics = PFVArControllerType1Dynamics
		self.VoltageCompensatorDynamics = VoltageCompensatorDynamics
		self.DiscontinuousExcitationControlDynamics = DiscontinuousExcitationControlDynamics
		self.UnderexcitationLimiterDynamics = UnderexcitationLimiterDynamics
		self.PFVArControllerType2Dynamics = PFVArControllerType2Dynamics
		self.OverexcitationLimiterDynamics = OverexcitationLimiterDynamics
		
	def __str__(self):
		str = 'class=ExcitationSystemDynamics\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
