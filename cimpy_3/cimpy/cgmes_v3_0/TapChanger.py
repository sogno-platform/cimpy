from .PowerSystemResource import PowerSystemResource


class TapChanger(PowerSystemResource):
    """
    Mechanism for changing transformer winding tap positions.

    :controlEnabled: Specifies the regulation status of the equipment.  True is regulating, false is not regulating. Default: False
    :step: Tap changer position. Starting step for a steady state solution. Non integer values are allowed to support continuous tap variables. The reasons for continuous value are to support study cases where no discrete tap changer has yet been designed, a solution where a narrow voltage band forces the tap step to oscillate or to accommodate for a continuous solution as input. The attribute shall be equal to or greater than lowStep and equal to or less than highStep. Default: 0.0
    :TapSchedules: A TapChanger can have TapSchedules. Default: "list"
    :highStep: Highest possible tap step position, advance from neutral. The attribute shall be greater than lowStep. Default: 0
    :lowStep: Lowest possible tap step position, retard from neutral. Default: 0
    :ltcFlag: Specifies whether or not a TapChanger has load tap changing capabilities. Default: False
    :neutralStep: The neutral tap step position for this winding. The attribute shall be equal to or greater than lowStep and equal or less than highStep. It is the step position where the voltage is neutralU when the other terminals of the transformer are at the ratedU.  If there are other tap changers on the transformer those taps are kept constant at their neutralStep. Default: 0
    :neutralU: Voltage at which the winding operates at the neutral tap setting. It is the voltage at the terminal of the PowerTransformerEnd associated with the tap changer when all tap changers on the transformer are at their neutralStep position.  Normally neutralU of the tap changer is the same as ratedU of the PowerTransformerEnd, but it can differ in special cases such as when the tapping mechanism is separate from the winding more common on lower voltage transformers. This attribute is not relevant for PhaseTapChangerAsymmetrical, PhaseTapChangerSymmetrical and PhaseTapChangerLinear. Default: 0.0
    :normalStep: The tap step position used in `normal` network operation for this winding. For a `Fixed` tap changer indicates the current physical tap setting. The attribute shall be equal to or greater than lowStep and equal to or less than highStep. Default: 0
    :TapChangerControl: The regulating control scheme in which this tap changer participates. Default: None
    :SvTapStep: The tap step state associated with the tap changer. Default: None
    """

    cgmesProfile = PowerSystemResource.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
            cgmesProfile.SV.value,
        ],
        "controlEnabled": [
            cgmesProfile.SSH.value,
        ],
        "step": [
            cgmesProfile.SSH.value,
        ],
        "TapSchedules": [
            cgmesProfile.EQ.value,
        ],
        "highStep": [
            cgmesProfile.EQ.value,
        ],
        "lowStep": [
            cgmesProfile.EQ.value,
        ],
        "ltcFlag": [
            cgmesProfile.EQ.value,
        ],
        "neutralStep": [
            cgmesProfile.EQ.value,
        ],
        "neutralU": [
            cgmesProfile.EQ.value,
        ],
        "normalStep": [
            cgmesProfile.EQ.value,
        ],
        "TapChangerControl": [
            cgmesProfile.EQ.value,
        ],
        "SvTapStep": [
            cgmesProfile.SV.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class PowerSystemResource: \n"
        + PowerSystemResource.__doc__
    )

    def __init__(
        self,
        controlEnabled=False,
        step=0.0,
        TapSchedules="list",
        highStep=0,
        lowStep=0,
        ltcFlag=False,
        neutralStep=0,
        neutralU=0.0,
        normalStep=0,
        TapChangerControl=None,
        SvTapStep=None,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.controlEnabled = controlEnabled
        self.step = step
        self.TapSchedules = TapSchedules
        self.highStep = highStep
        self.lowStep = lowStep
        self.ltcFlag = ltcFlag
        self.neutralStep = neutralStep
        self.neutralU = neutralU
        self.normalStep = normalStep
        self.TapChangerControl = TapChangerControl
        self.SvTapStep = SvTapStep

    def __str__(self):
        str = "class=TapChanger\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
