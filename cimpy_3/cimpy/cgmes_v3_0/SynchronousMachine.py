from .RotatingMachine import RotatingMachine


class SynchronousMachine(RotatingMachine):
    """
    An electromechanical device that operates with shaft rotating synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.

    :SynchronousMachineDynamics: Synchronous machine dynamics model used to describe dynamic behaviour of this synchronous machine. Default: None
    :operatingMode: Current mode of operation. Default: None
    :referencePriority: Priority of unit for use as powerflow voltage phase angle reference bus selection. 0 = don t care (default) 1 = highest priority. 2 is less than 1 and so on. Default: 0
    :InitialReactiveCapabilityCurve: The default reactive capability curve for use by a synchronous machine. Default: None
    :maxQ: Maximum reactive power limit. This is the maximum (nameplate) limit for the unit. Default: 0.0
    :minQ: Minimum reactive power limit for the unit. Default: 0.0
    :qPercent: Part of the coordinated reactive control that comes from this machine. The attribute is used as a participation factor not necessarily summing up to 100% for the participating devices in the control. Default: 0.0
    :type: Modes that this synchronous machine can operate in. Default: None
    :earthing: Indicates whether or not the generator is earthed. Used for short circuit data exchange according to IEC 60909. Default: False
    :earthingStarPointR: Generator star point earthing resistance (Re). Used for short circuit data exchange according to IEC 60909. Default: 0.0
    :earthingStarPointX: Generator star point earthing reactance (Xe). Used for short circuit data exchange according to IEC 60909. Default: 0.0
    :ikk: Steady-state short-circuit current (in A for the profile) of generator with compound excitation during 3-phase short circuit. - Ikk=0: Generator with no compound excitation. - Ikk&lt;&gt;0: Generator with compound excitation. Ikk is used to calculate the minimum steady-state short-circuit current for generators with compound excitation. (4.6.1.2 in IEC 60909-0:2001). Used only for single fed short circuit on a generator. (4.3.4.2. in IEC 60909-0:2001). Default: 0.0
    :mu: Factor to calculate the breaking current (Section 4.5.2.1 in IEC 60909-0). Used only for single fed short circuit on a generator (Section 4.3.4.2. in IEC 60909-0). Default: 0.0
    :x0: Zero sequence reactance of the synchronous machine. Default: 0.0
    :r0: Zero sequence resistance of the synchronous machine. Default: 0.0
    :x2: Negative sequence reactance. Default: 0.0
    :r2: Negative sequence resistance. Default: 0.0
    :r: Equivalent resistance (RG) of generator. RG is considered for the calculation of all currents, except for the calculation of the peak current ip. Used for short circuit data exchange according to IEC 60909. Default: 0.0
    :satDirectSubtransX: Direct-axis subtransient reactance saturated, also known as Xd`sat. Default: 0.0
    :satDirectSyncX: Direct-axes saturated synchronous reactance (xdsat); reciprocal of short-circuit ration. Used for short circuit data exchange, only for single fed short circuit on a generator. (4.3.4.2. in IEC 60909-0:2001). Default: 0.0
    :satDirectTransX: Saturated Direct-axis transient reactance. The attribute is primarily used for short circuit calculations according to ANSI. Default: 0.0
    :shortCircuitRotorType: Type of rotor, used by short circuit applications, only for single fed short circuit according to IEC 60909. Default: None
    :voltageRegulationRange: Range of generator voltage regulation (PG in IEC 60909-0) used for calculation of the impedance correction factor KG defined in IEC 60909-0. This attribute is used to describe the operating voltage of the generating unit. Default: 0.0
    """

    cgmesProfile = RotatingMachine.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
            cgmesProfile.SC.value,
        ],
        "SynchronousMachineDynamics": [
            cgmesProfile.DY.value,
        ],
        "operatingMode": [
            cgmesProfile.SSH.value,
        ],
        "referencePriority": [
            cgmesProfile.SSH.value,
        ],
        "InitialReactiveCapabilityCurve": [
            cgmesProfile.EQ.value,
        ],
        "maxQ": [
            cgmesProfile.EQ.value,
        ],
        "minQ": [
            cgmesProfile.EQ.value,
        ],
        "qPercent": [
            cgmesProfile.EQ.value,
        ],
        "type": [
            cgmesProfile.EQ.value,
        ],
        "earthing": [
            cgmesProfile.SC.value,
        ],
        "earthingStarPointR": [
            cgmesProfile.SC.value,
        ],
        "earthingStarPointX": [
            cgmesProfile.SC.value,
        ],
        "ikk": [
            cgmesProfile.SC.value,
        ],
        "mu": [
            cgmesProfile.SC.value,
        ],
        "x0": [
            cgmesProfile.SC.value,
        ],
        "r0": [
            cgmesProfile.SC.value,
        ],
        "x2": [
            cgmesProfile.SC.value,
        ],
        "r2": [
            cgmesProfile.SC.value,
        ],
        "r": [
            cgmesProfile.SC.value,
        ],
        "satDirectSubtransX": [
            cgmesProfile.SC.value,
        ],
        "satDirectSyncX": [
            cgmesProfile.SC.value,
        ],
        "satDirectTransX": [
            cgmesProfile.SC.value,
        ],
        "shortCircuitRotorType": [
            cgmesProfile.SC.value,
        ],
        "voltageRegulationRange": [
            cgmesProfile.SC.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class RotatingMachine: \n" + RotatingMachine.__doc__
    )

    def __init__(
        self,
        SynchronousMachineDynamics=None,
        operatingMode=None,
        referencePriority=0,
        InitialReactiveCapabilityCurve=None,
        maxQ=0.0,
        minQ=0.0,
        qPercent=0.0,
        type=None,
        earthing=False,
        earthingStarPointR=0.0,
        earthingStarPointX=0.0,
        ikk=0.0,
        mu=0.0,
        x0=0.0,
        r0=0.0,
        x2=0.0,
        r2=0.0,
        r=0.0,
        satDirectSubtransX=0.0,
        satDirectSyncX=0.0,
        satDirectTransX=0.0,
        shortCircuitRotorType=None,
        voltageRegulationRange=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.SynchronousMachineDynamics = SynchronousMachineDynamics
        self.operatingMode = operatingMode
        self.referencePriority = referencePriority
        self.InitialReactiveCapabilityCurve = InitialReactiveCapabilityCurve
        self.maxQ = maxQ
        self.minQ = minQ
        self.qPercent = qPercent
        self.type = type
        self.earthing = earthing
        self.earthingStarPointR = earthingStarPointR
        self.earthingStarPointX = earthingStarPointX
        self.ikk = ikk
        self.mu = mu
        self.x0 = x0
        self.r0 = r0
        self.x2 = x2
        self.r2 = r2
        self.r = r
        self.satDirectSubtransX = satDirectSubtransX
        self.satDirectSyncX = satDirectSyncX
        self.satDirectTransX = satDirectTransX
        self.shortCircuitRotorType = shortCircuitRotorType
        self.voltageRegulationRange = voltageRegulationRange

    def __str__(self):
        str = "class=SynchronousMachine\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str