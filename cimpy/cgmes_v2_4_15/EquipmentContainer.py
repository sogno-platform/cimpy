from .ConnectivityNodeContainer import ConnectivityNodeContainer
from .CGMESProfile import Profile


class EquipmentContainer(ConnectivityNodeContainer):
    """
    A modeling construct to provide a root class for containing equipment.

    :Equipments: Contained equipment. Default: "list"
    """

    possibleProfileList = {
        "class": [Profile.EQ_BD.value, Profile.EQ.value, ],
        "Equipments": [Profile.EQ_BD.value, Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class ConnectivityNodeContainer:\n" + ConnectivityNodeContainer.__doc__

    def __init__(self, Equipments = "list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.Equipments = Equipments

    def __str__(self):
        str = "class=EquipmentContainer\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
