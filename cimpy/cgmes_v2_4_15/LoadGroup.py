from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class LoadGroup(IdentifiedObject):
    """
    The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.

    :SubLoadArea: The SubLoadArea where the Loadgroup belongs. Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "SubLoadArea": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, SubLoadArea = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.SubLoadArea = SubLoadArea

    def __str__(self):
        str = "class=LoadGroup\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
