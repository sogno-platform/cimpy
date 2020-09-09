from .SeasonDayTypeSchedule import SeasonDayTypeSchedule


class TapSchedule(SeasonDayTypeSchedule):
	'''
	A pre-established pattern over time for a tap step.

	:TapChanger: A TapChanger can have TapSchedules. Default: None
		'''

	cgmesProfile = SeasonDayTypeSchedule.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'TapChanger': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class SeasonDayTypeSchedule: \n' + SeasonDayTypeSchedule.__doc__ 

	def __init__(self, TapChanger = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.TapChanger = TapChanger
		
	def __str__(self):
		str = 'class=TapSchedule\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
