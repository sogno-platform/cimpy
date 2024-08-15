from .MeasurementValue import MeasurementValue
from .CGMESProfile import Profile


class StringMeasurementValue(MeasurementValue):
    """
    StringMeasurementValue represents a measurement value of type string.

    :StringMeasurement: Measurement to which this value is connected. Default: None
    :value: The value to supervise. Default: ''
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "StringMeasurement": [Profile.EQ.value, ],
        "value": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class MeasurementValue:\n" + MeasurementValue.__doc__

    def __init__(self, StringMeasurement = None, value = '', *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.StringMeasurement = StringMeasurement
        self.value = value

    def __str__(self):
        str = "class=StringMeasurementValue\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
