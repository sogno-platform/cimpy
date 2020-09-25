from .IdentifiedObject import IdentifiedObject


class LimitSet(IdentifiedObject):
	'''
	Specifies a set of Limits that are associated with a Measurement. A Measurement may have several LimitSets corresponding to seasonal or other changing conditions. The condition is captured in the name and description attributes. The same LimitSet may be used for several Measurements. In particular percentage limits are used this way.

	:isPercentageLimits: Tells if the limit values are in percentage of normalValue or the specified Unit for Measurements and Controls. Default: False
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'isPercentageLimits': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, isPercentageLimits = False,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.isPercentageLimits = isPercentageLimits
		
	def __str__(self):
		str = 'class=LimitSet\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
