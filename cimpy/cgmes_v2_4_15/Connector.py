from .ConductingEquipment import ConductingEquipment
from .CGMESProfile import Profile


class Connector(ConductingEquipment):
    """
    A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation and are modelled with a single logical terminal.

    """

    possibleProfileList = {
        "class": [Profile.EQ_BD.value, Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class ConductingEquipment:\n" + ConductingEquipment.__doc__

    def __init__(self, *args, **kw_args):
        super().__init__(*args, **kw_args)

        pass

    def __str__(self):
        str = "class=Connector\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
