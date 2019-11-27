from cimpy.cgmes_v2_4_15.ACDCConverter import ACDCConverter


class VsConverter(ACDCConverter):
	'''
	DC side of the voltage source converter (VSC).

	:CapabilityCurve: All converters with this capability curve. Default: None
	:maxModulationIndex: The max quotient between the AC converter voltage (Uc) and DC voltage (Ud). A factor typically less than 1. VSC configuration data used in power flow. Default: 0.0
	:maxValveCurrent: The maximum current through a valve. This current limit is the basis for calculating the capability diagram. VSC  configuration data. Default: 0.0
	:delta: Angle between uf and uc. Converter state variable used in power flow. Default: 0.0
	:uf: Filter bus voltage. Converter state variable, result from power flow. Default: 0.0
	:droop: Droop constant; pu value is obtained as D [kV^2 / MW] x Sb / Ubdc^2. Default: 0.0
	:droopCompensation: Compensation (resistance) constant. Used to compensate for voltage drop when controlling voltage at a distant bus. Default: 0.0
	:pPccControl: Kind of control of real power and/or DC voltage. Default: None
	:qPccControl:  Default: None
	:qShare: Reactive power sharing factor among parallel converters on Uac control. Default: 0.0
	:targetQpcc: Reactive power injection target in AC grid, at point of common coupling. Default: 0.0
	:targetUpcc: Voltage target in AC grid, at point of common coupling. Default: 0.0
		'''

	cgmesProfile = ACDCConverter.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.SV.value, cgmesProfile.SSH.value, ],
						'CapabilityCurve': [cgmesProfile.EQ.value, ],
						'maxModulationIndex': [cgmesProfile.EQ.value, ],
						'maxValveCurrent': [cgmesProfile.EQ.value, ],
						'delta': [cgmesProfile.SV.value, ],
						'uf': [cgmesProfile.SV.value, ],
						'droop': [cgmesProfile.SSH.value, ],
						'droopCompensation': [cgmesProfile.SSH.value, ],
						'pPccControl': [cgmesProfile.SSH.value, ],
						'qPccControl': [cgmesProfile.SSH.value, ],
						'qShare': [cgmesProfile.SSH.value, ],
						'targetQpcc': [cgmesProfile.SSH.value, ],
						'targetUpcc': [cgmesProfile.SSH.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ACDCConverter: \n' + ACDCConverter.__doc__ 

	def __init__(self, CapabilityCurve = None, maxModulationIndex = 0.0, maxValveCurrent = 0.0, delta = 0.0, uf = 0.0, droop = 0.0, droopCompensation = 0.0, pPccControl = None, qPccControl = None, qShare = 0.0, targetQpcc = 0.0, targetUpcc = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.CapabilityCurve = CapabilityCurve
		self.maxModulationIndex = maxModulationIndex
		self.maxValveCurrent = maxValveCurrent
		self.delta = delta
		self.uf = uf
		self.droop = droop
		self.droopCompensation = droopCompensation
		self.pPccControl = pPccControl
		self.qPccControl = qPccControl
		self.qShare = qShare
		self.targetQpcc = targetQpcc
		self.targetUpcc = targetUpcc
		
	def __str__(self):
		str = 'class=VsConverter\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
