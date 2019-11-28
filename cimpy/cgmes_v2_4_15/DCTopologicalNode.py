from cimpy.cgmes_v2_4_15.IdentifiedObject import IdentifiedObject


class DCTopologicalNode(IdentifiedObject):
	'''
	DC bus.

	:DCTopologicalIsland:  Default: None
	:DCTerminals: See association end Terminal.TopologicalNode. Default: "many"
	:DCEquipmentContainer:  Default: None
	:DCNodes: See association end ConnectivityNode.TopologicalNode. Default: "many"
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.SV.value, cgmesProfile.TP.value, ],
						'DCTopologicalIsland': [cgmesProfile.SV.value, ],
						'DCTerminals': [cgmesProfile.TP.value, ],
						'DCEquipmentContainer': [cgmesProfile.TP.value, ],
						'DCNodes': [cgmesProfile.TP.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, DCTopologicalIsland = None, DCTerminals = "many", DCEquipmentContainer = None, DCNodes = "many",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.DCTopologicalIsland = DCTopologicalIsland
		self.DCTerminals = DCTerminals
		self.DCEquipmentContainer = DCEquipmentContainer
		self.DCNodes = DCNodes
		
	def __str__(self):
		str = 'class=DCTopologicalNode\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
