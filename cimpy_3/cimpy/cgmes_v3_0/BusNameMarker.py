from .IdentifiedObject import IdentifiedObject


class BusNameMarker(IdentifiedObject):
    """
    Used to apply user standard names to TopologicalNodes. Associated with one or more terminals that are normally connected with the bus name.    The associated terminals are normally connected by non-retained switches. For a ring bus station configuration, all BusbarSection terminals in the ring are typically associated.   For a breaker and a half scheme, both BusbarSections would normally be associated.  For a ring bus, all BusbarSections would normally be associated.  For a "straight" busbar configuration, normally only the main terminal at the BusbarSection would be associated.

    :Terminal: The terminals associated with this bus name marker. Default: "list"
    :priority: Priority of bus name marker for use as topology bus name.  Use 0 for do not care.  Use 1 for highest priority.  Use 2 as priority is less than 1 and so on. Default: 0
    :ReportingGroup: The reporting group to which this bus name marker belongs. Default: None
    """

    cgmesProfile = IdentifiedObject.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.EQ.value,
        ],
        "Terminal": [
            cgmesProfile.EQ.value,
        ],
        "priority": [
            cgmesProfile.EQ.value,
        ],
        "ReportingGroup": [
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class IdentifiedObject: \n"
        + IdentifiedObject.__doc__
    )

    def __init__(
        self, Terminal="list", priority=0, ReportingGroup=None, *args, **kw_args
    ):
        super().__init__(*args, **kw_args)

        self.Terminal = Terminal
        self.priority = priority
        self.ReportingGroup = ReportingGroup

    def __str__(self):
        str = "class=BusNameMarker\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
