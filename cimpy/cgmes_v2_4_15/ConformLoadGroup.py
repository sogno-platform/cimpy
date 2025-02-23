from .LoadGroup import LoadGroup
from .CGMESProfile import Profile


class ConformLoadGroup(LoadGroup):
    """
    A group of loads conforming to an allocation pattern.

    :ConformLoadSchedules: The ConformLoadSchedules in the ConformLoadGroup. Default: "list"
    :EnergyConsumers: Conform loads assigned to this ConformLoadGroup. Default: "list"
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "ConformLoadSchedules": [Profile.EQ.value, ],
        "EnergyConsumers": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class LoadGroup:\n" + LoadGroup.__doc__

    def __init__(self, ConformLoadSchedules = "list", EnergyConsumers = "list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ConformLoadSchedules = ConformLoadSchedules
        self.EnergyConsumers = EnergyConsumers

    def __str__(self):
        str = "class=ConformLoadGroup\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
