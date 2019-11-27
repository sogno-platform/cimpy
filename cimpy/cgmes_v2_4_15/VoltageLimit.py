from cimpy.cgmes_v2_4_15.OperationalLimit import OperationalLimit


class VoltageLimit(OperationalLimit):
	'''
	Operational limit applied to voltage.

	:value: Limit on voltage. High or low limit nature of the limit depends upon the properties of the operational limit type. Default: 0.0
		'''

	cgmesProfile = OperationalLimit.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'value': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class OperationalLimit: \n' + OperationalLimit.__doc__ 

	def __init__(self, value = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.value = value
		
	def __str__(self):
		str = 'class=VoltageLimit\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
