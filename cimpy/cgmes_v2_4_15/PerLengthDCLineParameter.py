from  import Base


class PerLengthDCLineParameter(Base):
	'''
	

	:DCLineSegments: All line segments described by this set of per-length parameters. Default: 
	:capacitance: Capacitance per unit of length of the DC line segment; significant for cables only. Default: 
	:inductance: Inductance per unit of length of the DC line segment. Default: 
	:resistance: Resistance per length of the DC line segment. Default: 
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'DCLineSegments': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'capacitance': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'inductance': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'resistance': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, DCLineSegments = , capacitance = , inductance = , resistance = ,  ):
	
		self.DCLineSegments = DCLineSegments
		self.capacitance = capacitance
		self.inductance = inductance
		self.resistance = resistance
		
	def __str__(self):
		str = 'class=PerLengthDCLineParameter\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
