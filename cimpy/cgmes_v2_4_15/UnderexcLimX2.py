from cimpy.cgmes_v2_4_15.UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics


class UnderexcLimX2(UnderexcitationLimiterDynamics):
	'''
	

	:kf2: Differential gain (Kf2). Default: 0.0
	:tf2: Differential time constant (Tf2) (>0). Default: 0.0
	:km: Minimum excitation limit gain (Km). Default: 0.0
	:tm: Minimum excitation limit time constant (Tm). Default: 0.0
	:melmax: Minimum excitation limit value (MELMAX). Default: 0.0
	:qo: Excitation center setting (Qo). Default: 0.0
	:r: Excitation radius (R). Default: 0.0
		'''

	cgmesProfile = UnderexcitationLimiterDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'kf2': [cgmesProfile.DY.value, ],
						'tf2': [cgmesProfile.DY.value, ],
						'km': [cgmesProfile.DY.value, ],
						'tm': [cgmesProfile.DY.value, ],
						'melmax': [cgmesProfile.DY.value, ],
						'qo': [cgmesProfile.DY.value, ],
						'r': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class UnderexcitationLimiterDynamics: \n' + UnderexcitationLimiterDynamics.__doc__ 

	def __init__(self, kf2 = 0.0, tf2 = 0.0, km = 0.0, tm = 0.0, melmax = 0.0, qo = 0.0, r = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.kf2 = kf2
		self.tf2 = tf2
		self.km = km
		self.tm = tm
		self.melmax = melmax
		self.qo = qo
		self.r = r
		
	def __str__(self):
		str = 'class=UnderexcLimX2\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
