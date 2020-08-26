from cimpy.output.OverexcitationLimiterDynamics import OverexcitationLimiterDynamics


class OverexcLim2(OverexcitationLimiterDynamics):
	'''
	Different from LimIEEEOEL, LimOEL2 has a fixed pickup threshold and reduces the excitation set-point by mean of non-windup integral regulator. Irated is the rated machine excitation current (calculated from nameplate conditions: V, P, CosPhi).

	:koi: Gain Over excitation limiter (K).  Typical Value = 0.1. Default: 
	:voimax: Maximum error signal (V).  Typical Value = 0. Default: 
	:voimin: Minimum error signal (V).  Typical Value = -9999. Default: 
	:ifdlim: Limit value of rated field current (I).  Typical Value = 1.05. Default: 
		'''

	cgmesProfile = OverexcitationLimiterDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'koi': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'voimax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'voimin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ifdlim': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class OverexcitationLimiterDynamics: \n' + OverexcitationLimiterDynamics.__doc__ 

	def __init__(self, koi = , voimax = , voimin = , ifdlim = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.koi = koi
		self.voimax = voimax
		self.voimin = voimin
		self.ifdlim = ifdlim
		
	def __str__(self):
		str = 'class=OverexcLim2\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
