from .DCEquipmentContainer import DCEquipmentContainer
from .CGMESProfile import Profile


class DCLine(DCEquipmentContainer):
    """
    Overhead lines and/or cables connecting two or more HVDC substations.

    :Region:  Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "Region": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class DCEquipmentContainer:\n" + DCEquipmentContainer.__doc__

    def __init__(self, Region = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.Region = Region

    def __str__(self):
        str = "class=DCLine\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
