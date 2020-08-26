from cimpy.output.ACDCConverter import ACDCConverter


class CsConverter(ACDCConverter):
	'''
	DC side of the current source converter (CSC).

	:maxAlpha: Maximum firing angle. CSC configuration data used in power flow. Default: 
	:maxGamma: Maximum extinction angle. CSC configuration data used in power flow. Default: 
	:maxIdc: The maximum direct current (Id) on the DC side at which the converter should operate. Converter configuration data use in power flow. Default: 
	:minAlpha: Minimum firing angle. CSC configuration data used in power flow. Default: 
	:minGamma: Minimum extinction angle. CSC configuration data used in power flow. Default: 
	:minIdc: The minimum direct current (Id) on the DC side at which the converter should operate. CSC configuration data used in power flow. Default: 
	:ratedIdc: Rated converter DC current, also called IdN. Converter configuration data used in power flow. Default: 
	:operatingMode: Indicates whether the DC pole is operating as an inverter or as a rectifier. CSC control variable used in power flow. Default: 
	:pPccControl:  Default: 
	:targetAlpha: Target firing angle. CSC control variable used in power flow. Default: 
	:targetGamma: Target extinction angle. CSC  control variable used in power flow. Default: 
	:targetIdc: DC current target value. CSC control variable used in power flow. Default: 
	:alpha: Firing angle, typical value between 10 and 18 degrees for a rectifier. CSC state variable, result from power flow. Default: 
	:gamma: Extinction angle. CSC state variable, result from power flow. Default: 
		'''

	cgmesProfile = ACDCConverter.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.SSH.value, cgmesProfile.SV.value, ],
						'maxAlpha': [cgmesProfile.EQ.value, ],
						'maxGamma': [cgmesProfile.EQ.value, ],
						'maxIdc': [cgmesProfile.EQ.value, ],
						'minAlpha': [cgmesProfile.EQ.value, ],
						'minGamma': [cgmesProfile.EQ.value, ],
						'minIdc': [cgmesProfile.EQ.value, ],
						'ratedIdc': [cgmesProfile.EQ.value, ],
						'operatingMode': [cgmesProfile.SSH.value, ],
						'pPccControl': [cgmesProfile.SSH.value, ],
						'targetAlpha': [cgmesProfile.SSH.value, ],
						'targetGamma': [cgmesProfile.SSH.value, ],
						'targetIdc': [cgmesProfile.SSH.value, ],
						'alpha': [cgmesProfile.SV.value, ],
						'gamma': [cgmesProfile.SV.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ACDCConverter: \n' + ACDCConverter.__doc__ 

	def __init__(self, maxAlpha = , maxGamma = , maxIdc = , minAlpha = , minGamma = , minIdc = , ratedIdc = , operatingMode = , pPccControl = , targetAlpha = , targetGamma = , targetIdc = , alpha = , gamma = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.maxAlpha = maxAlpha
		self.maxGamma = maxGamma
		self.maxIdc = maxIdc
		self.minAlpha = minAlpha
		self.minGamma = minGamma
		self.minIdc = minIdc
		self.ratedIdc = ratedIdc
		self.operatingMode = operatingMode
		self.pPccControl = pPccControl
		self.targetAlpha = targetAlpha
		self.targetGamma = targetGamma
		self.targetIdc = targetIdc
		self.alpha = alpha
		self.gamma = gamma
		
	def __str__(self):
		str = 'class=CsConverter\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
