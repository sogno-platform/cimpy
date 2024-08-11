from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class GeographicalRegion(IdentifiedObject):
    """
    A geographical region of a power system network model.

    :Regions: All sub-geograhpical regions within this geographical region. Default: "list"
    """

    possibleProfileList = {
        "class": [Profile.EQ_BD.value, Profile.EQ.value, ],
        "Regions": [Profile.EQ_BD.value, Profile.EQ.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, Regions = "list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.Regions = Regions

    def __str__(self):
        str = "class=GeographicalRegion\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
