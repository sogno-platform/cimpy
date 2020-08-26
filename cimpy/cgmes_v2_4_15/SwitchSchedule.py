from cimpy.output.SeasonDayTypeSchedule import SeasonDayTypeSchedule


class SwitchSchedule(SeasonDayTypeSchedule):
	'''
	A schedule of switch positions.  If RegularTimePoint.value1 is 0, the switch is open.  If 1, the switch is closed.

	:Switch: A Switch can be associated with SwitchSchedules. Default: 
		'''

	cgmesProfile = SeasonDayTypeSchedule.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'Switch': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class SeasonDayTypeSchedule: \n' + SeasonDayTypeSchedule.__doc__ 

	def __init__(self, Switch = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.Switch = Switch
		
	def __str__(self):
		str = 'class=SwitchSchedule\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
