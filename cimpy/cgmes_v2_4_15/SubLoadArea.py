from .EnergyArea import EnergyArea
from .CGMESProfile import Profile


class SubLoadArea(EnergyArea):
    """
    The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.

    :LoadArea: The LoadArea where the SubLoadArea belongs. Default: None
    :LoadGroups: The Loadgroups in the SubLoadArea. Default: "list"
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "LoadArea": [Profile.EQ.value, ],
        "LoadGroups": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class EnergyArea:\n" + EnergyArea.__doc__

    def __init__(self, LoadArea = None, LoadGroups = "list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.LoadArea = LoadArea
        self.LoadGroups = LoadGroups

    def __str__(self):
        str = "class=SubLoadArea\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
