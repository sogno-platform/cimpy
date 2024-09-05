from .Measurement import Measurement


class Accumulator(Measurement):
    """
    Accumulator represents an accumulated (counted) Measurement, e.g. an energy value.

    :AccumulatorValues: The values connected to this measurement. Default: "list"
    :LimitSets: A measurement may have zero or more limit ranges defined for it. Default: "list"
    """

    cgmesProfile = Measurement.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.OP.value,
        ],
        "AccumulatorValues": [
            cgmesProfile.OP.value,
        ],
        "LimitSets": [
            cgmesProfile.OP.value,
        ],
    }

    serializationProfile = {}

    __doc__ += "\n Documentation of parent class Measurement: \n" + Measurement.__doc__

    def __init__(self, AccumulatorValues="list", LimitSets="list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.AccumulatorValues = AccumulatorValues
        self.LimitSets = LimitSets

    def __str__(self):
        str = "class=Accumulator\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
