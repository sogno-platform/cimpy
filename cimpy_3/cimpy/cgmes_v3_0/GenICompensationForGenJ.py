from .IdentifiedObject import IdentifiedObject


class GenICompensationForGenJ(IdentifiedObject):
    """
    Resistive and reactive components of compensation for generator associated with IEEE type 2 voltage compensator for current flow out of another generator in the interconnection.

    :SynchronousMachineDynamics: Standard synchronous machine out of which current flow is being compensated for. Default: None
    :VcompIEEEType2: The standard IEEE type 2 voltage compensator of this compensation. Default: None
    :rcij: <font color=`#0f0f0f`>Resistive component of compensation of generator associated with this IEEE type 2 voltage compensator for current flow out of another generator (<i>Rcij</i>).</font> Default: 0.0
    :xcij: <font color=`#0f0f0f`>Reactive component of compensation of generator associated with this IEEE type 2 voltage compensator for current flow out of another generator (<i>Xcij</i>).</font> Default: 0.0
    """

    cgmesProfile = IdentifiedObject.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "SynchronousMachineDynamics": [
            cgmesProfile.DY.value,
        ],
        "VcompIEEEType2": [
            cgmesProfile.DY.value,
        ],
        "rcij": [
            cgmesProfile.DY.value,
        ],
        "xcij": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class IdentifiedObject: \n"
        + IdentifiedObject.__doc__
    )

    def __init__(
        self,
        SynchronousMachineDynamics=None,
        VcompIEEEType2=None,
        rcij=0.0,
        xcij=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.SynchronousMachineDynamics = SynchronousMachineDynamics
        self.VcompIEEEType2 = VcompIEEEType2
        self.rcij = rcij
        self.xcij = xcij

    def __str__(self):
        str = "class=GenICompensationForGenJ\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
