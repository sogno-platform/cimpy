from .DynamicsFunctionBlock import DynamicsFunctionBlock


class ExcitationSystemDynamics(DynamicsFunctionBlock):
	'''
	Excitation system function block whose behaviour is described by reference to a standard model <font color="#0f0f0f">or by definition of a user-defined model.</font>

	:SynchronousMachineDynamics: Synchronous machine model with which this excitation system model is associated. Default: None
	:VoltageCompensatorDynamics: Voltage compensator model associated with this excitation system model. Default: None
	:OverexcitationLimiterDynamics: Overexcitation limiter model associated with this excitation system model. Default: None
	:PFVArControllerType2Dynamics: Power factor or VAr controller type 2 model associated with this excitation system model. Default: None
	:DiscontinuousExcitationControlDynamics: Discontinuous excitation control model associated with this excitation system model. Default: None
	:PowerSystemStabilizerDynamics: Power system stabilizer model associated with this excitation system model. Default: None
	:UnderexcitationLimiterDynamics: Undrexcitation limiter model associated with this excitation system model. Default: None
	:PFVArControllerType1Dynamics: Power factor or VAr controller type 1 model associated with this excitation system model. Default: None
		'''

	cgmesProfile = DynamicsFunctionBlock.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'SynchronousMachineDynamics': [cgmesProfile.DY.value, ],
						'VoltageCompensatorDynamics': [cgmesProfile.DY.value, ],
						'OverexcitationLimiterDynamics': [cgmesProfile.DY.value, ],
						'PFVArControllerType2Dynamics': [cgmesProfile.DY.value, ],
						'DiscontinuousExcitationControlDynamics': [cgmesProfile.DY.value, ],
						'PowerSystemStabilizerDynamics': [cgmesProfile.DY.value, ],
						'UnderexcitationLimiterDynamics': [cgmesProfile.DY.value, ],
						'PFVArControllerType1Dynamics': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class DynamicsFunctionBlock: \n' + DynamicsFunctionBlock.__doc__ 

	def __init__(self, SynchronousMachineDynamics = None, VoltageCompensatorDynamics = None, OverexcitationLimiterDynamics = None, PFVArControllerType2Dynamics = None, DiscontinuousExcitationControlDynamics = None, PowerSystemStabilizerDynamics = None, UnderexcitationLimiterDynamics = None, PFVArControllerType1Dynamics = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.SynchronousMachineDynamics = SynchronousMachineDynamics
		self.VoltageCompensatorDynamics = VoltageCompensatorDynamics
		self.OverexcitationLimiterDynamics = OverexcitationLimiterDynamics
		self.PFVArControllerType2Dynamics = PFVArControllerType2Dynamics
		self.DiscontinuousExcitationControlDynamics = DiscontinuousExcitationControlDynamics
		self.PowerSystemStabilizerDynamics = PowerSystemStabilizerDynamics
		self.UnderexcitationLimiterDynamics = UnderexcitationLimiterDynamics
		self.PFVArControllerType1Dynamics = PFVArControllerType1Dynamics
		
	def __str__(self):
		str = 'class=ExcitationSystemDynamics\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
