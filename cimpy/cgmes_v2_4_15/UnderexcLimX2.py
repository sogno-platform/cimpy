from cimpy.output.UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics


class UnderexcLimX2(UnderexcitationLimiterDynamics):
	'''
	

	:kf2: Differential gain (Kf2). Default: 
	:tf2: Differential time constant (Tf2) (>0). Default: 
	:km: Minimum excitation limit gain (Km). Default: 
	:tm: Minimum excitation limit time constant (Tm). Default: 
	:melmax: Minimum excitation limit value (MELMAX). Default: 
	:qo: Excitation center setting (Qo). Default: 
	:r: Excitation radius (R). Default: 
		'''

	cgmesProfile = UnderexcitationLimiterDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kf2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tf2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'km': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tm': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'melmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'qo': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'r': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class UnderexcitationLimiterDynamics: \n' + UnderexcitationLimiterDynamics.__doc__ 

	def __init__(self, kf2 = , tf2 = , km = , tm = , melmax = , qo = , r = ,  *args, **kw_args):
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
