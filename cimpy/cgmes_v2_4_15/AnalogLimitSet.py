from .LimitSet import LimitSet
from .CGMESProfile import Profile


class AnalogLimitSet(LimitSet):
    """
    An AnalogLimitSet specifies a set of Limits that are associated with an Analog measurement.

    :Limits: The set of limits. Default: "list"
    :Measurements: A measurement may have zero or more limit ranges defined for it. Default: "list"
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "Limits": [Profile.EQ.value, ],
        "Measurements": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class LimitSet:\n" + LimitSet.__doc__

    def __init__(self, Limits = "list", Measurements = "list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.Limits = Limits
        self.Measurements = Measurements

    def __str__(self):
        str = "class=AnalogLimitSet\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
