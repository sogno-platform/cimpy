from .EarthFaultCompensator import EarthFaultCompensator
from .CGMESProfile import Profile


class GroundingImpedance(EarthFaultCompensator):
    """
    A fixed impedance device used for grounding.

    :x: Reactance of device. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "x": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class EarthFaultCompensator:\n" + EarthFaultCompensator.__doc__

    def __init__(self, x = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.x = x

    def __str__(self):
        str = "class=GroundingImpedance\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
