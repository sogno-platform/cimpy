from .SeasonDayTypeSchedule import SeasonDayTypeSchedule
from .CGMESProfile import Profile


class RegulationSchedule(SeasonDayTypeSchedule):
    """
    A pre-established pattern over time for a controlled variable, e.g., busbar voltage.

    :RegulatingControl: Regulating controls that have this Schedule. Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "RegulatingControl": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class SeasonDayTypeSchedule:\n" + SeasonDayTypeSchedule.__doc__

    def __init__(self, RegulatingControl = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.RegulatingControl = RegulatingControl

    def __str__(self):
        str = "class=RegulationSchedule\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
