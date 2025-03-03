from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class DiagramStyle(IdentifiedObject):
    """
    The diagram style refer to a style used by the originating system for a diagram.  A diagram style describes information such as schematic, geographic, bus-branch etc.

    :Diagram: A DiagramStyle can be used by many Diagrams. Default: "list"
    """

    possibleProfileList = {
        "class": [Profile.DL.value, ],
        "Diagram": [Profile.DL.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DL.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, Diagram = "list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.Diagram = Diagram

    def __str__(self):
        str = "class=DiagramStyle\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
