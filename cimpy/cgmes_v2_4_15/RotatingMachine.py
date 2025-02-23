from .RegulatingCondEq import RegulatingCondEq
from .CGMESProfile import Profile


class RotatingMachine(RegulatingCondEq):
    """
    A rotating machine which may be used as a generator or motor.

    :GeneratingUnit: A synchronous machine may operate as a generator and as such becomes a member of a generating unit. Default: None
    :HydroPump: The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating. Default: None
    :p: Active power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution. Default: 0.0
    :q: Reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution. Default: 0.0
    :ratedPowerFactor: Power factor (nameplate data). It is primarily used for short circuit data exchange according to IEC 60909. Default: 0.0
    :ratedS: Nameplate apparent power rating for the unit. The attribute shall have a positive value. Default: 0.0
    :ratedU: Rated voltage (nameplate data, Ur in IEC 60909-0). It is primarily used for short circuit data exchange according to IEC 60909. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, Profile.EQ.value, Profile.SSH.value, ],
        "GeneratingUnit": [Profile.EQ.value, ],
        "HydroPump": [Profile.EQ.value, ],
        "p": [Profile.SSH.value, ],
        "q": [Profile.SSH.value, ],
        "ratedPowerFactor": [Profile.EQ.value, ],
        "ratedS": [Profile.EQ.value, ],
        "ratedU": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class RegulatingCondEq:\n" + RegulatingCondEq.__doc__

    def __init__(self, GeneratingUnit = None, HydroPump = None, p = 0.0, q = 0.0, ratedPowerFactor = 0.0, ratedS = 0.0, ratedU = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.GeneratingUnit = GeneratingUnit
        self.HydroPump = HydroPump
        self.p = p
        self.q = q
        self.ratedPowerFactor = ratedPowerFactor
        self.ratedS = ratedS
        self.ratedU = ratedU

    def __str__(self):
        str = "class=RotatingMachine\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
