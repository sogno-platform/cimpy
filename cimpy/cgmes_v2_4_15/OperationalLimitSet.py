from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class OperationalLimitSet(IdentifiedObject):
    """
    A set of limits associated with equipment.  Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain different severities of limit levels that would apply to the same equipment. The set may contain limits of different types such as apparent power and current limits or high and low voltage limits  that are logically applied together as a set.

    :Equipment: The equipment to which the limit set applies. Default: None
    :OperationalLimitValue: The limit set to which the limit values belong. Default: "list"
    :Terminal:  Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "Equipment": [Profile.EQ.value, ],
        "OperationalLimitValue": [Profile.EQ.value, ],
        "Terminal": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, Equipment = None, OperationalLimitValue = "list", Terminal = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.Equipment = Equipment
        self.OperationalLimitValue = OperationalLimitValue
        self.Terminal = Terminal

    def __str__(self):
        str = "class=OperationalLimitSet\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
