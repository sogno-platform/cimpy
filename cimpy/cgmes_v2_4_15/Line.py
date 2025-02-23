from .EquipmentContainer import EquipmentContainer
from .CGMESProfile import Profile


class Line(EquipmentContainer):
    """
    Contains equipment beyond a substation belonging to a power transmission line.

    :Region: The lines within the sub-geographical region. Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ_BD.value, Profile.EQ.value, ],
        "Region": [Profile.EQ_BD.value, Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class EquipmentContainer:\n" + EquipmentContainer.__doc__

    def __init__(self, Region = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.Region = Region

    def __str__(self):
        str = "class=Line\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
