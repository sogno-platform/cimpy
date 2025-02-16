from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class Season(IdentifiedObject):
    """
    A specified time period of the year.

    :SeasonDayTypeSchedules: Season for the Schedule. Default: "list"
    :endDate: Date season ends. Default: 0.0
    :startDate: Date season starts. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "SeasonDayTypeSchedules": [Profile.EQ.value, ],
        "endDate": [Profile.EQ.value, ],
        "startDate": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, SeasonDayTypeSchedules = "list", endDate = 0.0, startDate = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.SeasonDayTypeSchedules = SeasonDayTypeSchedules
        self.endDate = endDate
        self.startDate = startDate

    def __str__(self):
        str = "class=Season\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
