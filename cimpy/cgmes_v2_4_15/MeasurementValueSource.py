from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class MeasurementValueSource(IdentifiedObject):
    """
    MeasurementValueSource describes the alternative sources updating a MeasurementValue. User conventions for how to use the MeasurementValueSource attributes are described in the introduction to IEC 61970-301.

    :MeasurementValues: A reference to the type of source that updates the MeasurementValue, e.g. SCADA, CCLink, manual, etc. User conventions for the names of sources are contained in the introduction to IEC 61970-301. Default: "list"
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "MeasurementValues": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, MeasurementValues = "list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.MeasurementValues = MeasurementValues

    def __str__(self):
        str = "class=MeasurementValueSource\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
