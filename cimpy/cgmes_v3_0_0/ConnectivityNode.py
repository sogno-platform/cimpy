from .IdentifiedObject import IdentifiedObject


class ConnectivityNode(IdentifiedObject):
	'''
	Connectivity nodes are points where terminals of AC conducting equipment are connected together with zero impedance.

	:TopologicalNode: The topological node to which this connectivity node is assigned.  May depend on the current state of switches in the network. Default: None
	:BoundaryPoint: The boundary point associated with the connectivity node. Default: None
	:Terminals: Terminals interconnected with zero impedance at a this connectivity node. Default: "list"
	:ConnectivityNodeContainer: Container of this connectivity node. Default: None
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.TP.value, cgmesProfile.EQ.value, cgmesProfile.EQBD.value, ],
						'TopologicalNode': [cgmesProfile.TP.value, ],
						'BoundaryPoint': [cgmesProfile.EQ.value, cgmesProfile.EQBD.value, ],
						'Terminals': [cgmesProfile.EQ.value, cgmesProfile.EQBD.value, ],
						'ConnectivityNodeContainer': [cgmesProfile.EQ.value, cgmesProfile.EQBD.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, TopologicalNode = None, BoundaryPoint = None, Terminals = "list", ConnectivityNodeContainer = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.TopologicalNode = TopologicalNode
		self.BoundaryPoint = BoundaryPoint
		self.Terminals = Terminals
		self.ConnectivityNodeContainer = ConnectivityNodeContainer
		
	def __str__(self):
		str = 'class=ConnectivityNode\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
