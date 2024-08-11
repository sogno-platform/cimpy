from .Measurement import Measurement
from .CGMESProfile import Profile


class Discrete(Measurement):
    """
    Discrete represents a discrete Measurement, i.e. a Measurement representing discrete values, e.g. a Breaker position.

    :DiscreteValues: Measurement to which this value is connected. Default: "list"
    :ValueAliasSet: The ValueAliasSet used for translation of a MeasurementValue.value to a name. Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "DiscreteValues": [Profile.EQ.value, ],
        "ValueAliasSet": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class Measurement:\n" + Measurement.__doc__

    def __init__(self, DiscreteValues = "list", ValueAliasSet = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.DiscreteValues = DiscreteValues
        self.ValueAliasSet = ValueAliasSet

    def __str__(self):
        str = "class=Discrete\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
