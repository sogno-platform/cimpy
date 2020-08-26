from  import Base


class SvVoltage(Base):
	'''
	State variable for voltage.

	:angle: The voltage angle of the topological node complex voltage with respect to system reference. Default: 
	:v: The voltage magnitude of the topological node. Default: 
	:TopologicalNode: The state voltage associated with the topological node. Default: 
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SV'}.value, ],
						'angle': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SV'}.value, ],
						'v': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SV'}.value, ],
						'TopologicalNode': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SV'}.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, angle = , v = , TopologicalNode = ,  ):
	
		self.angle = angle
		self.v = v
		self.TopologicalNode = TopologicalNode
		
	def __str__(self):
		str = 'class=SvVoltage\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
