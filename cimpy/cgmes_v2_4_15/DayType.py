from cimpy.output.IdentifiedObject import IdentifiedObject


class DayType(IdentifiedObject):
	'''
	Group of similar days.   For example it could be used to represent weekdays, weekend, or holidays.

	:SeasonDayTypeSchedules: DayType for the Schedule. Default: 
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'SeasonDayTypeSchedules': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, SeasonDayTypeSchedules = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.SeasonDayTypeSchedules = SeasonDayTypeSchedules
		
	def __str__(self):
		str = 'class=DayType\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
