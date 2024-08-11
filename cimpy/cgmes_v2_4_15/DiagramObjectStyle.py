from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class DiagramObjectStyle(IdentifiedObject):
    """
    A reference to a style used by the originating system for a diagram object.  A diagram object style describes information such as line thickness, shape such as circle or rectangle etc, and color.

    :StyledObjects: A style can be assigned to multiple diagram objects. Default: "list"
    """

    possibleProfileList = {
        "class": [Profile.DL.value, ],
        "StyledObjects": [Profile.DL.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, StyledObjects = "list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.StyledObjects = StyledObjects

    def __str__(self):
        str = "class=DiagramObjectStyle\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
