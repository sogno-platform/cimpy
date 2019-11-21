from cimpy.cgmes_v2_4_15_flat.Base import Base


class TopologicalNode(Base):
	'''
	For a detailed substation model a topological node is a set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes change as the current network state changes (i.e., switches, breakers, etc. change state). For a planning model, switch statuses are not used to form topological nodes. Instead they are manually created or deleted in a model builder tool. Topological nodes maintained this way are also called "busses".

	:SvInjection: The topological node associated with the flow injection state variable. Default: None
	:SvVoltage: The topological node associated with the voltage state. Default: None
	:AngleRefTopologicalIsland: The island for which the node is an angle reference.   Normally there is one angle reference node for each island. Default: None
	:TopologicalIsland: A topological node belongs to a topological island. Default: None
	:BaseVoltage: The base voltage of the topologocial node. Default: None
	:ConnectivityNodes: The topological node to which this connectivity node is assigned.  May depend on the current state of switches in the network. Default: []
	:ConnectivityNodeContainer: The connectivity node container to which the toplogical node belongs. Default: None
	:ReportingGroup: The topological nodes that belong to the reporting group. Default: None
	:Terminal: The topological node associated with the terminal.   This can be used as an alternative to the connectivity node path to topological node, thus making it unneccesary to model connectivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would probably not be used as an input specification. Default: []
		'''

	possibleProfileList = {'class': [cgmesProfile.SV.value, cgmesProfile.TP.value, ],
						'SvInjection': [cgmesProfile.SV.value, ],
						'SvVoltage': [cgmesProfile.SV.value, ],
						'AngleRefTopologicalIsland': [cgmesProfile.SV.value, ],
						'TopologicalIsland': [cgmesProfile.SV.value, ],
						'BaseVoltage': [cgmesProfile.TP.value, ],
						'ConnectivityNodes': [cgmesProfile.TP.value, ],
						'ConnectivityNodeContainer': [cgmesProfile.TP.value, ],
						'ReportingGroup': [cgmesProfile.TP.value, ],
						'Terminal': [cgmesProfile.TP.value, ],
						 }

	readInProfile = {}

	

	def __init__(self, SvInjection = None, SvVoltage = None, AngleRefTopologicalIsland = None, TopologicalIsland = None, BaseVoltage = None, ConnectivityNodes = [], ConnectivityNodeContainer = None, ReportingGroup = None, Terminal = [],  ):
	
		self.SvInjection = SvInjection
		self.SvVoltage = SvVoltage
		self.AngleRefTopologicalIsland = AngleRefTopologicalIsland
		self.TopologicalIsland = TopologicalIsland
		self.BaseVoltage = BaseVoltage
		self.ConnectivityNodes = ConnectivityNodes
		self.ConnectivityNodeContainer = ConnectivityNodeContainer
		self.ReportingGroup = ReportingGroup
		self.Terminal = Terminal
		
	def __str__(self):
		str = 'class=TopologicalNode\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
