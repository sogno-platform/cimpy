from cimpy.cgmes_v2_4_15.IdentifiedObject import IdentifiedObject


class OperationalLimitSet(IdentifiedObject):
	'''
	A set of limits associated with equipment.  Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain different severities of limit levels that would apply to the same equipment. The set may contain limits of different types such as apparent power and current limits or high and low voltage limits  that are logically applied together as a set.

	:Terminal:  Default: None
	:Equipment: The equipment to which the limit set applies. Default: None
	:OperationalLimitValue: The limit set to which the limit values belong. Default: "many"
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'Terminal': [cgmesProfile.EQ.value, ],
						'Equipment': [cgmesProfile.EQ.value, ],
						'OperationalLimitValue': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, Terminal = None, Equipment = None, OperationalLimitValue = "many",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.Terminal = Terminal
		self.Equipment = Equipment
		self.OperationalLimitValue = OperationalLimitValue
		
	def __str__(self):
		str = 'class=OperationalLimitSet\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
