from .Measurement import Measurement


class Analog(Measurement):
	'''
	Analog represents an analog Measurement.

	:positiveFlowIn: If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource. Default: False
	:AnalogValues: Measurement to which this value is connected. Default: "list"
	:LimitSets: The Measurements using the LimitSet. Default: "list"
		'''

	cgmesProfile = Measurement.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'positiveFlowIn': [cgmesProfile.EQ.value, ],
						'AnalogValues': [cgmesProfile.EQ.value, ],
						'LimitSets': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class Measurement: \n' + Measurement.__doc__ 

	def __init__(self, positiveFlowIn = False, AnalogValues = "list", LimitSets = "list",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.positiveFlowIn = positiveFlowIn
		self.AnalogValues = AnalogValues
		self.LimitSets = LimitSets
		
	def __str__(self):
		str = 'class=Analog\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
