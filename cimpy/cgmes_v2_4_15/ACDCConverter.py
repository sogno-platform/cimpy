from cimpy.cgmes_v2_4_15_flat.ConductingEquipment import ConductingEquipment


class ACDCConverter(ConductingEquipment):
	'''
	A unit with valves for three phases, together with unit control equipment, essential protective and switching devices, DC storage capacitors, phase reactors and auxiliaries, if any, used for conversion.

	:baseS: Base apparent power of the converter pole. Default: 0.0
	:idleLoss: Active power loss in pole at no power transfer. Converter configuration data used in power flow. Default: 0.0
	:maxUdc: The maximum voltage on the DC side at which the converter should operate. Converter configuration data used in power flow. Default: 0.0
	:minUdc: Min allowed converter DC voltage. Converter configuration data used in power flow. Default: 0.0
	:numberOfValves: Number of valves in the converter. Used in loss calculations. Default: 0
	:ratedUdc: Rated converter DC voltage, also called UdN. Converter configuration data used in power flow. Default: 0.0
	:resistiveLoss: Converter configuration data used in power flow. Refer to poleLossP. Default: 0.0
	:switchingLoss: Switching losses, relative to the base apparent power 'baseS'. Refer to poleLossP. Default: 0.0
	:valveU0: Valve threshold voltage. Forward voltage drop when the valve is conducting. Used in loss calculations, i.e. the switchLoss depend on numberOfValves * valveU0. Default: 0.0
	:DCTerminals:  Default: []
	:PccTerminal: All converters' DC sides linked to this point of common coupling terminal. Default: None
	:idc: Converter DC current, also called Id. Converter state variable, result from power flow. Default: 0.0
	:poleLossP: The active power loss at a DC Pole  = idleLoss + switchingLoss*|Idc| + resitiveLoss*Idc^2 For lossless operation Pdc=Pac For rectifier operation with losses Pdc=Pac-lossP For inverter operation with losses Pdc=Pac+lossP Converter state variable used in power flow. Default: 0.0
	:uc: Converter voltage, the voltage at the AC side of the bridge. Converter state variable, result from power flow. Default: 0.0
	:udc: Converter voltage at the DC side, also called Ud. Converter state variable, result from power flow. Default: 0.0
	:p: Active power at the point of common coupling. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution in the case a simplified power flow model is used. Default: 0.0
	:q: Reactive power at the point of common coupling. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution in the case a simplified power flow model is used. Default: 0.0
	:targetPpcc: Real power injection target in AC grid, at point of common coupling. Default: 0.0
	:targetUdc: Target value for DC voltage magnitude. Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.SV.value, cgmesProfile.SSH.value, ],
						'baseS': [cgmesProfile.EQ.value, ],
						'idleLoss': [cgmesProfile.EQ.value, ],
						'maxUdc': [cgmesProfile.EQ.value, ],
						'minUdc': [cgmesProfile.EQ.value, ],
						'numberOfValves': [cgmesProfile.EQ.value, ],
						'ratedUdc': [cgmesProfile.EQ.value, ],
						'resistiveLoss': [cgmesProfile.EQ.value, ],
						'switchingLoss': [cgmesProfile.EQ.value, ],
						'valveU0': [cgmesProfile.EQ.value, ],
						'DCTerminals': [cgmesProfile.EQ.value, ],
						'PccTerminal': [cgmesProfile.EQ.value, ],
						'idc': [cgmesProfile.SV.value, ],
						'poleLossP': [cgmesProfile.SV.value, ],
						'uc': [cgmesProfile.SV.value, ],
						'udc': [cgmesProfile.SV.value, ],
						'p': [cgmesProfile.SSH.value, ],
						'q': [cgmesProfile.SSH.value, ],
						'targetPpcc': [cgmesProfile.SSH.value, ],
						'targetUdc': [cgmesProfile.SSH.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ConductingEquipment: \n' + ConductingEquipment.__doc__ 

	def __init__(self, baseS = 0.0, idleLoss = 0.0, maxUdc = 0.0, minUdc = 0.0, numberOfValves = 0, ratedUdc = 0.0, resistiveLoss = 0.0, switchingLoss = 0.0, valveU0 = 0.0, DCTerminals = [], PccTerminal = None, idc = 0.0, poleLossP = 0.0, uc = 0.0, udc = 0.0, p = 0.0, q = 0.0, targetPpcc = 0.0, targetUdc = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.baseS = baseS
		self.idleLoss = idleLoss
		self.maxUdc = maxUdc
		self.minUdc = minUdc
		self.numberOfValves = numberOfValves
		self.ratedUdc = ratedUdc
		self.resistiveLoss = resistiveLoss
		self.switchingLoss = switchingLoss
		self.valveU0 = valveU0
		self.DCTerminals = DCTerminals
		self.PccTerminal = PccTerminal
		self.idc = idc
		self.poleLossP = poleLossP
		self.uc = uc
		self.udc = udc
		self.p = p
		self.q = q
		self.targetPpcc = targetPpcc
		self.targetUdc = targetUdc
		
	def __str__(self):
		str = 'class=ACDCConverter\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
