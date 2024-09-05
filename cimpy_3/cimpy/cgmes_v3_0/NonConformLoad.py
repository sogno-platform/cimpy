from .EnergyConsumer import EnergyConsumer


class NonConformLoad(EnergyConsumer):
    """
    NonConformLoad represents loads that do not follow a daily load change pattern and whose changes are not correlated with the daily load change pattern.

    :LoadGroup: Group of this ConformLoad. Default: None
    """

    cgmesProfile = EnergyConsumer.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
        ],
        "LoadGroup": [
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class EnergyConsumer: \n" + EnergyConsumer.__doc__
    )

    def __init__(self, LoadGroup=None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.LoadGroup = LoadGroup

    def __str__(self):
        str = "class=NonConformLoad\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
