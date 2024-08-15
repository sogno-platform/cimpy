from .Equipment import Equipment
from .CGMESProfile import Profile


class DCConductingEquipment(Equipment):
    """
    The parts of the DC power system that are designed to carry current or that are conductively connected through DC terminals.

    :DCTerminals:  Default: "list"
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "DCTerminals": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class Equipment:\n" + Equipment.__doc__

    def __init__(self, DCTerminals = "list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.DCTerminals = DCTerminals

    def __str__(self):
        str = "class=DCConductingEquipment\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
