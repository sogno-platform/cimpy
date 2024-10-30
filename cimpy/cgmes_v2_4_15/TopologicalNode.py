from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class TopologicalNode(IdentifiedObject):
    """
    For a detailed substation model a topological node is a set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes change as the current network state changes (i.e., switches, breakers, etc. change state). For a planning model, switch statuses are not used to form topological nodes. Instead they are manually created or deleted in a model builder tool. Topological nodes maintained this way are also called "busses".

    :AngleRefTopologicalIsland: The island for which the node is an angle reference.   Normally there is one angle reference node for each island. Default: None
    :BaseVoltage: The base voltage of the topologocial node. Default: None
    :ConnectivityNodeContainer: The connectivity node container to which the toplogical node belongs. Default: None
    :ConnectivityNodes: The connectivity nodes combine together to form this topological node.  May depend on the current state of switches in the network. Default: "list"
    :ReportingGroup: The topological nodes that belong to the reporting group. Default: None
    :SvInjection: The topological node associated with the flow injection state variable. Default: None
    :SvVoltage: The topological node associated with the voltage state. Default: None
    :Terminal: The topological node associated with the terminal.   This can be used as an alternative to the connectivity node path to topological node, thus making it unneccesary to model connectivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would probably not be used as an input specification. Default: "list"
    :TopologicalIsland: A topological node belongs to a topological island. Default: None
    :boundaryPoint: Identifies if a node is a BoundaryPoint. If boundaryPoint=true the ConnectivityNode or the TopologicalNode represents a BoundaryPoint. Default: False
    :fromEndIsoCode: The attribute is used for an exchange of the ISO code of the region to which the `From` side of the Boundary point belongs to or it is connected to. The ISO code is two characters country code as defined by ISO 3166 (). The length of the string is 2 characters maximum. The attribute is a required for the Boundary Model Authority Set where this attribute is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: ''
    :fromEndName: The attribute is used for an exchange of a human readable name with length of the string 32 characters maximum. The attribute covers two cases:  The attribute is required for the Boundary Model Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: ''
    :fromEndNameTso: The attribute is used for an exchange of the name of the TSO to which the `From` side of the Boundary point belongs to or it is connected to. The length of the string is 32 characters maximum. The attribute is required for the Boundary Model Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: ''
    :toEndIsoCode: The attribute is used for an exchange of the ISO code of the region to which the `To` side of the Boundary point belongs to or it is connected to. The ISO code is two characters country code as defined by ISO 3166 (). The length of the string is 2 characters maximum. The attribute is a required for the Boundary Model Authority Set where this attribute is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: ''
    :toEndName: The attribute is used for an exchange of a human readable name with length of the string 32 characters maximum. The attribute covers two cases:  The attribute is required for the Boundary Model Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: ''
    :toEndNameTso: The attribute is used for an exchange of the name of the TSO to which the `To` side of the Boundary point belongs to or it is connected to. The length of the string is 32 characters maximum. The attribute is required for the Boundary Model Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: ''
    """

    possibleProfileList = {
        "class": [Profile.SV.value, Profile.TP_BD.value, Profile.TP.value, ],
        "AngleRefTopologicalIsland": [Profile.SV.value, ],
        "BaseVoltage": [Profile.TP_BD.value, Profile.TP.value, ],
        "ConnectivityNodeContainer": [Profile.TP_BD.value, Profile.TP.value, ],
        "ConnectivityNodes": [Profile.TP_BD.value, Profile.TP.value, ],
        "ReportingGroup": [Profile.TP.value, ],
        "SvInjection": [Profile.SV.value, ],
        "SvVoltage": [Profile.SV.value, ],
        "Terminal": [Profile.TP.value, ],
        "TopologicalIsland": [Profile.SV.value, ],
        "boundaryPoint": [Profile.TP_BD.value, ],
        "fromEndIsoCode": [Profile.TP_BD.value, ],
        "fromEndName": [Profile.TP_BD.value, ],
        "fromEndNameTso": [Profile.TP_BD.value, ],
        "toEndIsoCode": [Profile.TP_BD.value, ],
        "toEndName": [Profile.TP_BD.value, ],
        "toEndNameTso": [Profile.TP_BD.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.TP.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, AngleRefTopologicalIsland = None, BaseVoltage = None, ConnectivityNodeContainer = None, ConnectivityNodes = "list", ReportingGroup = None, SvInjection = None, SvVoltage = None, Terminal = "list", TopologicalIsland = None, boundaryPoint = False, fromEndIsoCode = '', fromEndName = '', fromEndNameTso = '', toEndIsoCode = '', toEndName = '', toEndNameTso = '', *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.AngleRefTopologicalIsland = AngleRefTopologicalIsland
        self.BaseVoltage = BaseVoltage
        self.ConnectivityNodeContainer = ConnectivityNodeContainer
        self.ConnectivityNodes = ConnectivityNodes
        self.ReportingGroup = ReportingGroup
        self.SvInjection = SvInjection
        self.SvVoltage = SvVoltage
        self.Terminal = Terminal
        self.TopologicalIsland = TopologicalIsland
        self.boundaryPoint = boundaryPoint
        self.fromEndIsoCode = fromEndIsoCode
        self.fromEndName = fromEndName
        self.fromEndNameTso = fromEndNameTso
        self.toEndIsoCode = toEndIsoCode
        self.toEndName = toEndName
        self.toEndNameTso = toEndNameTso

    def __str__(self):
        str = "class=TopologicalNode\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
