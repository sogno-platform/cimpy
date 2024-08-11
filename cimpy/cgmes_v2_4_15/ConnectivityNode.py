from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class ConnectivityNode(IdentifiedObject):
    """
    Connectivity nodes are points where terminals of AC conducting equipment are connected together with zero impedance.

    :ConnectivityNodeContainer: Container of this connectivity node. Default: None
    :Terminals: The connectivity node to which this terminal connects with zero impedance. Default: "list"
    :TopologicalNode: The topological node to which this connectivity node is assigned.  May depend on the current state of switches in the network. Default: None
    :boundaryPoint: Identifies if a node is a BoundaryPoint. If boundaryPoint=true the ConnectivityNode or the TopologicalNode represents a BoundaryPoint. Default: False
    :fromEndIsoCode: The attribute is used for an exchange of the ISO code of the region to which the `From` side of the Boundary point belongs to or it is connected to. The ISO code is two characters country code as defined by ISO 3166 (). The length of the string is 2 characters maximum. The attribute is a required for the Boundary Model Authority Set where this attribute is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: ''
    :fromEndName: The attribute is used for an exchange of a human readable name with length of the string 32 characters maximum. The attribute covers two cases:  The attribute is required for the Boundary Model Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: ''
    :fromEndNameTso: The attribute is used for an exchange of the name of the TSO to which the `From` side of the Boundary point belongs to or it is connected to. The length of the string is 32 characters maximum. The attribute is required for the Boundary Model Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: ''
    :toEndIsoCode: The attribute is used for an exchange of the ISO code of the region to which the `To` side of the Boundary point belongs to or it is connected to. The ISO code is two characters country code as defined by ISO 3166 (). The length of the string is 2 characters maximum. The attribute is a required for the Boundary Model Authority Set where this attribute is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: ''
    :toEndName: The attribute is used for an exchange of a human readable name with length of the string 32 characters maximum. The attribute covers two cases:  The attribute is required for the Boundary Model Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: ''
    :toEndNameTso: The attribute is used for an exchange of the name of the TSO to which the `To` side of the Boundary point belongs to or it is connected to. The length of the string is 32 characters maximum. The attribute is required for the Boundary Model Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment profile. Default: ''
    """

    possibleProfileList = {
        "class": [Profile.EQ_BD.value, Profile.EQ.value, Profile.TP_BD.value, Profile.TP.value, ],
        "ConnectivityNodeContainer": [Profile.EQ_BD.value, Profile.EQ.value, ],
        "Terminals": [Profile.EQ.value, ],
        "TopologicalNode": [Profile.TP_BD.value, Profile.TP.value, ],
        "boundaryPoint": [Profile.EQ_BD.value, ],
        "fromEndIsoCode": [Profile.EQ_BD.value, ],
        "fromEndName": [Profile.EQ_BD.value, ],
        "fromEndNameTso": [Profile.EQ_BD.value, ],
        "toEndIsoCode": [Profile.EQ_BD.value, ],
        "toEndName": [Profile.EQ_BD.value, ],
        "toEndNameTso": [Profile.EQ_BD.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, ConnectivityNodeContainer = None, Terminals = "list", TopologicalNode = None, boundaryPoint = False, fromEndIsoCode = '', fromEndName = '', fromEndNameTso = '', toEndIsoCode = '', toEndName = '', toEndNameTso = '', *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ConnectivityNodeContainer = ConnectivityNodeContainer
        self.Terminals = Terminals
        self.TopologicalNode = TopologicalNode
        self.boundaryPoint = boundaryPoint
        self.fromEndIsoCode = fromEndIsoCode
        self.fromEndName = fromEndName
        self.fromEndNameTso = fromEndNameTso
        self.toEndIsoCode = toEndIsoCode
        self.toEndName = toEndName
        self.toEndNameTso = toEndNameTso

    def __str__(self):
        str = "class=ConnectivityNode\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
