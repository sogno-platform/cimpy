from .MeasurementValue import MeasurementValue


class StringMeasurementValue(MeasurementValue):
	'''
	StringMeasurementValue represents a measurement value of type string.

	:StringMeasurement: Measurement to which this value is connected. Default: None
		'''

	cgmesProfile = MeasurementValue.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.OP.value, ],
						'StringMeasurement': [cgmesProfile.OP.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class MeasurementValue: \n' + MeasurementValue.__doc__ 

	def __init__(self, StringMeasurement = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.StringMeasurement = StringMeasurement
		
	def __str__(self):
		str = 'class=StringMeasurementValue\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
