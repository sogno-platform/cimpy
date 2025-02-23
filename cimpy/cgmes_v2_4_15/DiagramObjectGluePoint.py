from .Base import Base
from .CGMESProfile import Profile


class DiagramObjectGluePoint(Base):
    """
    This is used for grouping diagram object points from different diagram objects that are considered to be glued together in a diagram even if they are not at the exact same coordinates.

    :DiagramObjectPoints: The `glue` point to which this point is associated. Default: "list"
    """

    possibleProfileList = {
        "class": [Profile.DL.value, ],
        "DiagramObjectPoints": [Profile.DL.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DL.value


    def __init__(self, DiagramObjectPoints = "list"):

        self.DiagramObjectPoints = DiagramObjectPoints

    def __str__(self):
        str = "class=DiagramObjectGluePoint\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
