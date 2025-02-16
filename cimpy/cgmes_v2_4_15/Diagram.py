from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class Diagram(IdentifiedObject):
    """
    The diagram being exchanged.  The coordinate system is a standard Cartesian coordinate system and the orientation attribute defines the orientation.

    :DiagramElements: A diagram is made up of multiple diagram objects. Default: "list"
    :DiagramStyle: A Diagram may have a DiagramStyle. Default: None
    :orientation: Coordinate system orientation of the diagram. Default: None
    :x1InitialView: X coordinate of the first corner of the initial view. Default: 0.0
    :x2InitialView: X coordinate of the second corner of the initial view. Default: 0.0
    :y1InitialView: Y coordinate of the first corner of the initial view. Default: 0.0
    :y2InitialView: Y coordinate of the second corner of the initial view. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DL.value, ],
        "DiagramElements": [Profile.DL.value, ],
        "DiagramStyle": [Profile.DL.value, ],
        "orientation": [Profile.DL.value, ],
        "x1InitialView": [Profile.DL.value, ],
        "x2InitialView": [Profile.DL.value, ],
        "y1InitialView": [Profile.DL.value, ],
        "y2InitialView": [Profile.DL.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DL.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, DiagramElements = "list", DiagramStyle = None, orientation = None, x1InitialView = 0.0, x2InitialView = 0.0, y1InitialView = 0.0, y2InitialView = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.DiagramElements = DiagramElements
        self.DiagramStyle = DiagramStyle
        self.orientation = orientation
        self.x1InitialView = x1InitialView
        self.x2InitialView = x2InitialView
        self.y1InitialView = y1InitialView
        self.y2InitialView = y2InitialView

    def __str__(self):
        str = "class=Diagram\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
