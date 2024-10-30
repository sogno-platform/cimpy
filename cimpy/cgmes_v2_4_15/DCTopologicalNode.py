from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class DCTopologicalNode(IdentifiedObject):
    """
    DC bus.

    :DCEquipmentContainer:  Default: None
    :DCNodes: See association end ConnectivityNode.TopologicalNode. Default: "list"
    :DCTerminals: See association end Terminal.TopologicalNode. Default: "list"
    :DCTopologicalIsland:  Default: None
    """

    possibleProfileList = {
        "class": [Profile.SV.value, Profile.TP.value, ],
        "DCEquipmentContainer": [Profile.TP.value, ],
        "DCNodes": [Profile.TP.value, ],
        "DCTerminals": [Profile.TP.value, ],
        "DCTopologicalIsland": [Profile.SV.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.TP.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, DCEquipmentContainer = None, DCNodes = "list", DCTerminals = "list", DCTopologicalIsland = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.DCEquipmentContainer = DCEquipmentContainer
        self.DCNodes = DCNodes
        self.DCTerminals = DCTerminals
        self.DCTopologicalIsland = DCTopologicalIsland

    def __str__(self):
        str = "class=DCTopologicalNode\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
