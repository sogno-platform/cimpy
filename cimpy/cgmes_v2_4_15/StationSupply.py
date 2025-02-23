from .EnergyConsumer import EnergyConsumer
from .CGMESProfile import Profile


class StationSupply(EnergyConsumer):
    """
    Station supply with load derived from the station output.

    """

    possibleProfileList = {
        "class": [Profile.EQ.value, Profile.SSH.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class EnergyConsumer:\n" + EnergyConsumer.__doc__

    def __init__(self, *args, **kw_args):
        super().__init__(*args, **kw_args)

        pass

    def __str__(self):
        str = "class=StationSupply\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
