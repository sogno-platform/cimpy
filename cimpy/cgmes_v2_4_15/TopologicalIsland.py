from cimpy.cgmes_v2_4_15.IdentifiedObject import IdentifiedObject


class TopologicalIsland(IdentifiedObject):
	'''
	An electrically connected subset of the network. Topological islands can change as the current network state changes: e.g. due to  - disconnect switches or breakers change state in a SCADA/EMS - manual creation, change or deletion of topological nodes in a planning tool.

	:AngleRefTopologicalNode: The angle reference for the island.   Normally there is one TopologicalNode that is selected as the angle reference for each island.   Other reference schemes exist, so the association is typically optional. Default: None
	:TopologicalNodes: A topological node belongs to a topological island. Default: "many"
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.SV.value, ],
						'AngleRefTopologicalNode': [cgmesProfile.SV.value, ],
						'TopologicalNodes': [cgmesProfile.SV.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, AngleRefTopologicalNode = None, TopologicalNodes = "many",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.AngleRefTopologicalNode = AngleRefTopologicalNode
		self.TopologicalNodes = TopologicalNodes
		
	def __str__(self):
		str = 'class=TopologicalIsland\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
