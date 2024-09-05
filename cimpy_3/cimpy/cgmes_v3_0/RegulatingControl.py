from .PowerSystemResource import PowerSystemResource


class RegulatingControl(PowerSystemResource):
    """
    Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.  Remote bus voltage control is possible by specifying the controlled terminal located at some place remote from the controlling equipment. The specified terminal shall be associated with the connectivity node of the controlled point.  The most specific subtype of RegulatingControl shall be used in case such equipment participate in the control, e.g. TapChangerControl for tap changers. For flow control, load sign convention is used, i.e. positive sign means flow out from a TopologicalNode (bus) into the conducting equipment. The attribute minAllowedTargetValue and maxAllowedTargetValue are required in the following cases: - For a power generating module operated in power factor control mode to specify maximum and minimum power factor values; - Whenever it is necessary to have an off center target voltage for the tap changer regulator. For instance, due to long cables to off shore wind farms and the need to have a simpler setup at the off shore transformer platform, the voltage is controlled from the land at the connection point for the off shore wind farm. Since there usually is a voltage rise along the cable, there is typical and overvoltage of up 3-4 kV compared to the on shore station. Thus in normal operation the tap changer on the on shore station is operated with a target set point, which is in the lower parts of the dead band. The attributes minAllowedTargetValue and maxAllowedTargetValue are not related to the attribute targetDeadband and thus they are not treated as an alternative of the targetDeadband. They are needed due to limitations in the local substation controller. The attribute targetDeadband is used to prevent the power flow from move the tap position in circles (hunting) that is to be used regardless of the attributes minAllowedTargetValue and maxAllowedTargetValue.

    :discrete: The regulation is performed in a discrete mode. This applies to equipment with discrete controls, e.g. tap changers and shunt compensators. Default: False
    :enabled: The flag tells if regulation is enabled. Default: False
    :targetDeadband: This is a deadband used with discrete control to avoid excessive update of controls like tap changers and shunt compensator banks while regulating.  The units of those appropriate for the mode. The attribute shall be a positive value or zero. If RegulatingControl.discrete is set to `false`, the RegulatingControl.targetDeadband is to be ignored. Note that for instance, if the targetValue is 100 kV and the targetDeadband is 2 kV the range is from 99 to 101 kV. Default: 0.0
    :targetValue: The target value specified for case input.   This value can be used for the target value without the use of schedules. The value has the units appropriate to the mode attribute. Default: 0.0
    :targetValueUnitMultiplier: Specify the multiplier for used for the targetValue. Default: None
    :maxAllowedTargetValue: Maximum allowed target value (RegulatingControl.targetValue). Default: 0.0
    :minAllowedTargetValue: Minimum allowed target value (RegulatingControl.targetValue). Default: 0.0
    :RegulationSchedule: Schedule for this regulating control. Default: "list"
    :RegulatingCondEq: The equipment that participates in this regulating control scheme. Default: "list"
    :mode: The regulating control mode presently available.  This specification allows for determining the kind of regulation without need for obtaining the units from a schedule. Default: None
    :Terminal: The terminal associated with this regulating control.  The terminal is associated instead of a node, since the terminal could connect into either a topological node or a connectivity node.  Sometimes it is useful to model regulation at a terminal of a bus bar object. Default: None
    """

    cgmesProfile = PowerSystemResource.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
        ],
        "discrete": [
            cgmesProfile.SSH.value,
        ],
        "enabled": [
            cgmesProfile.SSH.value,
        ],
        "targetDeadband": [
            cgmesProfile.SSH.value,
        ],
        "targetValue": [
            cgmesProfile.SSH.value,
        ],
        "targetValueUnitMultiplier": [
            cgmesProfile.SSH.value,
        ],
        "maxAllowedTargetValue": [
            cgmesProfile.SSH.value,
        ],
        "minAllowedTargetValue": [
            cgmesProfile.SSH.value,
        ],
        "RegulationSchedule": [
            cgmesProfile.EQ.value,
        ],
        "RegulatingCondEq": [
            cgmesProfile.EQ.value,
        ],
        "mode": [
            cgmesProfile.EQ.value,
        ],
        "Terminal": [
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class PowerSystemResource: \n"
        + PowerSystemResource.__doc__
    )

    def __init__(
        self,
        discrete=False,
        enabled=False,
        targetDeadband=0.0,
        targetValue=0.0,
        targetValueUnitMultiplier=None,
        maxAllowedTargetValue=0.0,
        minAllowedTargetValue=0.0,
        RegulationSchedule="list",
        RegulatingCondEq="list",
        mode=None,
        Terminal=None,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.discrete = discrete
        self.enabled = enabled
        self.targetDeadband = targetDeadband
        self.targetValue = targetValue
        self.targetValueUnitMultiplier = targetValueUnitMultiplier
        self.maxAllowedTargetValue = maxAllowedTargetValue
        self.minAllowedTargetValue = minAllowedTargetValue
        self.RegulationSchedule = RegulationSchedule
        self.RegulatingCondEq = RegulatingCondEq
        self.mode = mode
        self.Terminal = Terminal

    def __str__(self):
        str = "class=RegulatingControl\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
