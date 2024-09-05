from .PhaseTapChanger import PhaseTapChanger


class PhaseTapChangerLinear(PhaseTapChanger):
    """
    Describes a tap changer with a linear relation between the tap step and the phase angle difference across the transformer. This is a mathematical model that is an approximation of a real phase tap changer. The phase angle is computed as stepPhaseShiftIncrement times the tap position. The voltage magnitude of both sides is the same.

    :stepPhaseShiftIncrement: Phase shift per step position. A positive value indicates a positive angle variation from the Terminal at the  PowerTransformerEnd,  where the TapChanger is located, into the transformer. The actual phase shift increment might be more accurately computed from the symmetrical or asymmetrical models or a tap step table lookup if those are available. Default: 0.0
    :xMax: The reactance depends on the tap position according to a `u` shaped curve. The maximum reactance (xMax) appears at the low and high tap positions. Depending on the `u` curve the attribute can be either higher or lower than PowerTransformerEnd.x. Default: 0.0
    :xMin: The reactance depends on the tap position according to a `u` shaped curve. The minimum reactance (xMin) appears at the mid tap position.  PowerTransformerEnd.x shall be consistent with PhaseTapChangerLinear.xMin and PhaseTapChangerNonLinear.xMin. In case of inconsistency, PowerTransformerEnd.x shall be used. Default: 0.0
    """

    cgmesProfile = PhaseTapChanger.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
        ],
        "stepPhaseShiftIncrement": [
            cgmesProfile.EQ.value,
        ],
        "xMax": [
            cgmesProfile.EQ.value,
        ],
        "xMin": [
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class PhaseTapChanger: \n" + PhaseTapChanger.__doc__
    )

    def __init__(
        self, stepPhaseShiftIncrement=0.0, xMax=0.0, xMin=0.0, *args, **kw_args
    ):
        super().__init__(*args, **kw_args)

        self.stepPhaseShiftIncrement = stepPhaseShiftIncrement
        self.xMax = xMax
        self.xMin = xMin

    def __str__(self):
        str = "class=PhaseTapChangerLinear\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
