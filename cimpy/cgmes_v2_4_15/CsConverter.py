from cimpy.cgmes_v2_4_15_flat.ACDCConverter import ACDCConverter


class CsConverter(ACDCConverter):
	'''
	DC side of the current source converter (CSC).

	:maxAlpha: Maximum firing angle. CSC configuration data used in power flow. Default: 0.0
	:maxGamma: Maximum extinction angle. CSC configuration data used in power flow. Default: 0.0
	:maxIdc: The maximum direct current (Id) on the DC side at which the converter should operate. Converter configuration data use in power flow. Default: 0.0
	:minAlpha: Minimum firing angle. CSC configuration data used in power flow. Default: 0.0
	:minGamma: Minimum extinction angle. CSC configuration data used in power flow. Default: 0.0
	:minIdc: The minimum direct current (Id) on the DC side at which the converter should operate. CSC configuration data used in power flow. Default: 0.0
	:ratedIdc: Rated converter DC current, also called IdN. Converter configuration data used in power flow. Default: 0.0
	:alpha: Firing angle, typical value between 10 and 18 degrees for a rectifier. CSC state variable, result from power flow. Default: 0.0
	:gamma: Extinction angle. CSC state variable, result from power flow. Default: 0.0
	:operatingMode: Indicates whether the DC pole is operating as an inverter or as a rectifier. CSC control variable used in power flow. Default: None
	:pPccControl:  Default: None
	:targetAlpha: Target firing angle. CSC control variable used in power flow. Default: 0.0
	:targetGamma: Target extinction angle. CSC  control variable used in power flow. Default: 0.0
	:targetIdc: DC current target value. CSC control variable used in power flow. Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.SV.value, cgmesProfile.SSH.value, ],
						'maxAlpha': [cgmesProfile.EQ.value, ],
						'maxGamma': [cgmesProfile.EQ.value, ],
						'maxIdc': [cgmesProfile.EQ.value, ],
						'minAlpha': [cgmesProfile.EQ.value, ],
						'minGamma': [cgmesProfile.EQ.value, ],
						'minIdc': [cgmesProfile.EQ.value, ],
						'ratedIdc': [cgmesProfile.EQ.value, ],
						'alpha': [cgmesProfile.SV.value, ],
						'gamma': [cgmesProfile.SV.value, ],
						'operatingMode': [cgmesProfile.SSH.value, ],
						'pPccControl': [cgmesProfile.SSH.value, ],
						'targetAlpha': [cgmesProfile.SSH.value, ],
						'targetGamma': [cgmesProfile.SSH.value, ],
						'targetIdc': [cgmesProfile.SSH.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ACDCConverter: \n' + ACDCConverter.__doc__ 

	def __init__(self, maxAlpha = 0.0, maxGamma = 0.0, maxIdc = 0.0, minAlpha = 0.0, minGamma = 0.0, minIdc = 0.0, ratedIdc = 0.0, alpha = 0.0, gamma = 0.0, operatingMode = None, pPccControl = None, targetAlpha = 0.0, targetGamma = 0.0, targetIdc = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.maxAlpha = maxAlpha
		self.maxGamma = maxGamma
		self.maxIdc = maxIdc
		self.minAlpha = minAlpha
		self.minGamma = minGamma
		self.minIdc = minIdc
		self.ratedIdc = ratedIdc
		self.alpha = alpha
		self.gamma = gamma
		self.operatingMode = operatingMode
		self.pPccControl = pPccControl
		self.targetAlpha = targetAlpha
		self.targetGamma = targetGamma
		self.targetIdc = targetIdc
		
	def __str__(self):
		str = 'class=CsConverter\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
