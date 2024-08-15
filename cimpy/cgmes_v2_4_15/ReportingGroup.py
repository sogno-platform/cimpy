from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class ReportingGroup(IdentifiedObject):
    """
    A reporting group is used for various ad-hoc groupings used for reporting.

    :BusNameMarker: The reporting group to which this bus name marker belongs. Default: "list"
    :TopologicalNode: The reporting group to which the topological node belongs. Default: "list"
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, Profile.TP.value, ],
        "BusNameMarker": [Profile.EQ.value, ],
        "TopologicalNode": [Profile.TP.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, BusNameMarker = "list", TopologicalNode = "list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.BusNameMarker = BusNameMarker
        self.TopologicalNode = TopologicalNode

    def __str__(self):
        str = "class=ReportingGroup\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
