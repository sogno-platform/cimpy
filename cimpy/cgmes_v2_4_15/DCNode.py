from cimpy.output.IdentifiedObject import IdentifiedObject


class DCNode(IdentifiedObject):
	'''
	DC nodes are points where terminals of DC conducting equipment are connected together with zero impedance.

	:DCTerminals:  Default: 
	:DCEquipmentContainer:  Default: 
	:DCTopologicalNode: See association end TopologicalNode.ConnectivityNodes. Default: 
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'TP'}.value, ],
						'DCTerminals': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'DCEquipmentContainer': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'DCTopologicalNode': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'TP'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, DCTerminals = , DCEquipmentContainer = , DCTopologicalNode = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.DCTerminals = DCTerminals
		self.DCEquipmentContainer = DCEquipmentContainer
		self.DCTopologicalNode = DCTopologicalNode
		
	def __str__(self):
		str = 'class=DCNode\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
