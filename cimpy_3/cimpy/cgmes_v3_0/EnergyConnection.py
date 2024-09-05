from .ConductingEquipment import ConductingEquipment


class EnergyConnection(ConductingEquipment):
    """
    A connection of energy generation or consumption on the power system model.

    """

    cgmesProfile = ConductingEquipment.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
            cgmesProfile.SC.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class ConductingEquipment: \n"
        + ConductingEquipment.__doc__
    )

    def __init__(self, *args, **kw_args):
        super().__init__(*args, **kw_args)

        pass

    def __str__(self):
        str = "class=EnergyConnection\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
