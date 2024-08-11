from .RotatingMachine import RotatingMachine
from .CGMESProfile import Profile


class SynchronousMachine(RotatingMachine):
    """
    An electromechanical device that operates with shaft rotating synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.

    :InitialReactiveCapabilityCurve: Synchronous machines using this curve as default. Default: None
    :SynchronousMachineDynamics: Synchronous machine dynamics model used to describe dynamic behavior of this synchronous machine. Default: None
    :earthing: Indicates whether or not the generator is earthed. Used for short circuit data exchange according to IEC 60909 Default: False
    :earthingStarPointR: Generator star point earthing resistance (Re). Used for short circuit data exchange according to IEC 60909 Default: 0.0
    :earthingStarPointX: Generator star point earthing reactance (Xe). Used for short circuit data exchange according to IEC 60909 Default: 0.0
    :ikk: Steady-state short-circuit current (in A for the profile) of generator with compound excitation during 3-phase short circuit. - Ikk=0: Generator with no compound excitation. - Ikk?0: Generator with compound excitation. Ikk is used to calculate the minimum steady-state short-circuit current for generators with compound excitation (Section 4.6.1.2 in the IEC 60909-0) Used only for single fed short circuit on a generator. (Section 4.3.4.2. in the IEC 60909-0) Default: 0.0
    :maxQ: Maximum reactive power limit. This is the maximum (nameplate) limit for the unit. Default: 0.0
    :minQ: Minimum reactive power limit for the unit. Default: 0.0
    :mu: Factor to calculate the breaking current (Section 4.5.2.1 in the IEC 60909-0). Used only for single fed short circuit on a generator (Section 4.3.4.2. in the IEC 60909-0). Default: 0.0
    :operatingMode: Current mode of operation. Default: None
    :qPercent: Percent of the coordinated reactive control that comes from this machine. Default: 0.0
    :r: Equivalent resistance (RG) of generator. RG is considered for the calculation of all currents, except for the calculation of the peak current ip. Used for short circuit data exchange according to IEC 60909 Default: 0.0
    :r0: Zero sequence resistance of the synchronous machine. Default: 0.0
    :r2: Negative sequence resistance. Default: 0.0
    :referencePriority: Priority of unit for use as powerflow voltage phase angle reference bus selection. 0 = don t care (default) 1 = highest priority. 2 is less than 1 and so on. Default: 0
    :satDirectSubtransX: Direct-axis subtransient reactance saturated, also known as Xd`sat. Default: 0.0
    :satDirectSyncX: Direct-axes saturated synchronous reactance (xdsat); reciprocal of short-circuit ration. Used for short circuit data exchange, only for single fed short circuit on a generator. (Section 4.3.4.2. in the IEC 60909-0). Default: 0.0
    :satDirectTransX: Saturated Direct-axis transient reactance. The attribute is primarily used for short circuit calculations according to ANSI. Default: 0.0
    :shortCircuitRotorType: Type of rotor, used by short circuit applications, only for single fed short circuit according to IEC 60909. Default: None
    :type: Modes that this synchronous machine can operate in. Default: None
    :voltageRegulationRange: Range of generator voltage regulation (PG in the IEC 60909-0) used for calculation of the impedance correction factor KG defined in IEC 60909-0 This attribute is used to describe the operating voltage of the generating unit. Default: 0.0
    :x0: Zero sequence reactance of the synchronous machine. Default: 0.0
    :x2: Negative sequence reactance. Default: 0.0
    """

    possibleProfileList = {
        "class": [Profile.DY.value, Profile.EQ.value, Profile.SSH.value, ],
        "InitialReactiveCapabilityCurve": [Profile.EQ.value, ],
        "SynchronousMachineDynamics": [Profile.DY.value, ],
        "earthing": [Profile.EQ.value, ],
        "earthingStarPointR": [Profile.EQ.value, ],
        "earthingStarPointX": [Profile.EQ.value, ],
        "ikk": [Profile.EQ.value, ],
        "maxQ": [Profile.EQ.value, ],
        "minQ": [Profile.EQ.value, ],
        "mu": [Profile.EQ.value, ],
        "operatingMode": [Profile.SSH.value, ],
        "qPercent": [Profile.EQ.value, ],
        "r": [Profile.EQ.value, ],
        "r0": [Profile.EQ.value, ],
        "r2": [Profile.EQ.value, ],
        "referencePriority": [Profile.SSH.value, ],
        "satDirectSubtransX": [Profile.EQ.value, ],
        "satDirectSyncX": [Profile.EQ.value, ],
        "satDirectTransX": [Profile.EQ.value, ],
        "shortCircuitRotorType": [Profile.EQ.value, ],
        "type": [Profile.EQ.value, ],
        "voltageRegulationRange": [Profile.EQ.value, ],
        "x0": [Profile.EQ.value, ],
        "x2": [Profile.EQ.value, ],
    }

    serializationProfile = {}

    __doc__ += "\nDocumentation of parent class RotatingMachine:\n" + RotatingMachine.__doc__

    def __init__(self, InitialReactiveCapabilityCurve = None, SynchronousMachineDynamics = None, earthing = False, earthingStarPointR = 0.0, earthingStarPointX = 0.0, ikk = 0.0, maxQ = 0.0, minQ = 0.0, mu = 0.0, operatingMode = None, qPercent = 0.0, r = 0.0, r0 = 0.0, r2 = 0.0, referencePriority = 0, satDirectSubtransX = 0.0, satDirectSyncX = 0.0, satDirectTransX = 0.0, shortCircuitRotorType = None, type = None, voltageRegulationRange = 0.0, x0 = 0.0, x2 = 0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.InitialReactiveCapabilityCurve = InitialReactiveCapabilityCurve
        self.SynchronousMachineDynamics = SynchronousMachineDynamics
        self.earthing = earthing
        self.earthingStarPointR = earthingStarPointR
        self.earthingStarPointX = earthingStarPointX
        self.ikk = ikk
        self.maxQ = maxQ
        self.minQ = minQ
        self.mu = mu
        self.operatingMode = operatingMode
        self.qPercent = qPercent
        self.r = r
        self.r0 = r0
        self.r2 = r2
        self.referencePriority = referencePriority
        self.satDirectSubtransX = satDirectSubtransX
        self.satDirectSyncX = satDirectSyncX
        self.satDirectTransX = satDirectTransX
        self.shortCircuitRotorType = shortCircuitRotorType
        self.type = type
        self.voltageRegulationRange = voltageRegulationRange
        self.x0 = x0
        self.x2 = x2

    def __str__(self):
        str = "class=SynchronousMachine\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
