from .SeasonDayTypeSchedule import SeasonDayTypeSchedule


class ConformLoadSchedule(SeasonDayTypeSchedule):
	'''
	A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for each unit of the period covered. This curve represents a typical pattern of load over the time period for a given day type and season.

	:ConformLoadGroup: The ConformLoadGroup where the ConformLoadSchedule belongs. Default: None
		'''

	cgmesProfile = SeasonDayTypeSchedule.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'ConformLoadGroup': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class SeasonDayTypeSchedule: \n' + SeasonDayTypeSchedule.__doc__ 

	def __init__(self, ConformLoadGroup = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ConformLoadGroup = ConformLoadGroup
		
	def __str__(self):
		str = 'class=ConformLoadSchedule\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
