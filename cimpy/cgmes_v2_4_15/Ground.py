from .ConductingEquipment import ConductingEquipment
from .CGMESProfile import Profile


class Ground(ConductingEquipment):
    """
    A point where the system is grounded used for connecting conducting equipment to ground. The power system model can have any number of grounds.

    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class ConductingEquipment:\n" + ConductingEquipment.__doc__

    def __init__(self, *args, **kw_args):
        super().__init__(*args, **kw_args)

        pass

    def __str__(self):
        str = "class=Ground\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
