from .IdentifiedObject import IdentifiedObject
from .CGMESProfile import Profile


class TransformerEnd(IdentifiedObject):
    """
    A conducting connection point of a power transformer. It corresponds to a physical transformer winding terminal.  In earlier CIM versions, the TransformerWinding class served a similar purpose, but this class is more flexible because it associates to terminal but is not a specialization of ConductingEquipment.

    :BaseVoltage: Base voltage of the transformer end.  This is essential for PU calculation. Default: None
    :PhaseTapChanger: Transformer end to which this phase tap changer belongs. Default: None
    :RatioTapChanger: Transformer end to which this ratio tap changer belongs. Default: None
    :Terminal: Terminal of the power transformer to which this transformer end belongs. Default: None
    :endNumber: Number for this transformer end, corresponding to the end`s order in the power transformer vector group or phase angle clock number.  Highest voltage winding should be 1.  Each end within a power transformer should have a unique subsequent end number.   Note the transformer end number need not match the terminal sequence number. Default: 0
    :grounded: (for Yn and Zn connections) True if the neutral is solidly grounded. Default: False
    :rground: (for Yn and Zn connections) Resistance part of neutral impedance where `grounded` is true. Default: 0.0
    :xground: (for Yn and Zn connections) Reactive part of neutral impedance where `grounded` is true. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, ],
        "BaseVoltage": [Profile.EQ.value, ],
        "PhaseTapChanger": [Profile.EQ.value, ],
        "RatioTapChanger": [Profile.EQ.value, ],
        "Terminal": [Profile.EQ.value, ],
        "endNumber": [Profile.EQ.value, ],
        "grounded": [Profile.EQ.value, ],
        "rground": [Profile.EQ.value, ],
        "xground": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class IdentifiedObject:\n" + IdentifiedObject.__doc__

    def __init__(self, BaseVoltage = None, PhaseTapChanger = None, RatioTapChanger = None, Terminal = None, endNumber = 0, grounded = False, rground = 0.0, xground = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.BaseVoltage = BaseVoltage
        self.PhaseTapChanger = PhaseTapChanger
        self.RatioTapChanger = RatioTapChanger
        self.Terminal = Terminal
        self.endNumber = endNumber
        self.grounded = grounded
        self.rground = rground
        self.xground = xground

    def __str__(self):
        str = "class=TransformerEnd\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
