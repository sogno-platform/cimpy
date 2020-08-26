from cimpy.output.DynamicsFunctionBlock import DynamicsFunctionBlock


class WindTurbineType1or2Dynamics(DynamicsFunctionBlock):
	'''
	Parent class supporting relationships to wind turbines Type 1 and 2 and their control models.

	:RemoteInputSignal: Remote input signal used by this wind generator Type 1 or Type 2 model. Default: 
	:AsynchronousMachineDynamics: Asynchronous machine model with which this wind generator type 1 or 2 model is associated. Default: 
		'''

	cgmesProfile = DynamicsFunctionBlock.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'RemoteInputSignal': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'AsynchronousMachineDynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class DynamicsFunctionBlock: \n' + DynamicsFunctionBlock.__doc__ 

	def __init__(self, RemoteInputSignal = , AsynchronousMachineDynamics = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.RemoteInputSignal = RemoteInputSignal
		self.AsynchronousMachineDynamics = AsynchronousMachineDynamics
		
	def __str__(self):
		str = 'class=WindTurbineType1or2Dynamics\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
