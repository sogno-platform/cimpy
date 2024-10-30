from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class ValueToAlias(IdentifiedObject):
    """
    Describes the translation of one particular value into a name, e.g. 1 as "Open".

    :ValueAliasSet: The ValueToAlias mappings included in the set. Default: None
    :value: The value that is mapped. Default: 0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "ValueAliasSet": [Profile.EQ.value, ],
        "value": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, ValueAliasSet = None, value = 0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ValueAliasSet = ValueAliasSet
        self.value = value

    def __str__(self):
        str = "class=ValueToAlias\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
