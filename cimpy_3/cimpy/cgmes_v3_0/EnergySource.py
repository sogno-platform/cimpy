from .EnergyConnection import EnergyConnection


class EnergySource(EnergyConnection):
    """
    A generic equivalent for an energy supplier on a transmission or distribution voltage level.

    :activePower: High voltage source active injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for steady state solutions. Default: 0.0
    :reactivePower: High voltage source reactive injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for steady state solutions. Default: 0.0
    :voltageAngle: Phase angle of a-phase open circuit used when voltage characteristics need to be imposed at the node associated with the terminal of the energy source, such as when voltages and angles from the transmission level are used as input to the distribution network. The attribute shall be a positive value or zero. Default: 0.0
    :voltageMagnitude: Phase-to-phase open circuit voltage magnitude used when voltage characteristics need to be imposed at the node associated with the terminal of the energy source, such as when voltages and angles from the transmission level are used as input to the distribution network. The attribute shall be a positive value or zero. Default: 0.0
    :EnergySchedulingType: Energy Scheduling Type of an Energy Source. Default: None
    :nominalVoltage: Phase-to-phase nominal voltage. Default: 0.0
    :pMin: This is the minimum active power that can be produced by the source. Load sign convention is used, i.e. positive sign means flow out from a TopologicalNode (bus) into the conducting equipment. Default: 0.0
    :pMax: This is the maximum active power that can be produced by the source. Load sign convention is used, i.e. positive sign means flow out from a TopologicalNode (bus) into the conducting equipment. Default: 0.0
    :r: Positive sequence Thevenin resistance. Default: 0.0
    :r0: Zero sequence Thevenin resistance. Default: 0.0
    :rn: Negative sequence Thevenin resistance. Default: 0.0
    :x: Positive sequence Thevenin reactance. Default: 0.0
    :x0: Zero sequence Thevenin reactance. Default: 0.0
    :xn: Negative sequence Thevenin reactance. Default: 0.0
    """

    cgmesProfile = EnergyConnection.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
            cgmesProfile.SC.value,
        ],
        "activePower": [
            cgmesProfile.SSH.value,
        ],
        "reactivePower": [
            cgmesProfile.SSH.value,
        ],
        "voltageAngle": [
            cgmesProfile.SSH.value,
        ],
        "voltageMagnitude": [
            cgmesProfile.SSH.value,
        ],
        "EnergySchedulingType": [
            cgmesProfile.EQ.value,
        ],
        "nominalVoltage": [
            cgmesProfile.EQ.value,
        ],
        "pMin": [
            cgmesProfile.EQ.value,
        ],
        "pMax": [
            cgmesProfile.EQ.value,
        ],
        "r": [
            cgmesProfile.SC.value,
        ],
        "r0": [
            cgmesProfile.SC.value,
        ],
        "rn": [
            cgmesProfile.SC.value,
        ],
        "x": [
            cgmesProfile.SC.value,
        ],
        "x0": [
            cgmesProfile.SC.value,
        ],
        "xn": [
            cgmesProfile.SC.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class EnergyConnection: \n"
        + EnergyConnection.__doc__
    )

    def __init__(
        self,
        activePower=0.0,
        reactivePower=0.0,
        voltageAngle=0.0,
        voltageMagnitude=0.0,
        EnergySchedulingType=None,
        nominalVoltage=0.0,
        pMin=0.0,
        pMax=0.0,
        r=0.0,
        r0=0.0,
        rn=0.0,
        x=0.0,
        x0=0.0,
        xn=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.activePower = activePower
        self.reactivePower = reactivePower
        self.voltageAngle = voltageAngle
        self.voltageMagnitude = voltageMagnitude
        self.EnergySchedulingType = EnergySchedulingType
        self.nominalVoltage = nominalVoltage
        self.pMin = pMin
        self.pMax = pMax
        self.r = r
        self.r0 = r0
        self.rn = rn
        self.x = x
        self.x0 = x0
        self.xn = xn

    def __str__(self):
        str = "class=EnergySource\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
