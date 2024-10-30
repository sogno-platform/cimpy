from .MeasurementValue import MeasurementValue
from .CGMESProfile import Profile


class AnalogValue(MeasurementValue):
    """
    AnalogValue represents an analog MeasurementValue.

    :Analog: The values connected to this measurement. Default: None
    :AnalogControl: The MeasurementValue that is controlled. Default: None
    :value: The value to supervise. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "Analog": [Profile.EQ.value, ],
        "AnalogControl": [Profile.EQ.value, ],
        "value": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class MeasurementValue:\n" + MeasurementValue.__doc__

    def __init__(self, Analog = None, AnalogControl = None, value = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.Analog = Analog
        self.AnalogControl = AnalogControl
        self.value = value

    def __str__(self):
        str = "class=AnalogValue\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
