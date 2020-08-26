from cimpy.output.OperationalLimit import OperationalLimit


class VoltageLimit(OperationalLimit):
	'''
	Operational limit applied to voltage.

	:value: Limit on voltage. High or low limit nature of the limit depends upon the properties of the operational limit type. Default: 
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
		str = 'class=VoltageLimit\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
