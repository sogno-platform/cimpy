from .LimitSet import LimitSet


class AnalogLimitSet(LimitSet):
	'''
	An AnalogLimitSet specifies a set of Limits that are associated with an Analog measurement.

	:Measurements: A measurement may have zero or more limit ranges defined for it. Default: "list"
	:Limits: The set of limits. Default: "list"
		'''

	cgmesProfile = LimitSet.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'Measurements': [cgmesProfile.EQ.value, ],
						'Limits': [cgmesProfile.EQ.value, ],
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
