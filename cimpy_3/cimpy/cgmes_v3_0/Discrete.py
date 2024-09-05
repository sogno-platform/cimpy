from .Measurement import Measurement


class Discrete(Measurement):
    """
    Discrete represents a discrete Measurement, i.e. a Measurement representing discrete values, e.g. a Breaker position.

    :DiscreteValues: The values connected to this measurement. Default: "list"
    :ValueAliasSet: The ValueAliasSet used for translation of a MeasurementValue.value to a name. Default: None
    """

    cgmesProfile = Measurement.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.OP.value,
        ],
        "DiscreteValues": [
            cgmesProfile.OP.value,
        ],
        "ValueAliasSet": [
            cgmesProfile.OP.value,
        ],
    }

    serializationProfile = {}

    __doc__ += "\n Documentation of parent class Measurement: \n" + Measurement.__doc__

    def __init__(self, DiscreteValues="list", ValueAliasSet=None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.DiscreteValues = DiscreteValues
        self.ValueAliasSet = ValueAliasSet

    def __str__(self):
        str = "class=Discrete\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
