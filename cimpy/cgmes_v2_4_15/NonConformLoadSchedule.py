from .SeasonDayTypeSchedule import SeasonDayTypeSchedule


class NonConformLoadSchedule(SeasonDayTypeSchedule):
	'''
	An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus time (X-axis) for non-conforming loads, e.g., large industrial load or power station service (where modeled).

	:NonConformLoadGroup: The NonConformLoadGroup where the NonConformLoadSchedule belongs. Default: None
		'''

	cgmesProfile = SeasonDayTypeSchedule.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'NonConformLoadGroup': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class SeasonDayTypeSchedule: \n' + SeasonDayTypeSchedule.__doc__ 

	def __init__(self, NonConformLoadGroup = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.NonConformLoadGroup = NonConformLoadGroup
		
	def __str__(self):
		str = 'class=NonConformLoadSchedule\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
