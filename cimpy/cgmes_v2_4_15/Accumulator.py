from .Measurement import Measurement
from .CGMESProfile import Profile


class Accumulator(Measurement):
    """
    Accumulator represents an accumulated (counted) Measurement, e.g. an energy value.

    :AccumulatorValues: Measurement to which this value is connected. Default: "list"
    :LimitSets: The Measurements using the LimitSet. Default: "list"
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "AccumulatorValues": [Profile.EQ.value, ],
        "LimitSets": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class Measurement:\n" + Measurement.__doc__

    def __init__(self, AccumulatorValues = "list", LimitSets = "list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.AccumulatorValues = AccumulatorValues
        self.LimitSets = LimitSets

    def __str__(self):
        str = "class=Accumulator\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
