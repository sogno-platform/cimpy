from cimpy.cgmes_v2_4_15.Equipment import Equipment


class GeneratingUnit(Equipment):
	'''
	A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.

	:genControlSource: The source of controls for a generating unit. Default: 
	:governorSCD: Governor Speed Changer Droop.   This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency. Default: 
	:initialP: Default initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration. Default: 
	:longPF: Generating unit long term economic participation factor. Default: 
	:maximumAllowableSpinningReserve: Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point. Default: 
	:maxOperatingP: This is the maximum operating active power limit the dispatcher can enter for this unit. Default: 
	:minOperatingP: This is the minimum operating active power limit the dispatcher can enter for this unit. Default: 
	:nominalP: The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes such as the governor speed change droop (governorSCD attribute). The attribute shall be a positive value equal or less than RotatingMachine.ratedS. Default: 
	:ratedGrossMaxP: The unit`s gross rated maximum capacity (book value). Default: 
	:ratedGrossMinP: The gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission grid. Default: 
	:ratedNetMaxP: The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity. Default: 
	:shortPF: Generating unit short term economic participation factor. Default: 
	:startupCost: The initial startup cost incurred for each start of the GeneratingUnit. Default: 
	:variableCost: The variable cost component of production per unit of ActivePower. Default: 
	:totalEfficiency: The efficiency of the unit in converting the fuel into electrical energy. Default: 
	:ControlAreaGeneratingUnit: ControlArea specifications for this generating unit. Default: 
	:RotatingMachine: A synchronous machine may operate as a generator and as such becomes a member of a generating unit. Default: 
	:GrossToNetActivePowerCurves: A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit. Default: 
	:normalPF: Generating unit economic participation factor. Default: 
		'''

	cgmesProfile = Equipment.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.SSH.value, ],
						'genControlSource': [cgmesProfile.EQ.value, ],
						'governorSCD': [cgmesProfile.EQ.value, ],
						'initialP': [cgmesProfile.EQ.value, ],
						'longPF': [cgmesProfile.EQ.value, ],
						'maximumAllowableSpinningReserve': [cgmesProfile.EQ.value, ],
						'maxOperatingP': [cgmesProfile.EQ.value, ],
						'minOperatingP': [cgmesProfile.EQ.value, ],
						'nominalP': [cgmesProfile.EQ.value, ],
						'ratedGrossMaxP': [cgmesProfile.EQ.value, ],
						'ratedGrossMinP': [cgmesProfile.EQ.value, ],
						'ratedNetMaxP': [cgmesProfile.EQ.value, ],
						'shortPF': [cgmesProfile.EQ.value, ],
						'startupCost': [cgmesProfile.EQ.value, ],
						'variableCost': [cgmesProfile.EQ.value, ],
						'totalEfficiency': [cgmesProfile.EQ.value, ],
						'ControlAreaGeneratingUnit': [cgmesProfile.EQ.value, ],
						'RotatingMachine': [cgmesProfile.EQ.value, ],
						'GrossToNetActivePowerCurves': [cgmesProfile.EQ.value, ],
						'normalPF': [cgmesProfile.SSH.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class Equipment: \n' + Equipment.__doc__ 

	def __init__(self, genControlSource = , governorSCD = , initialP = , longPF = , maximumAllowableSpinningReserve = , maxOperatingP = , minOperatingP = , nominalP = , ratedGrossMaxP = , ratedGrossMinP = , ratedNetMaxP = , shortPF = , startupCost = , variableCost = , totalEfficiency = , ControlAreaGeneratingUnit = , RotatingMachine = , GrossToNetActivePowerCurves = , normalPF = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.genControlSource = genControlSource
		self.governorSCD = governorSCD
		self.initialP = initialP
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
		self.totalEfficiency = totalEfficiency
		self.ControlAreaGeneratingUnit = ControlAreaGeneratingUnit
		self.RotatingMachine = RotatingMachine
		self.GrossToNetActivePowerCurves = GrossToNetActivePowerCurves
		self.normalPF = normalPF
		
	def __str__(self):
		str = 'class=GeneratingUnit\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
