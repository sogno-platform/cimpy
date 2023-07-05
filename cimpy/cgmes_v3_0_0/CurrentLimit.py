from .OperationalLimit import OperationalLimit


class CurrentLimit(OperationalLimit):
	'''
	Operational limit on current.

	:value: Limit on current flow. The attribute shall be a positive value or zero. Default: 0.0
	:normalValue: The normal value for limit on current flow. The attribute shall be a positive value or zero. Default: 0.0
		'''

	cgmesProfile = OperationalLimit.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.SSH.value, cgmesProfile.EQ.value, ],
						'value': [cgmesProfile.SSH.value, ],
						'normalValue': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class OperationalLimit: \n' + OperationalLimit.__doc__ 

	def __init__(self, value = 0.0, normalValue = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.value = value
		self.normalValue = normalValue
		
	def __str__(self):
		str = 'class=CurrentLimit\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
