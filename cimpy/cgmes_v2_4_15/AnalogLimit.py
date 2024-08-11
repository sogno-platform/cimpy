from .Limit import Limit
from .CGMESProfile import Profile


class AnalogLimit(Limit):
    """
    Limit values for Analog measurements.

    :LimitSet: The limit values used for supervision of Measurements. Default: None
    :value: The value to supervise against. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "LimitSet": [Profile.EQ.value, ],
        "value": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class Limit:\n" + Limit.__doc__

    def __init__(self, LimitSet = None, value = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.LimitSet = LimitSet
        self.value = value

    def __str__(self):
        str = "class=AnalogLimit\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
