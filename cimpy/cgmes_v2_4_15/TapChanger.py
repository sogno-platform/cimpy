from .PowerSystemResource import PowerSystemResource
from .CGMESProfile import Profile


class TapChanger(PowerSystemResource):
    """
    Mechanism for changing transformer winding tap positions.

    :SvTapStep: The tap step state associated with the tap changer. Default: None
    :TapChangerControl: The tap changers that participates in this regulating tap control scheme. Default: None
    :TapSchedules: A TapSchedule is associated with a TapChanger. Default: "list"
    :controlEnabled: Specifies the regulation status of the equipment.  True is regulating, false is not regulating. Default: False
    :highStep: Highest possible tap step position, advance from neutral. The attribute shall be greater than lowStep. Default: 0
    :lowStep: Lowest possible tap step position, retard from neutral Default: 0
    :ltcFlag: Specifies whether or not a TapChanger has load tap changing capabilities. Default: False
    :neutralStep: The neutral tap step position for this winding. The attribute shall be equal or greater than lowStep and equal or less than highStep. Default: 0
    :neutralU: Voltage at which the winding operates at the neutral tap setting. Default: 0.0
    :normalStep: The tap step position used in `normal` network operation for this winding. For a `Fixed` tap changer indicates the current physical tap setting. The attribute shall be equal or greater than lowStep and equal or less than highStep. Default: 0
    :step: Tap changer position. Starting step for a steady state solution. Non integer values are allowed to support continuous tap variables. The reasons for continuous value are to support study cases where no discrete tap changers has yet been designed, a solutions where a narrow voltage band force the tap step to oscillate or accommodate for a continuous solution as input. The attribute shall be equal or greater than lowStep and equal or less than highStep. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, Profile.SV.value, Profile.SSH.value, ],
        "SvTapStep": [Profile.SV.value, ],
        "TapChangerControl": [Profile.EQ.value, ],
        "TapSchedules": [Profile.EQ.value, ],
        "controlEnabled": [Profile.SSH.value, ],
        "highStep": [Profile.EQ.value, ],
        "lowStep": [Profile.EQ.value, ],
        "ltcFlag": [Profile.EQ.value, ],
        "neutralStep": [Profile.EQ.value, ],
        "neutralU": [Profile.EQ.value, ],
        "normalStep": [Profile.EQ.value, ],
        "step": [Profile.SSH.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class PowerSystemResource:\n" + PowerSystemResource.__doc__

    def __init__(self, SvTapStep = None, TapChangerControl = None, TapSchedules = "list", controlEnabled = False, highStep = 0, lowStep = 0, ltcFlag = False, neutralStep = 0, neutralU = 0.0, normalStep = 0, step = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.SvTapStep = SvTapStep
        self.TapChangerControl = TapChangerControl
        self.TapSchedules = TapSchedules
        self.controlEnabled = controlEnabled
        self.highStep = highStep
        self.lowStep = lowStep
        self.ltcFlag = ltcFlag
        self.neutralStep = neutralStep
        self.neutralU = neutralU
        self.normalStep = normalStep
        self.step = step

    def __str__(self):
        str = "class=TapChanger\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
