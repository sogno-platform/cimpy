from cimpy.output.DynamicsFunctionBlock import DynamicsFunctionBlock


class ExcitationSystemDynamics(DynamicsFunctionBlock):
	'''
	Excitation system function block whose behavior is described by reference to a standard model

	:SynchronousMachineDynamics: Synchronous machine model with which this excitation system model is associated. Default: 
	:PowerSystemStabilizerDynamics: Power system stabilizer model associated with this excitation system model. Default: 
	:PFVArControllerType1Dynamics: Power Factor or VAr controller Type I model associated with this excitation system model. Default: 
	:VoltageCompensatorDynamics: Voltage compensator model associated with this excitation system model. Default: 
	:DiscontinuousExcitationControlDynamics: Discontinuous excitation control model associated with this excitation system model. Default: 
	:UnderexcitationLimiterDynamics: Undrexcitation limiter model associated with this excitation system model. Default: 
	:PFVArControllerType2Dynamics: Power Factor or VAr controller Type II model associated with this excitation system model. Default: 
	:OverexcitationLimiterDynamics: Overexcitation limiter model associated with this excitation system model. Default: 
		'''

	cgmesProfile = DynamicsFunctionBlock.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'SynchronousMachineDynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'PowerSystemStabilizerDynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'PFVArControllerType1Dynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'VoltageCompensatorDynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'DiscontinuousExcitationControlDynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'UnderexcitationLimiterDynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'PFVArControllerType2Dynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'OverexcitationLimiterDynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class DynamicsFunctionBlock: \n' + DynamicsFunctionBlock.__doc__ 

	def __init__(self, SynchronousMachineDynamics = , PowerSystemStabilizerDynamics = , PFVArControllerType1Dynamics = , VoltageCompensatorDynamics = , DiscontinuousExcitationControlDynamics = , UnderexcitationLimiterDynamics = , PFVArControllerType2Dynamics = , OverexcitationLimiterDynamics = ,  *args, **kw_args):
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
