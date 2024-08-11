from .Equipment import Equipment
from .CGMESProfile import Profile


class HydroPump(Equipment):
    """
    A synchronous motor-driven pump, typically associated with a pumped storage plant.

    :HydroPowerPlant: The hydro pump may be a member of a pumped storage plant or a pump for distributing water. Default: None
    :RotatingMachine: The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating. Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "HydroPowerPlant": [Profile.EQ.value, ],
        "RotatingMachine": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class Equipment:\n" + Equipment.__doc__

    def __init__(self, HydroPowerPlant = None, RotatingMachine = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.HydroPowerPlant = HydroPowerPlant
        self.RotatingMachine = RotatingMachine

    def __str__(self):
        str = "class=HydroPump\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
