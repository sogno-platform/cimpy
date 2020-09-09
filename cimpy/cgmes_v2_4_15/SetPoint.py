from .AnalogControl import AnalogControl


class SetPoint(AnalogControl):
	'''
	An analog control that issue a set point value.

	:normalValue: Normal value for Control.value e.g. used for percentage scaling. Default: 0.0
	:value: The value representing the actuator output. Default: 0.0
		'''

	cgmesProfile = AnalogControl.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'normalValue': [cgmesProfile.EQ.value, ],
						'value': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class AnalogControl: \n' + AnalogControl.__doc__ 

	def __init__(self, normalValue = 0.0, value = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.normalValue = normalValue
		self.value = value
		
	def __str__(self):
		str = 'class=SetPoint\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
