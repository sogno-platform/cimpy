from cimpy.output.DynamicsFunctionBlock import DynamicsFunctionBlock


class PFVArControllerType1Dynamics(DynamicsFunctionBlock):
	'''
	Power Factor or VAr controller Type I function block whose behaviour is described by reference to a standard model

	:RemoteInputSignal: Remote input signal used by this Power Factor or VAr controller Type I model. Default: 
	:ExcitationSystemDynamics: Excitation system model with which this Power Factor or VAr controller Type I model is associated. Default: 
	:VoltageAdjusterDynamics: Voltage adjuster model associated with this Power Factor or VA controller Type I model. Default: 
		'''

	cgmesProfile = DynamicsFunctionBlock.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'RemoteInputSignal': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ExcitationSystemDynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'VoltageAdjusterDynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class DynamicsFunctionBlock: \n' + DynamicsFunctionBlock.__doc__ 

	def __init__(self, RemoteInputSignal = , ExcitationSystemDynamics = , VoltageAdjusterDynamics = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.RemoteInputSignal = RemoteInputSignal
		self.ExcitationSystemDynamics = ExcitationSystemDynamics
		self.VoltageAdjusterDynamics = VoltageAdjusterDynamics
		
	def __str__(self):
		str = 'class=PFVArControllerType1Dynamics\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
