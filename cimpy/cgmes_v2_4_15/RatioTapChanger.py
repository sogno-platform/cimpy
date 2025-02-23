from .TapChanger import TapChanger
from .CGMESProfile import Profile


class RatioTapChanger(TapChanger):
    """
    A tap changer that changes the voltage ratio impacting the voltage magnitude but not the phase angle across the transformer.

    :RatioTapChangerTable: The ratio tap changer of this tap ratio table. Default: None
    :TransformerEnd: Ratio tap changer associated with this transformer end. Default: None
    :stepVoltageIncrement: Tap step increment, in per cent of nominal voltage, per step position. Default: 0.0
    :tculControlMode: Specifies the regulation control mode (voltage or reactive) of the RatioTapChanger. Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, Profile.SSH.value, ],
        "RatioTapChangerTable": [Profile.EQ.value, ],
        "TransformerEnd": [Profile.EQ.value, ],
        "stepVoltageIncrement": [Profile.EQ.value, ],
        "tculControlMode": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class TapChanger:\n" + TapChanger.__doc__

    def __init__(self, RatioTapChangerTable = None, TransformerEnd = None, stepVoltageIncrement = 0.0, tculControlMode = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.RatioTapChangerTable = RatioTapChangerTable
        self.TransformerEnd = TransformerEnd
        self.stepVoltageIncrement = stepVoltageIncrement
        self.tculControlMode = tculControlMode

    def __str__(self):
        str = "class=RatioTapChanger\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(repr(attributes[key]))
        return str
