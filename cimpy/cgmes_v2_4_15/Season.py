from cimpy.output.IdentifiedObject import IdentifiedObject


class Season(IdentifiedObject):
	'''
	A specified time period of the year.

	:endDate: Date season ends. Default: 
	:startDate: Date season starts. Default: 
	:SeasonDayTypeSchedules: Season for the Schedule. Default: 
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'endDate': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'startDate': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'SeasonDayTypeSchedules': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, endDate = , startDate = , SeasonDayTypeSchedules = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.endDate = endDate
		self.startDate = startDate
		self.SeasonDayTypeSchedules = SeasonDayTypeSchedules
		
	def __str__(self):
		str = 'class=Season\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
