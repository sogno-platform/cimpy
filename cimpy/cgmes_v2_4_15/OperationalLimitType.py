from cimpy.cgmes_v2_4_15_flat.IdentifiedObject import IdentifiedObject


class OperationalLimitType(IdentifiedObject):
	'''
	The operational meaning of a category of limits.

	:OperationalLimit: The operational limits associated with this type of limit. Default: []
	:acceptableDuration: The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed. Default: 0.0
	:limitType: Types of limits defined in the ENTSO-E Operational Handbook Policy 3. Default: None
	:direction: The direction of the limit. Default: None
		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'OperationalLimit': [cgmesProfile.EQ.value, ],
						'acceptableDuration': [cgmesProfile.EQ.value, ],
						'limitType': [cgmesProfile.EQ.value, ],
						'direction': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, OperationalLimit = [], acceptableDuration = 0.0, limitType = None, direction = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.OperationalLimit = OperationalLimit
		self.acceptableDuration = acceptableDuration
		self.limitType = limitType
		self.direction = direction
		
	def __str__(self):
		str = 'class=OperationalLimitType\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
