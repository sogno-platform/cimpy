from cimpy.output.MeasurementValue import MeasurementValue


class AnalogValue(MeasurementValue):
	'''
	AnalogValue represents an analog MeasurementValue.

	:Analog: The values connected to this measurement. Default: 
	:AnalogControl: The MeasurementValue that is controlled. Default: 
	:value: The value to supervise. Default: 
		'''

	cgmesProfile = MeasurementValue.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'Analog': [cgmesProfile.EQ.value, ],
						'AnalogControl': [cgmesProfile.EQ.value, ],
						'value': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class MeasurementValue: \n' + MeasurementValue.__doc__ 

	def __init__(self, Analog = , AnalogControl = , value = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.Analog = Analog
		self.AnalogControl = AnalogControl
		self.value = value
		
	def __str__(self):
		str = 'class=AnalogValue\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
