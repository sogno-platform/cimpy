from .EquipmentContainer import EquipmentContainer


class DCEquipmentContainer(EquipmentContainer):
    """
    A modelling construct to provide a root class for containment of DC as well as AC equipment. The class differ from the EquipmentContaner for AC in that it may also contain DCNode-s. Hence it can contain both AC and DC equipment.

    :DCTopologicalNode: The topological nodes which belong to this connectivity node container. Default: "list"
    :DCNodes: The DC nodes contained in the DC equipment container. Default: "list"
    """

    cgmesProfile = EquipmentContainer.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.TP.value,
            cgmesProfile.EQ.value,
        ],
        "DCTopologicalNode": [
            cgmesProfile.TP.value,
        ],
        "DCNodes": [
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class EquipmentContainer: \n"
        + EquipmentContainer.__doc__
    )

    def __init__(self, DCTopologicalNode="list", DCNodes="list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.DCTopologicalNode = DCTopologicalNode
        self.DCNodes = DCNodes

    def __str__(self):
        str = "class=DCEquipmentContainer\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
