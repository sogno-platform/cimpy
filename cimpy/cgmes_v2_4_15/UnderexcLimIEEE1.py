from cimpy.output.UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics


class UnderexcLimIEEE1(UnderexcitationLimiterDynamics):
	'''
	The class represents the Type UEL1 model which has a circular limit boundary when plotted in terms of machine reactive power vs. real power output.  Reference: IEEE UEL1 421.5-2005 Section 10.1.

	:kur: UEL radius setting (K).  Typical Value = 1.95. Default: 
	:kuc: UEL center setting (K).  Typical Value = 1.38. Default: 
	:kuf: UEL excitation system stabilizer gain (K).  Typical Value = 3.3. Default: 
	:vurmax: UEL maximum limit for radius phasor magnitude (V).  Typical Value = 5.8. Default: 
	:vucmax: UEL maximum limit for operating point phasor magnitude (V).  Typical Value = 5.8. Default: 
	:kui: UEL integral gain (K).  Typical Value = 0. Default: 
	:kul: UEL proportional gain (K).  Typical Value = 100. Default: 
	:vuimax: UEL integrator output maximum limit (V). Default: 
	:vuimin: UEL integrator output minimum limit (V). Default: 
	:tu1: UEL lead time constant (T).  Typical Value = 0. Default: 
	:tu2: UEL lag time constant (T).  Typical Value = 0.05. Default: 
	:tu3: UEL lead time constant (T).  Typical Value = 0. Default: 
	:tu4: UEL lag time constant (T).  Typical Value = 0. Default: 
	:vulmax: UEL output maximum limit (V).  Typical Value = 18. Default: 
	:vulmin: UEL output minimum limit (V).  Typical Value = -18. Default: 
		'''

	cgmesProfile = UnderexcitationLimiterDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'kur': [cgmesProfile.DY.value, ],
						'kuc': [cgmesProfile.DY.value, ],
						'kuf': [cgmesProfile.DY.value, ],
						'vurmax': [cgmesProfile.DY.value, ],
						'vucmax': [cgmesProfile.DY.value, ],
						'kui': [cgmesProfile.DY.value, ],
						'kul': [cgmesProfile.DY.value, ],
						'vuimax': [cgmesProfile.DY.value, ],
						'vuimin': [cgmesProfile.DY.value, ],
						'tu1': [cgmesProfile.DY.value, ],
						'tu2': [cgmesProfile.DY.value, ],
						'tu3': [cgmesProfile.DY.value, ],
						'tu4': [cgmesProfile.DY.value, ],
						'vulmax': [cgmesProfile.DY.value, ],
						'vulmin': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class UnderexcitationLimiterDynamics: \n' + UnderexcitationLimiterDynamics.__doc__ 

	def __init__(self, kur = , kuc = , kuf = , vurmax = , vucmax = , kui = , kul = , vuimax = , vuimin = , tu1 = , tu2 = , tu3 = , tu4 = , vulmax = , vulmin = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.kur = kur
		self.kuc = kuc
		self.kuf = kuf
		self.vurmax = vurmax
		self.vucmax = vucmax
		self.kui = kui
		self.kul = kul
		self.vuimax = vuimax
		self.vuimin = vuimin
		self.tu1 = tu1
		self.tu2 = tu2
		self.tu3 = tu3
		self.tu4 = tu4
		self.vulmax = vulmax
		self.vulmin = vulmin
		
	def __str__(self):
		str = 'class=UnderexcLimIEEE1\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
