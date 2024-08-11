from .SeasonDayTypeSchedule import SeasonDayTypeSchedule
from .CGMESProfile import Profile


class SwitchSchedule(SeasonDayTypeSchedule):
    """
    A schedule of switch positions.  If RegularTimePoint.value1 is 0, the switch is open.  If 1, the switch is closed.

    :Switch: A Switch can be associated with SwitchSchedules. Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "Switch": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class SeasonDayTypeSchedule:\n" + SeasonDayTypeSchedule.__doc__

    def __init__(self, Switch = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.Switch = Switch

    def __str__(self):
        str = "class=SwitchSchedule\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
