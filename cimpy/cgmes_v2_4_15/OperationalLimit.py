from cimpy.cgmes_v2_4_15_flat.IdentifiedObject import IdentifiedObject


class OperationalLimit(IdentifiedObject):
	'''
	A value associated with a specific kind of limit.  The sub class value attribute shall be positive.  The sub class value attribute is inversely proportional to OperationalLimitType.acceptableDuration (acceptableDuration for short). A pair of value_x and acceptableDuration_x are related to each other as follows: if value_1 > value_2 > value_3 >... then acceptableDuration_1 < acceptableDuration_2 < acceptableDuration_3 < ... A value_x with direction="high" shall be greater than a value_y with direction="low".

	:OperationalLimitSet: Values of equipment limits. Default: None
	:OperationalLimitType: The limit type associated with this limit. Default: None
		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'OperationalLimitSet': [cgmesProfile.EQ.value, ],
						'OperationalLimitType': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, OperationalLimitSet = None, OperationalLimitType = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.OperationalLimitSet = OperationalLimitSet
		self.OperationalLimitType = OperationalLimitType
		
	def __str__(self):
		str = 'class=OperationalLimit\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
