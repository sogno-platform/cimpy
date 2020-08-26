from cimpy.output.DynamicsFunctionBlock import DynamicsFunctionBlock


class TurbineGovernorDynamics(DynamicsFunctionBlock):
	'''
	Turbine-governor function block whose behavior is described by reference to a standard model

	:SynchronousMachineDynamics: Turbine-governor model associated with this synchronous machine model. Default: 
	:AsynchronousMachineDynamics: Asynchronous machine model with which this turbine-governor model is associated. Default: 
	:TurbineLoadControllerDynamics: Turbine load controller providing input to this turbine-governor. Default: 
		'''

	cgmesProfile = DynamicsFunctionBlock.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'SynchronousMachineDynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'AsynchronousMachineDynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'TurbineLoadControllerDynamics': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class DynamicsFunctionBlock: \n' + DynamicsFunctionBlock.__doc__ 

	def __init__(self, SynchronousMachineDynamics = , AsynchronousMachineDynamics = , TurbineLoadControllerDynamics = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.SynchronousMachineDynamics = SynchronousMachineDynamics
		self.AsynchronousMachineDynamics = AsynchronousMachineDynamics
		self.TurbineLoadControllerDynamics = TurbineLoadControllerDynamics
		
	def __str__(self):
		str = 'class=TurbineGovernorDynamics\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
