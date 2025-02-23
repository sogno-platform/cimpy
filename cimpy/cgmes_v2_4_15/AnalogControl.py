from .Control import Control
from .CGMESProfile import Profile


class AnalogControl(Control):
    """
    An analog control used for supervisory control.

    :AnalogValue: The Control variable associated with the MeasurementValue. Default: None
    :maxValue: Normal value range maximum for any of the Control.value. Used for scaling, e.g. in bar graphs. Default: 0.0
    :minValue: Normal value range minimum for any of the Control.value. Used for scaling, e.g. in bar graphs. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "AnalogValue": [Profile.EQ.value, ],
        "maxValue": [Profile.EQ.value, ],
        "minValue": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class Control:\n" + Control.__doc__

    def __init__(self, AnalogValue = None, maxValue = 0.0, minValue = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.AnalogValue = AnalogValue
        self.maxValue = maxValue
        self.minValue = minValue

    def __str__(self):
        str = "class=AnalogControl\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
