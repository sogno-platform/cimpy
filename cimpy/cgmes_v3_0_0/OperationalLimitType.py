from .IdentifiedObject import IdentifiedObject


class OperationalLimitType(IdentifiedObject):
	'''
	The operational meaning of a category of limits.

	:OperationalLimit: The operational limits associated with this type of limit. Default: "list"
	:acceptableDuration: The nominal acceptable duration of the limit. Limits are commonly expressed in terms of the time limit for which the limit is normally acceptable. The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed. The attribute has meaning only if the flag isInfiniteDuration is set to false, hence it shall not be exchanged when isInfiniteDuration is set to true. Default: 0
	:direction: The direction of the limit. Default: None
	:isInfiniteDuration: Defines if the operational limit type has infinite duration. If true, the limit has infinite duration. If false, the limit has definite duration which is defined by the attribute acceptableDuration. Default: False
	:kind: Types of limits defined in the ENTSO-E Operational Handbook Policy 3. Default: None
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'OperationalLimit': [cgmesProfile.EQ.value, ],
						'acceptableDuration': [cgmesProfile.EQ.value, ],
						'direction': [cgmesProfile.EQ.value, ],
						'isInfiniteDuration': [cgmesProfile.EQ.value, ],
						'kind': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, OperationalLimit = "list", acceptableDuration = 0, direction = None, isInfiniteDuration = False, kind = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.OperationalLimit = OperationalLimit
		self.acceptableDuration = acceptableDuration
		self.direction = direction
		self.isInfiniteDuration = isInfiniteDuration
		self.kind = kind
		
	def __str__(self):
		str = 'class=OperationalLimitType\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
