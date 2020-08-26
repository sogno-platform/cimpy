from cimpy.output.Limit import Limit


class AnalogLimit(Limit):
	'''
	Limit values for Analog measurements.

	:value: The value to supervise against. Default: 
	:LimitSet: The limit values used for supervision of Measurements. Default: 
		'''

	cgmesProfile = Limit.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'value': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'LimitSet': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class Limit: \n' + Limit.__doc__ 

	def __init__(self, value = , LimitSet = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.value = value
		self.LimitSet = LimitSet
		
	def __str__(self):
		str = 'class=AnalogLimit\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
