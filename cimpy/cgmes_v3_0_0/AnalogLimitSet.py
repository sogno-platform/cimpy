from .LimitSet import LimitSet


class AnalogLimitSet(LimitSet):
	'''
	An AnalogLimitSet specifies a set of Limits that are associated with an Analog measurement.

	:Measurements: The Measurements using the LimitSet. Default: "list"
	:Limits: The limit values used for supervision of Measurements. Default: "list"
		'''

	cgmesProfile = LimitSet.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.OP.value, ],
						'Measurements': [cgmesProfile.OP.value, ],
						'Limits': [cgmesProfile.OP.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class LimitSet: \n' + LimitSet.__doc__ 

	def __init__(self, Measurements = "list", Limits = "list",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.Measurements = Measurements
		self.Limits = Limits
		
	def __str__(self):
		str = 'class=AnalogLimitSet\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
