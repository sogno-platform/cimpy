from .PowerSystemResource import PowerSystemResource


class ConnectivityNodeContainer(PowerSystemResource):
    """
    A base class for all objects that may contain connectivity nodes or topological nodes.

    :TopologicalNode: The topological nodes which belong to this connectivity node container. Default: "list"
    :ConnectivityNodes: Connectivity nodes which belong to this connectivity node container. Default: "list"
    """

    cgmesProfile = PowerSystemResource.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.TP.value,
            cgmesProfile.EQ.value,
            cgmesProfile.EQBD.value,
        ],
        "TopologicalNode": [
            cgmesProfile.TP.value,
        ],
        "ConnectivityNodes": [
            cgmesProfile.EQ.value,
            cgmesProfile.EQBD.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class PowerSystemResource: \n"
        + PowerSystemResource.__doc__
    )

    def __init__(
        self, TopologicalNode="list", ConnectivityNodes="list", *args, **kw_args
    ):
        super().__init__(*args, **kw_args)

        self.TopologicalNode = TopologicalNode
        self.ConnectivityNodes = ConnectivityNodes

    def __str__(self):
        str = "class=ConnectivityNodeContainer\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
