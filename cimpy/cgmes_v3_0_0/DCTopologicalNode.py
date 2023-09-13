from .IdentifiedObject import IdentifiedObject


class DCTopologicalNode(IdentifiedObject):
	'''
	DC bus.

	:DCTerminals: See association end TopologicalNode.Terminal. Default: "list"
	:DCEquipmentContainer: The connectivity node container to which the topological node belongs. Default: None
	:DCNodes: The DC connectivity nodes combined together to form this DC topological node.  May depend on the current state of switches in the network. Default: "list"
	:DCTopologicalIsland: A DC topological node belongs to a DC topological island. Default: None
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.TP.value, cgmesProfile.SV.value, ],
						'DCTerminals': [cgmesProfile.TP.value, ],
						'DCEquipmentContainer': [cgmesProfile.TP.value, ],
						'DCNodes': [cgmesProfile.TP.value, ],
						'DCTopologicalIsland': [cgmesProfile.SV.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, DCTerminals = "list", DCEquipmentContainer = None, DCNodes = "list", DCTopologicalIsland = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.DCTerminals = DCTerminals
		self.DCEquipmentContainer = DCEquipmentContainer
		self.DCNodes = DCNodes
		self.DCTopologicalIsland = DCTopologicalIsland
		
	def __str__(self):
		str = 'class=DCTopologicalNode\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
