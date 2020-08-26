from cimpy.output.IdentifiedObject import IdentifiedObject


class OperationalLimitSet(IdentifiedObject):
	'''
	A set of limits associated with equipment.  Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain different severities of limit levels that would apply to the same equipment. The set may contain limits of different types such as apparent power and current limits or high and low voltage limits  that are logically applied together as a set.

	:Terminal:  Default: 
	:Equipment: The equipment to which the limit set applies. Default: 
	:OperationalLimitValue: The limit set to which the limit values belong. Default: 
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'Terminal': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'Equipment': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'OperationalLimitValue': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, Terminal = , Equipment = , OperationalLimitValue = ,  *args, **kw_args):
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
