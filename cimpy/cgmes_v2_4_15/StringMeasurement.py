from .Measurement import Measurement


class StringMeasurement(Measurement):
	'''
	StringMeasurement represents a measurement with values of type string.

	:StringMeasurementValues: The values connected to this measurement. Default: "list"
		'''

	cgmesProfile = Measurement.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'StringMeasurementValues': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class Measurement: \n' + Measurement.__doc__ 

	def __init__(self, StringMeasurementValues = "list",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.StringMeasurementValues = StringMeasurementValues
		
	def __str__(self):
		str = 'class=StringMeasurement\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
