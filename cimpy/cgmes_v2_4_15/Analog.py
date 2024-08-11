from .Measurement import Measurement
from .CGMESProfile import Profile


class Analog(Measurement):
    """
    Analog represents an analog Measurement.

    :AnalogValues: Measurement to which this value is connected. Default: "list"
    :LimitSets: The Measurements using the LimitSet. Default: "list"
    :positiveFlowIn: If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource. Default: False
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "AnalogValues": [Profile.EQ.value, ],
        "LimitSets": [Profile.EQ.value, ],
        "positiveFlowIn": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class Measurement:\n" + Measurement.__doc__

    def __init__(self, AnalogValues = "list", LimitSets = "list", positiveFlowIn = False, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.AnalogValues = AnalogValues
        self.LimitSets = LimitSets
        self.positiveFlowIn = positiveFlowIn

    def __str__(self):
        str = "class=Analog\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
