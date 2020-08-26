from cimpy.cgmes_v2_4_15.ACDCConverter import ACDCConverter


class VsConverter(ACDCConverter):
	'''
	DC side of the voltage source converter (VSC).

	:CapabilityCurve: All converters with this capability curve. Default: 
	:maxModulationIndex: The max quotient between the AC converter voltage (Uc) and DC voltage (Ud). A factor typically less than 1. VSC configuration data used in power flow. Default: 
	:maxValveCurrent: The maximum current through a valve. This current limit is the basis for calculating the capability diagram. VSC  configuration data. Default: 
	:droop: Droop constant; pu value is obtained as D [kV^2 / MW] x Sb / Ubdc^2. Default: 
	:droopCompensation: Compensation (resistance) constant. Used to compensate for voltage drop when controlling voltage at a distant bus. Default: 
	:pPccControl: Kind of control of real power and/or DC voltage. Default: 
	:qPccControl:  Default: 
	:qShare: Reactive power sharing factor among parallel converters on Uac control. Default: 
	:targetQpcc: Reactive power injection target in AC grid, at point of common coupling. Default: 
	:targetUpcc: Voltage target in AC grid, at point of common coupling. Default: 
	:delta: Angle between uf and uc. Converter state variable used in power flow. Default: 
	:uf: Filter bus voltage. Converter state variable, result from power flow. Default: 
		'''

	cgmesProfile = ACDCConverter.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.SSH.value, cgmesProfile.SV.value, ],
						'CapabilityCurve': [cgmesProfile.EQ.value, ],
						'maxModulationIndex': [cgmesProfile.EQ.value, ],
						'maxValveCurrent': [cgmesProfile.EQ.value, ],
						'droop': [cgmesProfile.SSH.value, ],
						'droopCompensation': [cgmesProfile.SSH.value, ],
						'pPccControl': [cgmesProfile.SSH.value, ],
						'qPccControl': [cgmesProfile.SSH.value, ],
						'qShare': [cgmesProfile.SSH.value, ],
						'targetQpcc': [cgmesProfile.SSH.value, ],
						'targetUpcc': [cgmesProfile.SSH.value, ],
						'delta': [cgmesProfile.SV.value, ],
						'uf': [cgmesProfile.SV.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ACDCConverter: \n' + ACDCConverter.__doc__ 

	def __init__(self, CapabilityCurve = , maxModulationIndex = , maxValveCurrent = , droop = , droopCompensation = , pPccControl = , qPccControl = , qShare = , targetQpcc = , targetUpcc = , delta = , uf = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.CapabilityCurve = CapabilityCurve
		self.maxModulationIndex = maxModulationIndex
		self.maxValveCurrent = maxValveCurrent
		self.droop = droop
		self.droopCompensation = droopCompensation
		self.pPccControl = pPccControl
		self.qPccControl = qPccControl
		self.qShare = qShare
		self.targetQpcc = targetQpcc
		self.targetUpcc = targetUpcc
		self.delta = delta
		self.uf = uf
		
	def __str__(self):
		str = 'class=VsConverter\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
