from cimpy.output.LoadDynamics import LoadDynamics


class LoadAggregate(LoadDynamics):
	'''
	Standard aggregate load model comprised of static and/or dynamic components.  A static load model represents the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage. A dynamic load model can used to represent the aggregate response of the motor components of the load.

	:LoadStatic: Aggregate static load associated with this aggregate load. Default: 
	:LoadMotor: Aggregate motor (dynamic) load associated with this aggregate load. Default: 
		'''

	cgmesProfile = LoadDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'LoadStatic': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'LoadMotor': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class LoadDynamics: \n' + LoadDynamics.__doc__ 

	def __init__(self, LoadStatic = , LoadMotor = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.LoadStatic = LoadStatic
		self.LoadMotor = LoadMotor
		
	def __str__(self):
		str = 'class=LoadAggregate\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
