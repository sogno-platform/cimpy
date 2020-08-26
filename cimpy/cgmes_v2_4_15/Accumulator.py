from cimpy.cgmes_v2_4_15.Measurement import Measurement


class Accumulator(Measurement):
	'''
	Accumulator represents an accumulated (counted) Measurement, e.g. an energy value.

	:LimitSets: The Measurements using the LimitSet. Default: 
	:AccumulatorValues: Measurement to which this value is connected. Default: 
		'''

	cgmesProfile = Measurement.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'LimitSets': [cgmesProfile.EQ.value, ],
						'AccumulatorValues': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class Measurement: \n' + Measurement.__doc__ 

	def __init__(self, LimitSets = , AccumulatorValues = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.LimitSets = LimitSets
		self.AccumulatorValues = AccumulatorValues
		
	def __str__(self):
		str = 'class=Accumulator\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
