from .Equipment import Equipment


class GeneratingUnit(Equipment):
    """
    A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.

    :normalPF: Generating unit economic participation factor.  The sum of the participation factors across generating units does not have to sum to one.  It is used for representing distributed slack participation factor. The attribute shall be a positive value or zero. Default: 0.0
    :ControlAreaGeneratingUnit: ControlArea specifications for this generating unit. Default: "list"
    :genControlSource: The source of controls for a generating unit.  Defines the control status of the generating unit. Default: None
    :governorSCD: Governor Speed Changer Droop.   This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency. Default: 0.0
    :longPF: Generating unit long term economic participation factor. Default: 0.0
    :maximumAllowableSpinningReserve: Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point. Default: 0.0
    :maxOperatingP: This is the maximum operating active power limit the dispatcher can enter for this unit. Default: 0.0
    :minOperatingP: This is the minimum operating active power limit the dispatcher can enter for this unit. Default: 0.0
    :nominalP: The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes such as the governor speed change droop (governorSCD attribute). The attribute shall be a positive value equal to or less than RotatingMachine.ratedS. Default: 0.0
    :ratedGrossMaxP: The unit`s gross rated maximum capacity (book value). The attribute shall be a positive value. Default: 0.0
    :ratedGrossMinP: The gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission grid. The attribute shall be a positive value. Default: 0.0
    :ratedNetMaxP: The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity. The attribute shall be a positive value. Default: 0.0
    :shortPF: Generating unit short term economic participation factor. Default: 0.0
    :startupCost: The initial startup cost incurred for each start of the GeneratingUnit. Default: 0.0
    :variableCost: The variable cost component of production per unit of ActivePower. Default: 0.0
    :startupTime: Time it takes to get the unit on-line, from the time that the prime mover mechanical power is applied. Default: 0
    :totalEfficiency: The efficiency of the unit in converting the fuel into electrical energy. Default: 0.0
    :GrossToNetActivePowerCurves: A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit. Default: "list"
    :RotatingMachine: A synchronous machine may operate as a generator and as such becomes a member of a generating unit. Default: "list"
    """

    cgmesProfile = Equipment.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
        ],
        "normalPF": [
            cgmesProfile.SSH.value,
        ],
        "ControlAreaGeneratingUnit": [
            cgmesProfile.EQ.value,
        ],
        "genControlSource": [
            cgmesProfile.EQ.value,
        ],
        "governorSCD": [
            cgmesProfile.EQ.value,
        ],
        "longPF": [
            cgmesProfile.EQ.value,
        ],
        "maximumAllowableSpinningReserve": [
            cgmesProfile.EQ.value,
        ],
        "maxOperatingP": [
            cgmesProfile.EQ.value,
        ],
        "minOperatingP": [
            cgmesProfile.EQ.value,
        ],
        "nominalP": [
            cgmesProfile.EQ.value,
        ],
        "ratedGrossMaxP": [
            cgmesProfile.EQ.value,
        ],
        "ratedGrossMinP": [
            cgmesProfile.EQ.value,
        ],
        "ratedNetMaxP": [
            cgmesProfile.EQ.value,
        ],
        "shortPF": [
            cgmesProfile.EQ.value,
        ],
        "startupCost": [
            cgmesProfile.EQ.value,
        ],
        "variableCost": [
            cgmesProfile.EQ.value,
        ],
        "startupTime": [
            cgmesProfile.EQ.value,
        ],
        "totalEfficiency": [
            cgmesProfile.EQ.value,
        ],
        "GrossToNetActivePowerCurves": [
            cgmesProfile.EQ.value,
        ],
        "RotatingMachine": [
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    __doc__ += "\n Documentation of parent class Equipment: \n" + Equipment.__doc__

    def __init__(
        self,
        normalPF=0.0,
        ControlAreaGeneratingUnit="list",
        genControlSource=None,
        governorSCD=0.0,
        longPF=0.0,
        maximumAllowableSpinningReserve=0.0,
        maxOperatingP=0.0,
        minOperatingP=0.0,
        nominalP=0.0,
        ratedGrossMaxP=0.0,
        ratedGrossMinP=0.0,
        ratedNetMaxP=0.0,
        shortPF=0.0,
        startupCost=0.0,
        variableCost=0.0,
        startupTime=0,
        totalEfficiency=0.0,
        GrossToNetActivePowerCurves="list",
        RotatingMachine="list",
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.normalPF = normalPF
        self.ControlAreaGeneratingUnit = ControlAreaGeneratingUnit
        self.genControlSource = genControlSource
        self.governorSCD = governorSCD
        self.longPF = longPF
        self.maximumAllowableSpinningReserve = maximumAllowableSpinningReserve
        self.maxOperatingP = maxOperatingP
        self.minOperatingP = minOperatingP
        self.nominalP = nominalP
        self.ratedGrossMaxP = ratedGrossMaxP
        self.ratedGrossMinP = ratedGrossMinP
        self.ratedNetMaxP = ratedNetMaxP
        self.shortPF = shortPF
        self.startupCost = startupCost
        self.variableCost = variableCost
        self.startupTime = startupTime
        self.totalEfficiency = totalEfficiency
        self.GrossToNetActivePowerCurves = GrossToNetActivePowerCurves
        self.RotatingMachine = RotatingMachine

    def __str__(self):
        str = "class=GeneratingUnit\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
