from .PowerSystemResource import PowerSystemResource
from .CGMESProfile import Profile


class RegulatingControl(PowerSystemResource):
    """
    Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.  Remote bus voltage control is possible by specifying the controlled terminal located at some place remote from the controlling equipment. In case multiple equipment, possibly of different types, control same terminal there must be only one RegulatingControl at that terminal. The most specific subtype of RegulatingControl shall be used in case such equipment participate in the control, e.g. TapChangerControl for tap changers. For flow control  load sign convention is used, i.e. positive sign means flow out from a TopologicalNode (bus) into the conducting equipment.

    :RegulatingCondEq: The equipment that participates in this regulating control scheme. Default: "list"
    :RegulationSchedule: Schedule for this Regulating regulating control. Default: "list"
    :Terminal: The controls regulating this terminal. Default: None
    :discrete: The regulation is performed in a discrete mode. This applies to equipment with discrete controls, e.g. tap changers and shunt compensators. Default: False
    :enabled: The flag tells if regulation is enabled. Default: False
    :mode: The regulating control mode presently available.  This specification allows for determining the kind of regulation without need for obtaining the units from a schedule. Default: None
    :targetDeadband: This is a deadband used with discrete control to avoid excessive update of controls like tap changers and shunt compensator banks while regulating. The units of those appropriate for the mode. Default: 0.0
    :targetValue: The target value specified for case input.   This value can be used for the target value without the use of schedules. The value has the units appropriate to the mode attribute. Default: 0.0
    :targetValueUnitMultiplier: Specify the multiplier for used for the targetValue. Default: None
    """

    possibleProfileList = {
        "class": [Profile.EQ.value, Profile.SSH.value, ],
        "RegulatingCondEq": [Profile.EQ.value, ],
        "RegulationSchedule": [Profile.EQ.value, ],
        "Terminal": [Profile.EQ.value, ],
        "discrete": [Profile.SSH.value, ],
        "enabled": [Profile.SSH.value, ],
        "mode": [Profile.EQ.value, ],
        "targetDeadband": [Profile.SSH.value, ],
        "targetValue": [Profile.SSH.value, ],
        "targetValueUnitMultiplier": [Profile.SSH.value, ],
    }

    serializationProfile = {}

    recommendedClassProfile = Profile.EQ.value

    __doc__ += "\nDocumentation of parent class PowerSystemResource:\n" + PowerSystemResource.__doc__

    def __init__(self, RegulatingCondEq = "list", RegulationSchedule = "list", Terminal = None, discrete = False, enabled = False, mode = None, targetDeadband = 0.0, targetValue = 0.0, targetValueUnitMultiplier = None, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.RegulatingCondEq = RegulatingCondEq
        self.RegulationSchedule = RegulationSchedule
        self.Terminal = Terminal
        self.discrete = discrete
        self.enabled = enabled
        self.mode = mode
        self.targetDeadband = targetDeadband
        self.targetValue = targetValue
        self.targetValueUnitMultiplier = targetValueUnitMultiplier

    def __str__(self):
        str = "class=RegulatingControl\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
