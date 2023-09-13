from .ACDCConverter import ACDCConverter


class CsConverter(ACDCConverter):
	'''
	DC side of the current source converter (CSC). The firing angle controls the dc voltage at the converter, both for rectifier and inverter. The difference between the dc voltages of the rectifier and inverter determines the dc current. The extinction angle is used to limit the dc voltage at the inverter, if needed, and is not used in active power control. The firing angle, transformer tap position and number of connected filters are the primary means to control a current source dc line. Higher level controls are built on top, e.g. dc voltage, dc current and active power. From a steady state perspective it is sufficient to specify the wanted active power transfer (ACDCConverter.targetPpcc) and the control functions will set the dc voltage, dc current, firing angle, transformer tap position and number of connected filters to meet this. Therefore attributes targetAlpha and targetGamma are not applicable in this case. The reactive power consumed by the converter is a function of the firing angle, transformer tap position and number of connected filter, which can be approximated with half of the active power. The losses is a function of the dc voltage and dc current. The attributes minAlpha and maxAlpha define the range of firing angles for rectifier operation between which no discrete tap changer action takes place. The range is typically 10-18 degrees. The attributes minGamma and maxGamma define the range of extinction angles for inverter operation between which no discrete tap changer action takes place. The range is typically 17-20 degrees.

	:CSCDynamics: Current source converter dynamics model used to describe dynamic behaviour of this converter. Default: None
	:operatingMode: Indicates whether the DC pole is operating as an inverter or as a rectifier. It is converter`s control variable used in power flow. Default: None
	:pPccControl: Kind of active power control. Default: None
	:targetAlpha: Target firing angle. It is converter`s control variable used in power flow. It is only applicable for rectifier if continuous tap changer control is used. Allowed values are within the range minAlpha&lt;=targetAlpha&lt;=maxAlpha. The attribute shall be a positive value. Default: 0.0
	:targetGamma: Target extinction angle. It is converter`s control variable used in power flow. It is only applicable for inverter if continuous tap changer control is used. Allowed values are within the range minGamma&lt;=targetGamma&lt;=maxGamma. The attribute shall be a positive value. Default: 0.0
	:targetIdc: DC current target value. It is converter`s control variable used in power flow. The attribute shall be a positive value. Default: 0.0
	:maxAlpha: Maximum firing angle. It is converter`s configuration data used in power flow. The attribute shall be a positive value. Default: 0.0
	:maxGamma: Maximum extinction angle. It is converter`s configuration data used in power flow. The attribute shall be a positive value. Default: 0.0
	:maxIdc: The maximum direct current (Id) on the DC side at which the converter should operate. It is converter`s configuration data use in power flow. The attribute shall be a positive value. Default: 0.0
	:minAlpha: Minimum firing angle. It is converter`s configuration data used in power flow. The attribute shall be a positive value. Default: 0.0
	:minGamma: Minimum extinction angle. It is converter`s configuration data used in power flow. The attribute shall be a positive value. Default: 0.0
	:minIdc: The minimum direct current (Id) on the DC side at which the converter should operate. It is converter`s configuration data used in power flow. The attribute shall be a positive value. Default: 0.0
	:ratedIdc: Rated converter DC current, also called IdN. The attribute shall be a positive value. It is converter`s configuration data used in power flow. Default: 0.0
	:alpha: Firing angle that determines the dc voltage at the converter dc terminal. Typical value between 10 degrees and 18 degrees for a rectifier. It is converter`s state variable, result from power flow. The attribute shall be a positive value. Default: 0.0
	:gamma: Extinction angle. It is used to limit the dc voltage at the inverter if needed. Typical value between 17 degrees and 20 degrees for an inverter. It is converter`s state variable, result from power flow. The attribute shall be a positive value. Default: 0.0
		'''

	cgmesProfile = ACDCConverter.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, cgmesProfile.SSH.value, cgmesProfile.EQ.value, cgmesProfile.SV.value, ],
						'CSCDynamics': [cgmesProfile.DY.value, ],
						'operatingMode': [cgmesProfile.SSH.value, ],
						'pPccControl': [cgmesProfile.SSH.value, ],
						'targetAlpha': [cgmesProfile.SSH.value, ],
						'targetGamma': [cgmesProfile.SSH.value, ],
						'targetIdc': [cgmesProfile.SSH.value, ],
						'maxAlpha': [cgmesProfile.EQ.value, ],
						'maxGamma': [cgmesProfile.EQ.value, ],
						'maxIdc': [cgmesProfile.EQ.value, ],
						'minAlpha': [cgmesProfile.EQ.value, ],
						'minGamma': [cgmesProfile.EQ.value, ],
						'minIdc': [cgmesProfile.EQ.value, ],
						'ratedIdc': [cgmesProfile.EQ.value, ],
						'alpha': [cgmesProfile.SV.value, ],
						'gamma': [cgmesProfile.SV.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ACDCConverter: \n' + ACDCConverter.__doc__ 

	def __init__(self, CSCDynamics = None, operatingMode = None, pPccControl = None, targetAlpha = 0.0, targetGamma = 0.0, targetIdc = 0.0, maxAlpha = 0.0, maxGamma = 0.0, maxIdc = 0.0, minAlpha = 0.0, minGamma = 0.0, minIdc = 0.0, ratedIdc = 0.0, alpha = 0.0, gamma = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.CSCDynamics = CSCDynamics
		self.operatingMode = operatingMode
		self.pPccControl = pPccControl
		self.targetAlpha = targetAlpha
		self.targetGamma = targetGamma
		self.targetIdc = targetIdc
		self.maxAlpha = maxAlpha
		self.maxGamma = maxGamma
		self.maxIdc = maxIdc
		self.minAlpha = minAlpha
		self.minGamma = minGamma
		self.minIdc = minIdc
		self.ratedIdc = ratedIdc
		self.alpha = alpha
		self.gamma = gamma
		
	def __str__(self):
		str = 'class=CsConverter\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
