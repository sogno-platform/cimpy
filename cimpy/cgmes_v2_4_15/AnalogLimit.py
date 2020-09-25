from .Limit import Limit


class AnalogLimit(Limit):
	'''
	Limit values for Analog measurements.

	:value: The value to supervise against. Default: 0.0
	:LimitSet: The limit values used for supervision of Measurements. Default: None
		'''

	cgmesProfile = Limit.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'value': [cgmesProfile.EQ.value, ],
						'LimitSet': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class Limit: \n' + Limit.__doc__ 

	def __init__(self, value = 0.0, LimitSet = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.value = value
		self.LimitSet = LimitSet
		
	def __str__(self):
		str = 'class=AnalogLimit\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
