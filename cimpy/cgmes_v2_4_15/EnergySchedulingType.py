from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class EnergySchedulingType(IdentifiedObject):
    """
    Used to define the type of generation for scheduling purposes.

    :EnergySource: Energy Source of a particular Energy Scheduling Type Default: "list"
    """

    possibleProfileList = {
        "class": [Profile.EQ_BD.value, Profile.EQ.value, ],
        "EnergySource": [Profile.EQ_BD.value, Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, EnergySource = "list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.EnergySource = EnergySource

    def __str__(self):
        str = "class=EnergySchedulingType\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
