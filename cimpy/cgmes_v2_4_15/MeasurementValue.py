from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class MeasurementValue(IdentifiedObject):
    """
    The current state for a measurement. A state value is an instance of a measurement from a specific source. Measurements can be associated with many state values, each representing a different source for the measurement.

    :MeasurementValueQuality: A MeasurementValue has a MeasurementValueQuality associated with it. Default: None
    :MeasurementValueSource: The MeasurementValues updated by the source. Default: None
    :sensorAccuracy: The limit, expressed as a percentage of the sensor maximum, that errors will not exceed when the sensor is used under  reference conditions. Default: 0.0
    :timeStamp: The time when the value was last updated Default: ''
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "MeasurementValueQuality": [Profile.EQ.value, ],
        "MeasurementValueSource": [Profile.EQ.value, ],
        "sensorAccuracy": [Profile.EQ.value, ],
        "timeStamp": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, MeasurementValueQuality = None, MeasurementValueSource = None, sensorAccuracy = 0.0, timeStamp = '', *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.MeasurementValueQuality = MeasurementValueQuality
        self.MeasurementValueSource = MeasurementValueSource
        self.sensorAccuracy = sensorAccuracy
        self.timeStamp = timeStamp

    def __str__(self):
        str = "class=MeasurementValue\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
