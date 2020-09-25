from .IdentifiedObject import IdentifiedObject


class TopologicalNode(IdentifiedObject):
	'''
	For a detailed substation model a topological node is a set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes change as the current network state changes (i.e., switches, breakers, etc. change state). For a planning model, switch statuses are not used to form topological nodes. Instead they are manually created or deleted in a model builder tool. Topological nodes maintained this way are also called "busses".

	:SvInjection: The topological node associated with the flow injection state variable. Default: None
	:SvVoltage: The topological node associated with the voltage state. Default: None
	:AngleRefTopologicalIsland: The island for which the node is an angle reference.   Normally there is one angle reference node for each island. Default: None
	:TopologicalIsland: A topological node belongs to a topological island. Default: None
	:BaseVoltage: The base voltage of the topologocial node. Default: None
	:ConnectivityNodes: The topological node to which this connectivity node is assigned.  May depend on the current state of switches in the network. Default: "list"
	:ConnectivityNodeContainer: The connectivity node container to which the toplogical node belongs. Default: None
	:ReportingGroup: The topological nodes that belong to the reporting group. Default: None
	:Terminal: The topological node associated with the terminal.   This can be used as an alternative to the connectivity node path to topological node, thus making it unneccesary to model connectivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would probably not be used as an input specification. Default: "list"
	:boundaryPoint: Identifies if a node is a BoundaryPoint. If boundaryPoint=true the ConnectivityNode or the TopologicalNode represents a BoundaryPoint. Default: False
	:fromEndIsoCode: The attribute is used for an exchange of the ISO code of the region to which the `From` side of the Boundary point belongs to or it is connected to. The ISO code is two characters country code as defined by ISO 3166 (). The length of the string is 2 characters maximum. The attribute is a required for the Boundary Model Authority Set where this attribute is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: ''
	:fromEndName: The attribute is used for an exchange of a human readable name with length of the string 32 characters maximum. The attribute covers two cases:  The attribute is required for the Boundary Model Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: ''
	:fromEndNameTso: The attribute is used for an exchange of the name of the TSO to which the `From` side of the Boundary point belongs to or it is connected to. The length of the string is 32 characters maximum. The attribute is required for the Boundary Model Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: ''
	:toEndIsoCode: The attribute is used for an exchange of the ISO code of the region to which the `To` side of the Boundary point belongs to or it is connected to. The ISO code is two characters country code as defined by ISO 3166 (). The length of the string is 2 characters maximum. The attribute is a required for the Boundary Model Authority Set where this attribute is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: ''
	:toEndName: The attribute is used for an exchange of a human readable name with length of the string 32 characters maximum. The attribute covers two cases:  The attribute is required for the Boundary Model Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: ''
	:toEndNameTso: The attribute is used for an exchange of the name of the TSO to which the `To` side of the Boundary point belongs to or it is connected to. The length of the string is 32 characters maximum. The attribute is required for the Boundary Model Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: ''
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.SV.value, cgmesProfile.TP.value, cgmesProfile.TP_BD.value, ],
						'SvInjection': [cgmesProfile.SV.value, ],
						'SvVoltage': [cgmesProfile.SV.value, ],
						'AngleRefTopologicalIsland': [cgmesProfile.SV.value, ],
						'TopologicalIsland': [cgmesProfile.SV.value, ],
						'BaseVoltage': [cgmesProfile.TP.value, cgmesProfile.TP_BD.value, ],
						'ConnectivityNodes': [cgmesProfile.TP.value, cgmesProfile.TP_BD.value, ],
						'ConnectivityNodeContainer': [cgmesProfile.TP.value, cgmesProfile.TP_BD.value, ],
						'ReportingGroup': [cgmesProfile.TP.value, ],
						'Terminal': [cgmesProfile.TP.value, ],
						'boundaryPoint': [cgmesProfile.TP_BD.value, ],
						'fromEndIsoCode': [cgmesProfile.TP_BD.value, ],
						'fromEndName': [cgmesProfile.TP_BD.value, ],
						'fromEndNameTso': [cgmesProfile.TP_BD.value, ],
						'toEndIsoCode': [cgmesProfile.TP_BD.value, ],
						'toEndName': [cgmesProfile.TP_BD.value, ],
						'toEndNameTso': [cgmesProfile.TP_BD.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, SvInjection = None, SvVoltage = None, AngleRefTopologicalIsland = None, TopologicalIsland = None, BaseVoltage = None, ConnectivityNodes = "list", ConnectivityNodeContainer = None, ReportingGroup = None, Terminal = "list", boundaryPoint = False, fromEndIsoCode = '', fromEndName = '', fromEndNameTso = '', toEndIsoCode = '', toEndName = '', toEndNameTso = '',  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.SvInjection = SvInjection
		self.SvVoltage = SvVoltage
		self.AngleRefTopologicalIsland = AngleRefTopologicalIsland
		self.TopologicalIsland = TopologicalIsland
		self.BaseVoltage = BaseVoltage
		self.ConnectivityNodes = ConnectivityNodes
		self.ConnectivityNodeContainer = ConnectivityNodeContainer
		self.ReportingGroup = ReportingGroup
		self.Terminal = Terminal
		self.boundaryPoint = boundaryPoint
		self.fromEndIsoCode = fromEndIsoCode
		self.fromEndName = fromEndName
		self.fromEndNameTso = fromEndNameTso
		self.toEndIsoCode = toEndIsoCode
		self.toEndName = toEndName
		self.toEndNameTso = toEndNameTso
		
	def __str__(self):
		str = 'class=TopologicalNode\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
