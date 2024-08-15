from .EquipmentContainer import EquipmentContainer
from .CGMESProfile import Profile


class DCEquipmentContainer(EquipmentContainer):
    """
    A modeling construct to provide a root class for containment of DC as well as AC equipment. The class differ from the EquipmentContaner for AC in that it may also contain DCNodes. Hence it can contain both AC and DC equipment.

    :DCNodes:  Default: "list"
    :DCTopologicalNode:  Default: "list"
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, Profile.TP.value, ],
        "DCNodes": [Profile.EQ.value, ],
        "DCTopologicalNode": [Profile.TP.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class EquipmentContainer:\n" + EquipmentContainer.__doc__

    def __init__(self, DCNodes = "list", DCTopologicalNode = "list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.DCNodes = DCNodes
        self.DCTopologicalNode = DCTopologicalNode

    def __str__(self):
        str = "class=DCEquipmentContainer\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
