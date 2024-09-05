from .IdentifiedObject import IdentifiedObject


class MutualCoupling(IdentifiedObject):
    """
    This class represents the zero sequence line mutual coupling.

    :b0ch: Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section. Default: 0.0
    :distance11: Distance to the start of the coupled region from the first line`s terminal having sequence number equal to 1. Default: 0.0
    :distance12: Distance to the end of the coupled region from the first line`s terminal with sequence number equal to 1. Default: 0.0
    :distance21: Distance to the start of coupled region from the second line`s terminal with sequence number equal to 1. Default: 0.0
    :distance22: Distance to the end of coupled region from the second line`s terminal with sequence number equal to 1. Default: 0.0
    :g0ch: Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section. Default: 0.0
    :r0: Zero sequence branch-to-branch mutual impedance coupling, resistance. Default: 0.0
    :x0: Zero sequence branch-to-branch mutual impedance coupling, reactance. Default: 0.0
    :Second_Terminal: The starting terminal for the calculation of distances along the second branch of the mutual coupling. Default: None
    :First_Terminal: The starting terminal for the calculation of distances along the first branch of the mutual coupling.  Normally MutualCoupling would only be used for terminals of AC line segments.  The first and second terminals of a mutual coupling should point to different AC line segments. Default: None
    """

    cgmesProfile = IdentifiedObject.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.SC.value,
        ],
        "b0ch": [
            cgmesProfile.SC.value,
        ],
        "distance11": [
            cgmesProfile.SC.value,
        ],
        "distance12": [
            cgmesProfile.SC.value,
        ],
        "distance21": [
            cgmesProfile.SC.value,
        ],
        "distance22": [
            cgmesProfile.SC.value,
        ],
        "g0ch": [
            cgmesProfile.SC.value,
        ],
        "r0": [
            cgmesProfile.SC.value,
        ],
        "x0": [
            cgmesProfile.SC.value,
        ],
        "Second_Terminal": [
            cgmesProfile.SC.value,
        ],
        "First_Terminal": [
            cgmesProfile.SC.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class IdentifiedObject: \n"
        + IdentifiedObject.__doc__
    )

    def __init__(
        self,
        b0ch=0.0,
        distance11=0.0,
        distance12=0.0,
        distance21=0.0,
        distance22=0.0,
        g0ch=0.0,
        r0=0.0,
        x0=0.0,
        Second_Terminal=None,
        First_Terminal=None,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.b0ch = b0ch
        self.distance11 = distance11
        self.distance12 = distance12
        self.distance21 = distance21
        self.distance22 = distance22
        self.g0ch = g0ch
        self.r0 = r0
        self.x0 = x0
        self.Second_Terminal = Second_Terminal
        self.First_Terminal = First_Terminal

    def __str__(self):
        str = "class=MutualCoupling\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
