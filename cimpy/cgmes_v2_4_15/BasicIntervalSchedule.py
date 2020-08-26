from cimpy.output.IdentifiedObject import IdentifiedObject


class BasicIntervalSchedule(IdentifiedObject):
	'''
	Schedule of values at points in time.

	:startTime: The time for the first time point. Default: 
	:value1Unit: Value1 units of measure. Default: 
	:value2Unit: Value2 units of measure. Default: 
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'startTime': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'value1Unit': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'value2Unit': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, startTime = , value1Unit = , value2Unit = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.startTime = startTime
		self.value1Unit = value1Unit
		self.value2Unit = value2Unit
		
	def __str__(self):
		str = 'class=BasicIntervalSchedule\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
