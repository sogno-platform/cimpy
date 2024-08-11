from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class BasicIntervalSchedule(IdentifiedObject):
    """
    Schedule of values at points in time.

    :startTime: The time for the first time point. Default: ''
    :value1Unit: Value1 units of measure. Default: None
    :value2Unit: Value2 units of measure. Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "startTime": [Profile.EQ.value, ],
        "value1Unit": [Profile.EQ.value, ],
        "value2Unit": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, startTime = '', value1Unit = None, value2Unit = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.startTime = startTime
        self.value1Unit = value1Unit
        self.value2Unit = value2Unit

    def __str__(self):
        str = "class=BasicIntervalSchedule\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
