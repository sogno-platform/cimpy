from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class DCNode(IdentifiedObject):
    """
    DC nodes are points where terminals of DC conducting equipment are connected together with zero impedance.

    :DCEquipmentContainer:  Default: None
    :DCTerminals:  Default: "list"
    :DCTopologicalNode: See association end TopologicalNode.ConnectivityNodes. Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, Profile.TP.value, ],
        "DCEquipmentContainer": [Profile.EQ.value, ],
        "DCTerminals": [Profile.EQ.value, ],
        "DCTopologicalNode": [Profile.TP.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, DCEquipmentContainer = None, DCTerminals = "list", DCTopologicalNode = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.DCEquipmentContainer = DCEquipmentContainer
        self.DCTerminals = DCTerminals
        self.DCTopologicalNode = DCTopologicalNode

    def __str__(self):
        str = "class=DCNode\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
