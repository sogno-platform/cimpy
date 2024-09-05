from .IdentifiedObject import IdentifiedObject


class DCNode(IdentifiedObject):
    """
    DC nodes are points where terminals of DC conducting equipment are connected together with zero impedance.

    :DCTopologicalNode: The DC topological node to which this DC connectivity node is assigned.  May depend on the current state of switches in the network. Default: None
    :DCTerminals: DC base terminals interconnected with zero impedance at a this DC connectivity node. Default: "list"
    :DCEquipmentContainer: The DC container for the DC nodes. Default: None
    """

    cgmesProfile = IdentifiedObject.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.TP.value,
            cgmesProfile.EQ.value,
        ],
        "DCTopologicalNode": [
            cgmesProfile.TP.value,
        ],
        "DCTerminals": [
            cgmesProfile.EQ.value,
        ],
        "DCEquipmentContainer": [
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class IdentifiedObject: \n"
        + IdentifiedObject.__doc__
    )

    def __init__(
        self,
        DCTopologicalNode=None,
        DCTerminals="list",
        DCEquipmentContainer=None,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.DCTopologicalNode = DCTopologicalNode
        self.DCTerminals = DCTerminals
        self.DCEquipmentContainer = DCEquipmentContainer

    def __str__(self):
        str = "class=DCNode\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
