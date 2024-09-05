from .MeasurementValue import MeasurementValue


class AnalogValue(MeasurementValue):
    """
    AnalogValue represents an analog MeasurementValue.

    :Analog: Measurement to which this value is connected. Default: None
    :AnalogControl: The Control variable associated with the MeasurementValue. Default: None
    """

    cgmesProfile = MeasurementValue.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.OP.value,
        ],
        "Analog": [
            cgmesProfile.OP.value,
        ],
        "AnalogControl": [
            cgmesProfile.OP.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class MeasurementValue: \n"
        + MeasurementValue.__doc__
    )

    def __init__(self, Analog=None, AnalogControl=None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.Analog = Analog
        self.AnalogControl = AnalogControl

    def __str__(self):
        str = "class=AnalogValue\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
