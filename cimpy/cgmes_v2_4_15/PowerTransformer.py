from cimpy.cgmes_v2_4_15.ConductingEquipment import ConductingEquipment


class PowerTransformer(ConductingEquipment):
	'''
	An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow). A power transformer may be composed of separate transformer tanks that need not be identical. A power transformer can be modeled with or without tanks and is intended for use in both balanced and unbalanced representations.   A power transformer typically has two terminals, but may have one (grounding), three or more terminals. The inherited association ConductingEquipment.BaseVoltage should not be used.  The association from TransformerEnd to BaseVoltage should be used instead.

	:PowerTransformerEnd: The power transformer of this power transformer end. Default: "many"
	:beforeShCircuitHighestOperatingCurrent: The highest operating current (Ib in the IEC 60909-0) before short circuit (depends on network configuration and relevant reliability philosophy). It is used for calculation of the impedance correction factor KT defined in IEC 60909-0. Default: 0.0
	:beforeShCircuitHighestOperatingVoltage: The highest operating voltage (Ub in the IEC 60909-0) before short circuit. It is used for calculation of the impedance correction factor KT defined in IEC 60909-0. This is worst case voltage on the low side winding (Section 3.7.1 in the standard). Used to define operating conditions. Default: 0.0
	:beforeShortCircuitAnglePf: The angle of power factor before short circuit (phib in the IEC 60909-0). It is used for calculation of the impedance correction factor KT defined in IEC 60909-0. This is the worst case power factor. Used to define operating conditions. Default: 0.0
	:highSideMinOperatingU: The minimum operating voltage (uQmin in the IEC 60909-0) at the high voltage side (Q side) of the unit transformer of the power station unit. A value well established from long-term operating experience of the system. It is used for calculation of the impedance correction factor KG defined in IEC 60909-0 Default: 0.0
	:isPartOfGeneratorUnit: Indicates whether the machine is part of a power station unit. Used for short circuit data exchange according to IEC 60909 Default: False
	:operationalValuesConsidered: It is used to define if the data (other attributes related to short circuit data exchange) defines long term operational conditions or not. Used for short circuit data exchange according to IEC 60909. Default: False
		'''

	cgmesProfile = ConductingEquipment.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'PowerTransformerEnd': [cgmesProfile.EQ.value, ],
						'beforeShCircuitHighestOperatingCurrent': [cgmesProfile.EQ.value, ],
						'beforeShCircuitHighestOperatingVoltage': [cgmesProfile.EQ.value, ],
						'beforeShortCircuitAnglePf': [cgmesProfile.EQ.value, ],
						'highSideMinOperatingU': [cgmesProfile.EQ.value, ],
						'isPartOfGeneratorUnit': [cgmesProfile.EQ.value, ],
						'operationalValuesConsidered': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ConductingEquipment: \n' + ConductingEquipment.__doc__ 

	def __init__(self, PowerTransformerEnd = "many", beforeShCircuitHighestOperatingCurrent = 0.0, beforeShCircuitHighestOperatingVoltage = 0.0, beforeShortCircuitAnglePf = 0.0, highSideMinOperatingU = 0.0, isPartOfGeneratorUnit = False, operationalValuesConsidered = False,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.PowerTransformerEnd = PowerTransformerEnd
		self.beforeShCircuitHighestOperatingCurrent = beforeShCircuitHighestOperatingCurrent
		self.beforeShCircuitHighestOperatingVoltage = beforeShCircuitHighestOperatingVoltage
		self.beforeShortCircuitAnglePf = beforeShortCircuitAnglePf
		self.highSideMinOperatingU = highSideMinOperatingU
		self.isPartOfGeneratorUnit = isPartOfGeneratorUnit
		self.operationalValuesConsidered = operationalValuesConsidered
		
	def __str__(self):
		str = 'class=PowerTransformer\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
