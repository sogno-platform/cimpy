from .MeasurementValue import MeasurementValue


class StringMeasurementValue(MeasurementValue):
	'''
	StringMeasurementValue represents a measurement value of type string.

	:StringMeasurement: Measurement to which this value is connected. Default: None
	:value: The value to supervise. Default: ''
		'''

	cgmesProfile = MeasurementValue.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'StringMeasurement': [cgmesProfile.EQ.value, ],
						'value': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class MeasurementValue: \n' + MeasurementValue.__doc__ 

	def __init__(self, StringMeasurement = None, value = '',  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.StringMeasurement = StringMeasurement
		self.value = value
		
	def __str__(self):
		str = 'class=StringMeasurementValue\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
