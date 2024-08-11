from .ACDCTerminal import ACDCTerminal
from .CGMESProfile import Profile


class DCBaseTerminal(ACDCTerminal):
    """
    An electrical connection point at a piece of DC conducting equipment. DC terminals are connected at one physical DC node that may have multiple DC terminals connected. A DC node is similar to an AC connectivity node. The model enforces that DC connections are distinct from AC connections.

    :DCNode:  Default: None
    :DCTopologicalNode: See association end TopologicalNode.Terminal. Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, Profile.SSH.value, Profile.TP.value, ],
        "DCNode": [Profile.EQ.value, ],
        "DCTopologicalNode": [Profile.TP.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class ACDCTerminal:\n" + ACDCTerminal.__doc__

    def __init__(self, DCNode = None, DCTopologicalNode = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.DCNode = DCNode
        self.DCTopologicalNode = DCTopologicalNode

    def __str__(self):
        str = "class=DCBaseTerminal\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
