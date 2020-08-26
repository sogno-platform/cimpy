from cimpy.output.MeasurementValue import MeasurementValue


class DiscreteValue(MeasurementValue):
	'''
	DiscreteValue represents a discrete MeasurementValue.

	:Command: The MeasurementValue that is controlled. Default: 
	:Discrete: The values connected to this measurement. Default: 
	:value: The value to supervise. Default: 
		'''

	cgmesProfile = MeasurementValue.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'Command': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'Discrete': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'value': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class MeasurementValue: \n' + MeasurementValue.__doc__ 

	def __init__(self, Command = , Discrete = , value = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.Command = Command
		self.Discrete = Discrete
		self.value = value
		
	def __str__(self):
		str = 'class=DiscreteValue\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
