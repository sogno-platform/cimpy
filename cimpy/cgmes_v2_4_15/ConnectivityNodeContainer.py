from cimpy.output.PowerSystemResource import PowerSystemResource


class ConnectivityNodeContainer(PowerSystemResource):
	'''
	A base class for all objects that may contain connectivity nodes or topological nodes.

	:ConnectivityNodes: Connectivity nodes which belong to this connectivity node container. Default: 
	:TopologicalNode: The topological nodes which belong to this connectivity node container. Default: 
		'''

	cgmesProfile = PowerSystemResource.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'TP'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'TP_BD'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ_BD'}.value, ],
						'ConnectivityNodes': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ_BD'}.value, ],
						'TopologicalNode': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'TP'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'TP_BD'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemResource: \n' + PowerSystemResource.__doc__ 

	def __init__(self, ConnectivityNodes = , TopologicalNode = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ConnectivityNodes = ConnectivityNodes
		self.TopologicalNode = TopologicalNode
		
	def __str__(self):
		str = 'class=ConnectivityNodeContainer\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
