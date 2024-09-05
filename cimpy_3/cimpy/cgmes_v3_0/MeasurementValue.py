from .IOPoint import IOPoint


class MeasurementValue(IOPoint):
    """
    The current state for a measurement. A state value is an instance of a measurement from a specific source. Measurements can be associated with many state values, each representing a different source for the measurement.

    :timeStamp: The time when the value was last updated. Default: ''
    :sensorAccuracy: The limit, expressed as a percentage of the sensor maximum, that errors will not exceed when the sensor is used under  reference conditions. Default: 0.0
    :MeasurementValueQuality: A MeasurementValue has a MeasurementValueQuality associated with it. Default: None
    :MeasurementValueSource: A reference to the type of source that updates the MeasurementValue, e.g. SCADA, CCLink, manual, etc. User conventions for the names of sources are contained in the introduction to IEC 61970-301. Default: None
    """

    cgmesProfile = IOPoint.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.OP.value,
        ],
        "timeStamp": [
            cgmesProfile.OP.value,
        ],
        "sensorAccuracy": [
            cgmesProfile.OP.value,
        ],
        "MeasurementValueQuality": [
            cgmesProfile.OP.value,
        ],
        "MeasurementValueSource": [
            cgmesProfile.OP.value,
        ],
    }

    serializationProfile = {}

    __doc__ += "\n Documentation of parent class IOPoint: \n" + IOPoint.__doc__

    def __init__(
        self,
        timeStamp="",
        sensorAccuracy=0.0,
        MeasurementValueQuality=None,
        MeasurementValueSource=None,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.timeStamp = timeStamp
        self.sensorAccuracy = sensorAccuracy
        self.MeasurementValueQuality = MeasurementValueQuality
        self.MeasurementValueSource = MeasurementValueSource

    def __str__(self):
        str = "class=MeasurementValue\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
