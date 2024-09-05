from .ConnectivityNodeContainer import ConnectivityNodeContainer


class EquivalentNetwork(ConnectivityNodeContainer):
    """
    A class that groups electrical equivalents, including internal nodes, of a network that has been reduced. The ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The boundary Connectivity nodes where the equivalent connects outside itself are not contained by the equivalent.

    :EquivalentEquipments: The associated reduced equivalents. Default: "list"
    """

    cgmesProfile = ConnectivityNodeContainer.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.EQ.value,
        ],
        "EquivalentEquipments": [
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class ConnectivityNodeContainer: \n"
        + ConnectivityNodeContainer.__doc__
    )

    def __init__(self, EquivalentEquipments="list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.EquivalentEquipments = EquivalentEquipments

    def __str__(self):
        str = "class=EquivalentNetwork\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
