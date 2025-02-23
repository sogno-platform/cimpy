from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class GenICompensationForGenJ(IdentifiedObject):
    """
    This class provides the resistive and reactive components of compensation for the generator associated with the IEEE Type 2 voltage compensator for current flow out of one of the other generators in the interconnection.

    :SynchronousMachineDynamics: Standard synchronous machine out of which current flow is being compensated for. Default: None
    :VcompIEEEType2: The standard IEEE Type 2 voltage compensator of this compensation. Default: None
    :rcij:  Default: 0.0
    :xcij:  Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, ],
        "SynchronousMachineDynamics": [Profile.DY.value, ],
        "VcompIEEEType2": [Profile.DY.value, ],
        "rcij": [Profile.DY.value, ],
        "xcij": [Profile.DY.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.DY.value

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, SynchronousMachineDynamics = None, VcompIEEEType2 = None, rcij = 0.0, xcij = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.SynchronousMachineDynamics = SynchronousMachineDynamics
        self.VcompIEEEType2 = VcompIEEEType2
        self.rcij = rcij
        self.xcij = xcij

    def __str__(self):
        str = "class=GenICompensationForGenJ\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
