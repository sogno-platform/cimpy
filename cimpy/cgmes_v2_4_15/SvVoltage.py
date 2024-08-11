from .Base import Base
from .CGMESProfile import Profile


class SvVoltage(Base):
    """
    State variable for voltage.

    :TopologicalNode: The state voltage associated with the topological node. Default: None
    :angle: The voltage angle of the topological node complex voltage with respect to system reference. Default: 0.0
    :v: The voltage magnitude of the topological node. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.SV.value, ],
        "TopologicalNode": [Profile.SV.value, ],
        "angle": [Profile.SV.value, ],
        "v": [Profile.SV.value, ],
    }

    serializationProfile = {}


    def __init__(self, TopologicalNode = None, angle = 0.0, v = 0.0):

        self.TopologicalNode = TopologicalNode
        self.angle = angle
        self.v = v

    def __str__(self):
        str = "class=SvVoltage\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
