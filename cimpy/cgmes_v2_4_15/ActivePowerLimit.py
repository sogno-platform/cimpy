from cimpy.output.OperationalLimit import OperationalLimit


class ActivePowerLimit(OperationalLimit):
	'''
	Limit on active power flow.

	:value: Value of active power limit. Default: 
		'''

	cgmesProfile = OperationalLimit.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'value': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class OperationalLimit: \n' + OperationalLimit.__doc__ 

	def __init__(self, value = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.value = value
		
	def __str__(self):
		str = 'class=ActivePowerLimit\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
