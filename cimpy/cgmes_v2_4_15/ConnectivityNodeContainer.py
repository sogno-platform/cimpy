from .PowerSystemResource import PowerSystemResource
from .CGMESProfile import Profile


class ConnectivityNodeContainer(PowerSystemResource):
    """
    A base class for all objects that may contain connectivity nodes or topological nodes.

    :ConnectivityNodes: Connectivity nodes which belong to this connectivity node container. Default: "list"
    :TopologicalNode: The topological nodes which belong to this connectivity node container. Default: "list"
    """

    possibleProfileList = {
        "class": [Profile.EQ_BD.value, Profile.EQ.value, Profile.TP_BD.value, Profile.TP.value, ],
        "ConnectivityNodes": [Profile.EQ_BD.value, Profile.EQ.value, ],
        "TopologicalNode": [Profile.TP_BD.value, Profile.TP.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class PowerSystemResource:\n" + PowerSystemResource.__doc__

    def __init__(self, ConnectivityNodes = "list", TopologicalNode = "list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ConnectivityNodes = ConnectivityNodes
        self.TopologicalNode = TopologicalNode

    def __str__(self):
        str = "class=ConnectivityNodeContainer\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
