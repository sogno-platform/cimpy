from .IdentifiedObject import IdentifiedObject


class MeasurementValue(IdentifiedObject):
	'''
	The current state for a measurement. A state value is an instance of a measurement from a specific source. Measurements can be associated with many state values, each representing a different source for the measurement.

	:timeStamp: The time when the value was last updated Default: ''
	:sensorAccuracy: The limit, expressed as a percentage of the sensor maximum, that errors will not exceed when the sensor is used under  reference conditions. Default: 0.0
	:MeasurementValueQuality: A MeasurementValue has a MeasurementValueQuality associated with it. Default: None
	:MeasurementValueSource: The MeasurementValues updated by the source. Default: None
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'timeStamp': [cgmesProfile.EQ.value, ],
						'sensorAccuracy': [cgmesProfile.EQ.value, ],
						'MeasurementValueQuality': [cgmesProfile.EQ.value, ],
						'MeasurementValueSource': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, timeStamp = '', sensorAccuracy = 0.0, MeasurementValueQuality = None, MeasurementValueSource = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.timeStamp = timeStamp
		self.sensorAccuracy = sensorAccuracy
		self.MeasurementValueQuality = MeasurementValueQuality
		self.MeasurementValueSource = MeasurementValueSource
		
	def __str__(self):
		str = 'class=MeasurementValue\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
