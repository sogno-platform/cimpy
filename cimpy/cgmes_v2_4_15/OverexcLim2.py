from cimpy.cgmes_v2_4_15_flat.OverexcitationLimiterDynamics import OverexcitationLimiterDynamics


class OverexcLim2(OverexcitationLimiterDynamics):
	'''
	Different from LimIEEEOEL, LimOEL2 has a fixed pickup threshold and reduces the excitation set-point by mean of non-windup integral regulator. Irated is the rated machine excitation current (calculated from nameplate conditions: V, P, CosPhi).

	:koi: Gain Over excitation limiter (K).  Typical Value = 0.1. Default: 0.0
	:voimax: Maximum error signal (V).  Typical Value = 0. Default: 0.0
	:voimin: Minimum error signal (V).  Typical Value = -9999. Default: 0.0
	:ifdlim: Limit value of rated field current (I).  Typical Value = 1.05. Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'koi': [cgmesProfile.DY.value, ],
						'voimax': [cgmesProfile.DY.value, ],
						'voimin': [cgmesProfile.DY.value, ],
						'ifdlim': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class OverexcitationLimiterDynamics: \n' + OverexcitationLimiterDynamics.__doc__ 

	def __init__(self, koi = 0.0, voimax = 0.0, voimin = 0.0, ifdlim = 0.0,  *args, **kw_args):
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
