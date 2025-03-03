from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class TopologicalIsland(IdentifiedObject):
    """
    An electrically connected subset of the network. Topological islands can change as the current network state changes: e.g. due to  - disconnect switches or breakers change state in a SCADA/EMS - manual creation, change or deletion of topological nodes in a planning tool.

    :AngleRefTopologicalNode: The angle reference for the island.   Normally there is one TopologicalNode that is selected as the angle reference for each island.   Other reference schemes exist, so the association is typically optional. Default: None
    :TopologicalNodes: A topological node belongs to a topological island. Default: "list"
    """

    possibleProfileList = {
        "class": [Profile.SV.value, ],
        "AngleRefTopologicalNode": [Profile.SV.value, ],
        "TopologicalNodes": [Profile.SV.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.SV.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, AngleRefTopologicalNode = None, TopologicalNodes = "list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.AngleRefTopologicalNode = AngleRefTopologicalNode
        self.TopologicalNodes = TopologicalNodes

    def __str__(self):
        str = "class=TopologicalIsland\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
