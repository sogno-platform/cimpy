from .IdentifiedObject import IdentifiedObject


class ConnectivityNode(IdentifiedObject):
	'''
	Connectivity nodes are points where terminals of AC conducting equipment are connected together with zero impedance.

	:Terminals: The connectivity node to which this terminal connects with zero impedance. Default: "list"
	:ConnectivityNodeContainer: Container of this connectivity node. Default: None
	:TopologicalNode: The connectivity nodes combine together to form this topological node.  May depend on the current state of switches in the network. Default: None
	:boundaryPoint: Identifies if a node is a BoundaryPoint. If boundaryPoint=true the ConnectivityNode or the TopologicalNode represents a BoundaryPoint. Default: False
	:fromEndIsoCode: The attribute is used for an exchange of the ISO code of the region to which the `From` side of the Boundary point belongs to or it is connected to. The ISO code is two characters country code as defined by ISO 3166 (). The length of the string is 2 characters maximum. The attribute is a required for the Boundary Model Authority Set where this attribute is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: ''
	:fromEndName: The attribute is used for an exchange of a human readable name with length of the string 32 characters maximum. The attribute covers two cases:  The attribute is required for the Boundary Model Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: ''
	:fromEndNameTso: The attribute is used for an exchange of the name of the TSO to which the `From` side of the Boundary point belongs to or it is connected to. The length of the string is 32 characters maximum. The attribute is required for the Boundary Model Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: ''
	:toEndIsoCode: The attribute is used for an exchange of the ISO code of the region to which the `To` side of the Boundary point belongs to or it is connected to. The ISO code is two characters country code as defined by ISO 3166 (). The length of the string is 2 characters maximum. The attribute is a required for the Boundary Model Authority Set where this attribute is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: ''
	:toEndName: The attribute is used for an exchange of a human readable name with length of the string 32 characters maximum. The attribute covers two cases:  The attribute is required for the Boundary Model Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: ''
	:toEndNameTso: The attribute is used for an exchange of the name of the TSO to which the `To` side of the Boundary point belongs to or it is connected to. The length of the string is 32 characters maximum. The attribute is required for the Boundary Model Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: ''
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.TP.value, cgmesProfile.TP_BD.value, cgmesProfile.EQ_BD.value, ],
						'Terminals': [cgmesProfile.EQ.value, ],
						'ConnectivityNodeContainer': [cgmesProfile.EQ.value, cgmesProfile.EQ_BD.value, ],
						'TopologicalNode': [cgmesProfile.TP.value, cgmesProfile.TP_BD.value, ],
						'boundaryPoint': [cgmesProfile.EQ_BD.value, ],
						'fromEndIsoCode': [cgmesProfile.EQ_BD.value, ],
						'fromEndName': [cgmesProfile.EQ_BD.value, ],
						'fromEndNameTso': [cgmesProfile.EQ_BD.value, ],
						'toEndIsoCode': [cgmesProfile.EQ_BD.value, ],
						'toEndName': [cgmesProfile.EQ_BD.value, ],
						'toEndNameTso': [cgmesProfile.EQ_BD.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, Terminals = "list", ConnectivityNodeContainer = None, TopologicalNode = None, boundaryPoint = False, fromEndIsoCode = '', fromEndName = '', fromEndNameTso = '', toEndIsoCode = '', toEndName = '', toEndNameTso = '',  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.Terminals = Terminals
		self.ConnectivityNodeContainer = ConnectivityNodeContainer
		self.TopologicalNode = TopologicalNode
		self.boundaryPoint = boundaryPoint
		self.fromEndIsoCode = fromEndIsoCode
		self.fromEndName = fromEndName
		self.fromEndNameTso = fromEndNameTso
		self.toEndIsoCode = toEndIsoCode
		self.toEndName = toEndName
		self.toEndNameTso = toEndNameTso
		
	def __str__(self):
		str = 'class=ConnectivityNode\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
