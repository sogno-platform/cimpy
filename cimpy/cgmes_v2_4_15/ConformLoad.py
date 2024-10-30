from .EnergyConsumer import EnergyConsumer
from .CGMESProfile import Profile


class ConformLoad(EnergyConsumer):
    """
    ConformLoad represent loads that follow a daily load change pattern where the pattern can be used to scale the load with a system load.

    :LoadGroup: Group of this ConformLoad. Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, Profile.SSH.value, ],
        "LoadGroup": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class EnergyConsumer:\n" + EnergyConsumer.__doc__

    def __init__(self, LoadGroup = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.LoadGroup = LoadGroup

    def __str__(self):
        str = "class=ConformLoad\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
