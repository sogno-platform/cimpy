from .Base import Base
from .CGMESProfile import Profile


class SvInjection(Base):
    """
    The SvInjection is reporting the calculated bus injection minus the sum of the terminal flows. The terminal flow is positive out from the bus (load sign convention) and bus injection has positive flow into the bus. SvInjection may have the remainder after state estimation or slack after power flow calculation.

    :TopologicalNode: The injection flows state variables associated with the topological node. Default: None
    :pInjection: The active power injected into the bus in addition to injections from equipment terminals.  Positive sign means injection into the TopologicalNode (bus). Default: 0.0
    :qInjection: The reactive power injected into the bus in addition to injections from equipment terminals. Positive sign means injection into the TopologicalNode (bus). Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.SV.value, ],
        "TopologicalNode": [Profile.SV.value, ],
        "pInjection": [Profile.SV.value, ],
        "qInjection": [Profile.SV.value, ],
    }

    serializationProfile = {}


    def __init__(self, TopologicalNode = None, pInjection = 0.0, qInjection = 0.0):

        self.TopologicalNode = TopologicalNode
        self.pInjection = pInjection
        self.qInjection = qInjection

    def __str__(self):
        str = "class=SvInjection\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
