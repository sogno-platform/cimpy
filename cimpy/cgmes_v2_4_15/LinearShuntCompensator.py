from .ShuntCompensator import ShuntCompensator
from .CGMESProfile import Profile


class LinearShuntCompensator(ShuntCompensator):
    """
    A linear shunt compensator has banks or sections with equal admittance values.

    :b0PerSection: Zero sequence shunt (charging) susceptance per section Default: 0.0
    :bPerSection: Positive sequence shunt (charging) susceptance per section Default: 0.0
    :g0PerSection: Zero sequence shunt (charging) conductance per section Default: 0.0
    :gPerSection: Positive sequence shunt (charging) conductance per section Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, Profile.SSH.value, ],
        "b0PerSection": [Profile.EQ.value, ],
        "bPerSection": [Profile.EQ.value, ],
        "g0PerSection": [Profile.EQ.value, ],
        "gPerSection": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class ShuntCompensator:\n" + ShuntCompensator.__doc__

    def __init__(self, b0PerSection = 0.0, bPerSection = 0.0, g0PerSection = 0.0, gPerSection = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.b0PerSection = b0PerSection
        self.bPerSection = bPerSection
        self.g0PerSection = g0PerSection
        self.gPerSection = gPerSection

    def __str__(self):
        str = "class=LinearShuntCompensator\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
