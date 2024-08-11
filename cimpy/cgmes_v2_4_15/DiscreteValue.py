from .MeasurementValue import MeasurementValue
from .CGMESProfile import Profile


class DiscreteValue(MeasurementValue):
    """
    DiscreteValue represents a discrete MeasurementValue.

    :Command: The MeasurementValue that is controlled. Default: None
    :Discrete: The values connected to this measurement. Default: None
    :value: The value to supervise. Default: 0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "Command": [Profile.EQ.value, ],
        "Discrete": [Profile.EQ.value, ],
        "value": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class MeasurementValue:\n" + MeasurementValue.__doc__

    def __init__(self, Command = None, Discrete = None, value = 0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.Command = Command
        self.Discrete = Discrete
        self.value = value

    def __str__(self):
        str = "class=DiscreteValue\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
