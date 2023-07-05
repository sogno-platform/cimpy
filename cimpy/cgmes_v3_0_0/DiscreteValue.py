from .MeasurementValue import MeasurementValue


class DiscreteValue(MeasurementValue):
	'''
	DiscreteValue represents a discrete MeasurementValue.

	:Command: The Control variable associated with the MeasurementValue. Default: None
	:Discrete: Measurement to which this value is connected. Default: None
		'''

	cgmesProfile = MeasurementValue.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.OP.value, ],
						'Command': [cgmesProfile.OP.value, ],
						'Discrete': [cgmesProfile.OP.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class MeasurementValue: \n' + MeasurementValue.__doc__ 

	def __init__(self, Command = None, Discrete = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.Command = Command
		self.Discrete = Discrete
		
	def __str__(self):
		str = 'class=DiscreteValue\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
