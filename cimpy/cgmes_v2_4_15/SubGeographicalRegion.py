from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class SubGeographicalRegion(IdentifiedObject):
    """
    A subset of a geographical region of a power system network model.

    :DCLines:  Default: "list"
    :Lines: The sub-geographical region of the line. Default: "list"
    :Region: The geographical region to which this sub-geographical region is within. Default: None
    :Substations: The substations in this sub-geographical region. Default: "list"
    """

    possibleProfileList = {
        "class": [Profile.EQ_BD.value, Profile.EQ.value, ],
        "DCLines": [Profile.EQ.value, ],
        "Lines": [Profile.EQ_BD.value, Profile.EQ.value, ],
        "Region": [Profile.EQ_BD.value, Profile.EQ.value, ],
        "Substations": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, DCLines = "list", Lines = "list", Region = None, Substations = "list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.DCLines = DCLines
        self.Lines = Lines
        self.Region = Region
        self.Substations = Substations

    def __str__(self):
        str = "class=SubGeographicalRegion\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
