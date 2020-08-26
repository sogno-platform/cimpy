from  import Base


class TieFlow(Base):
	'''
	A flow specification in terms of location and direction for a control area.

	:Terminal: The terminal to which this tie flow belongs. Default: 
	:ControlArea: The control area of the tie flows. Default: 
	:positiveFlowIn: True if the flow into the terminal (load convention) is also flow into the control area.  For example, this attribute should be true if using the tie line terminal further away from the control area. For example to represent a tie to a shunt component (like a load or generator) in another area, this is the near end of a branch and this attribute would be specified as false. Default: 
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'Terminal': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'ControlArea': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'positiveFlowIn': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, Terminal = , ControlArea = , positiveFlowIn = ,  ):
	
		self.Terminal = Terminal
		self.ControlArea = ControlArea
		self.positiveFlowIn = positiveFlowIn
		
	def __str__(self):
		str = 'class=TieFlow\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
