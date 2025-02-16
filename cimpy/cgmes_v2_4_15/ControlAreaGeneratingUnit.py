from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class ControlAreaGeneratingUnit(IdentifiedObject):
    """
    A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit.

    :ControlArea: The parent control area for the generating unit specifications. Default: None
    :GeneratingUnit: The generating unit specified for this control area.  Note that a control area should include a GeneratingUnit only once. Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "ControlArea": [Profile.EQ.value, ],
        "GeneratingUnit": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, ControlArea = None, GeneratingUnit = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ControlArea = ControlArea
        self.GeneratingUnit = GeneratingUnit

    def __str__(self):
        str = "class=ControlAreaGeneratingUnit\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
