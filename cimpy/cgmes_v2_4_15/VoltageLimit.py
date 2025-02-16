from .OperationalLimit import OperationalLimit
from .CGMESProfile import Profile


class VoltageLimit(OperationalLimit):
    """
    Operational limit applied to voltage.

    :value: Limit on voltage. High or low limit nature of the limit depends upon the properties of the operational limit type. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "value": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class OperationalLimit:\n" + OperationalLimit.__doc__

    def __init__(self, value = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.value = value

    def __str__(self):
        str = "class=VoltageLimit\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
