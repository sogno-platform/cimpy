from .MeasurementValue import MeasurementValue


class AccumulatorValue(MeasurementValue):
	'''
	AccumulatorValue represents an accumulated (counted) MeasurementValue.

	:Accumulator: Measurement to which this value is connected. Default: None
	:AccumulatorReset: The command that resets the accumulator value. Default: None
		'''

	cgmesProfile = MeasurementValue.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.OP.value, ],
						'Accumulator': [cgmesProfile.OP.value, ],
						'AccumulatorReset': [cgmesProfile.OP.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class MeasurementValue: \n' + MeasurementValue.__doc__ 

	def __init__(self, Accumulator = None, AccumulatorReset = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.Accumulator = Accumulator
		self.AccumulatorReset = AccumulatorReset
		
	def __str__(self):
		str = 'class=AccumulatorValue\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
