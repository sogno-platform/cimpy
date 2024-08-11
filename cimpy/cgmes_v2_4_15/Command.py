from .Control import Control
from .CGMESProfile import Profile


class Command(Control):
    """
    A Command is a discrete control used for supervisory control.

    :DiscreteValue: The Control variable associated with the MeasurementValue. Default: None
    :ValueAliasSet: The ValueAliasSet used for translation of a Control value to a name. Default: None
    :normalValue: Normal value for Control.value e.g. used for percentage scaling. Default: 0
    :value: The value representing the actuator output. Default: 0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "DiscreteValue": [Profile.EQ.value, ],
        "ValueAliasSet": [Profile.EQ.value, ],
        "normalValue": [Profile.EQ.value, ],
        "value": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class Control:\n" + Control.__doc__

    def __init__(self, DiscreteValue = None, ValueAliasSet = None, normalValue = 0, value = 0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.DiscreteValue = DiscreteValue
        self.ValueAliasSet = ValueAliasSet
        self.normalValue = normalValue
        self.value = value

    def __str__(self):
        str = "class=Command\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
