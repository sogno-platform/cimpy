from .IdentifiedObject import IdentifiedObject


class OperationalLimit(IdentifiedObject):
	'''
	A value and normal value associated with a specific kind of limit.  The sub class value and normalValue attributes vary inversely to the associated OperationalLimitType.acceptableDuration (acceptableDuration for short).   If a particular piece of equipment has multiple operational limits of the same kind (apparent power, current, etc.), the limit with the greatest acceptableDuration shall have the smallest limit value and the limit with the smallest acceptableDuration shall have the largest limit value.  Note: A large current can only be allowed to flow through a piece of equipment for a short duration without causing damage, but a lesser current can be allowed to flow for a longer duration.

	:OperationalLimitSet: The limit set to which the limit values belong. Default: None
	:OperationalLimitType: The limit type associated with this limit. Default: None
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.SSH.value, cgmesProfile.EQ.value, ],
						'OperationalLimitSet': [cgmesProfile.EQ.value, ],
						'OperationalLimitType': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

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
