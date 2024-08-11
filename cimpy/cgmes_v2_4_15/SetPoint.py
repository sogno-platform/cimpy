from .AnalogControl import AnalogControl
from .CGMESProfile import Profile


class SetPoint(AnalogControl):
    """
    An analog control that issue a set point value.

    :normalValue: Normal value for Control.value e.g. used for percentage scaling. Default: 0.0
    :value: The value representing the actuator output. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "normalValue": [Profile.EQ.value, ],
        "value": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class AnalogControl:\n" + AnalogControl.__doc__

    def __init__(self, normalValue = 0.0, value = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.normalValue = normalValue
        self.value = value

    def __str__(self):
        str = "class=SetPoint\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
