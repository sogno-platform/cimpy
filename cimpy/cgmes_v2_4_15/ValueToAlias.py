from cimpy.output.IdentifiedObject import IdentifiedObject


class ValueToAlias(IdentifiedObject):
	'''
	Describes the translation of one particular value into a name, e.g. 1 as "Open".

	:ValueAliasSet: The ValueToAlias mappings included in the set. Default: 
	:value: The value that is mapped. Default: 
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'ValueAliasSet': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'value': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, ValueAliasSet = , value = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ValueAliasSet = ValueAliasSet
		self.value = value
		
	def __str__(self):
		str = 'class=ValueToAlias\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
