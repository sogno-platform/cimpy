from .EnergyArea import EnergyArea
from .CGMESProfile import Profile


class LoadArea(EnergyArea):
    """
    The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.

    :SubLoadAreas: The SubLoadAreas in the LoadArea. Default: "list"
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "SubLoadAreas": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class EnergyArea:\n" + EnergyArea.__doc__

    def __init__(self, SubLoadAreas = "list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.SubLoadAreas = SubLoadAreas

    def __str__(self):
        str = "class=LoadArea\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
