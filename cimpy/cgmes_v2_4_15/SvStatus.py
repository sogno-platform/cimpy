from .Base import Base
from .CGMESProfile import Profile


class SvStatus(Base):
    """
    State variable for status.

    :ConductingEquipment: The conducting equipment associated with the status state variable. Default: None
    :inService: The in service status as a result of topology processing. Default: False
    """

    possibleProfileList = {
        "class": [Profile.SV.value, ],
        "ConductingEquipment": [Profile.SV.value, ],
        "inService": [Profile.SV.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.SV.value


    def __init__(self, ConductingEquipment = None, inService = False):

        self.ConductingEquipment = ConductingEquipment
        self.inService = inService

    def __str__(self):
        str = "class=SvStatus\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
