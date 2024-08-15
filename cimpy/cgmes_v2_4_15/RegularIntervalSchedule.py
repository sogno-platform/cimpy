from .BasicIntervalSchedule import BasicIntervalSchedule
from .CGMESProfile import Profile


class RegularIntervalSchedule(BasicIntervalSchedule):
    """
    The schedule has time points where the time between them is constant.

    :TimePoints: The regular interval time point data values that define this schedule. Default: "list"
    :endTime: The time for the last time point. Default: ''
    :timeStep: The time between each pair of subsequent regular time points in sequence order. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "TimePoints": [Profile.EQ.value, ],
        "endTime": [Profile.EQ.value, ],
        "timeStep": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class BasicIntervalSchedule:\n" + BasicIntervalSchedule.__doc__

    def __init__(self, TimePoints = "list", endTime = '', timeStep = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.TimePoints = TimePoints
        self.endTime = endTime
        self.timeStep = timeStep

    def __str__(self):
        str = "class=RegularIntervalSchedule\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
