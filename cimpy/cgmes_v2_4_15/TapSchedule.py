from .SeasonDayTypeSchedule import SeasonDayTypeSchedule
from .CGMESProfile import Profile


class TapSchedule(SeasonDayTypeSchedule):
    """
    A pre-established pattern over time for a tap step.

    :TapChanger: A TapChanger can have TapSchedules. Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "TapChanger": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class SeasonDayTypeSchedule:\n" + SeasonDayTypeSchedule.__doc__

    def __init__(self, TapChanger = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.TapChanger = TapChanger

    def __str__(self):
        str = "class=TapSchedule\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
