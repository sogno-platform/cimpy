from cimpy.output.AnalogControl import AnalogControl


class SetPoint(AnalogControl):
	'''
	An analog control that issue a set point value.

	:normalValue: Normal value for Control.value e.g. used for percentage scaling. Default: 
	:value: The value representing the actuator output. Default: 
		'''

	cgmesProfile = AnalogControl.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'normalValue': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'value': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class AnalogControl: \n' + AnalogControl.__doc__ 

	def __init__(self, normalValue = , value = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.normalValue = normalValue
		self.value = value
		
	def __str__(self):
		str = 'class=SetPoint\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
