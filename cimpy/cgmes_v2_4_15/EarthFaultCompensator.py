from .ConductingEquipment import ConductingEquipment
from .CGMESProfile import Profile


class EarthFaultCompensator(ConductingEquipment):
    """
    A conducting equipment used to represent a connection to ground which is typically used to compensate earth faults..   An earth fault compensator device modeled with a single terminal implies a second terminal solidly connected to ground.  If two terminals are modeled, the ground is not assumed and normal connection rules apply.

    :r: Nominal resistance of device. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "r": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class ConductingEquipment:\n" + ConductingEquipment.__doc__

    def __init__(self, r = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.r = r

    def __str__(self):
        str = "class=EarthFaultCompensator\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
