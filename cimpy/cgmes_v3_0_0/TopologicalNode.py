from .IdentifiedObject import IdentifiedObject


class TopologicalNode(IdentifiedObject):
	'''
	For a detailed substation model a topological node is a set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes change as the current network state changes (i.e., switches, breakers, etc. change state). For a planning model, switch statuses are not used to form topological nodes. Instead they are manually created or deleted in a model builder tool. Topological nodes maintained this way are also called "busses".

	:BaseVoltage: The base voltage of the topological node. Default: None
	:ConnectivityNodes: The connectivity nodes combine together to form this topological node.  May depend on the current state of switches in the network. Default: "list"
	:ConnectivityNodeContainer: The connectivity node container to which the topological node belongs. Default: None
	:Terminal: The terminals associated with the topological node.   This can be used as an alternative to the connectivity node path to terminal, thus making it unnecessary to model connectivity nodes in some cases.   Note that if connectivity nodes are in the model, this association would probably not be used as an input specification. Default: "list"
	:ReportingGroup: The reporting group to which the topological node belongs. Default: None
	:SvInjection: The injection flows state variables associated with the topological node. Default: None
	:SvVoltage: The state voltage associated with the topological node. Default: None
	:AngleRefTopologicalIsland: The island for which the node is an angle reference.   Normally there is one angle reference node for each island. Default: None
	:TopologicalIsland: A topological node belongs to a topological island. Default: None
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.TP.value, cgmesProfile.SV.value, ],
						'BaseVoltage': [cgmesProfile.TP.value, ],
						'ConnectivityNodes': [cgmesProfile.TP.value, ],
						'ConnectivityNodeContainer': [cgmesProfile.TP.value, ],
						'Terminal': [cgmesProfile.TP.value, ],
						'ReportingGroup': [cgmesProfile.TP.value, ],
						'SvInjection': [cgmesProfile.SV.value, ],
						'SvVoltage': [cgmesProfile.SV.value, ],
						'AngleRefTopologicalIsland': [cgmesProfile.SV.value, ],
						'TopologicalIsland': [cgmesProfile.SV.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, BaseVoltage = None, ConnectivityNodes = "list", ConnectivityNodeContainer = None, Terminal = "list", ReportingGroup = None, SvInjection = None, SvVoltage = None, AngleRefTopologicalIsland = None, TopologicalIsland = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.BaseVoltage = BaseVoltage
		self.ConnectivityNodes = ConnectivityNodes
		self.ConnectivityNodeContainer = ConnectivityNodeContainer
		self.Terminal = Terminal
		self.ReportingGroup = ReportingGroup
		self.SvInjection = SvInjection
		self.SvVoltage = SvVoltage
		self.AngleRefTopologicalIsland = AngleRefTopologicalIsland
		self.TopologicalIsland = TopologicalIsland
		
	def __str__(self):
		str = 'class=TopologicalNode\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
