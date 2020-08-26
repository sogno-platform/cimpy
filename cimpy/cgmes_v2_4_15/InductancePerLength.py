from  import Base


class InductancePerLength(Base):
	'''
	Inductance per unit of length.

	:value:  Default: 
	:unit:  Default: 
	:multiplier:  Default: 
	:denominatorUnit:  Default: 
	:denominatorMultiplier:  Default: 
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'value': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'unit': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'multiplier': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'denominatorUnit': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'denominatorMultiplier': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, value = , unit = , multiplier = , denominatorUnit = , denominatorMultiplier = ,  ):
	
		self.value = value
		self.unit = unit
		self.multiplier = multiplier
		self.denominatorUnit = denominatorUnit
		self.denominatorMultiplier = denominatorMultiplier
		
	def __str__(self):
		str = 'class=InductancePerLength\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
