from .OverexcitationLimiterDynamics import OverexcitationLimiterDynamics


class OverexcLim2(OverexcitationLimiterDynamics):
	'''
	Different from LimIEEEOEL, LimOEL2 has a fixed pickup threshold and reduces the excitation set-point by means of a non-windup integral regulator. <i>Irated</i> is the rated machine excitation current (calculated from nameplate conditions: <i>V</i><i><sub>nom</sub></i>, <i>P</i><i><sub>nom</sub></i>, <i>CosPhi</i><i><sub>nom</sub></i>).

	:koi: Gain Over excitation limiter (<i>K</i><i><sub>OI</sub></i>).  Typical value = 0,1. Default: 0.0
	:voimax: Maximum error signal (<i>V</i><i><sub>OIMAX</sub></i>) (&gt; OverexcLim2.voimin).  Typical value = 0. Default: 0.0
	:voimin: Minimum error signal (<i>V</i><i><sub>OIMIN</sub></i>) (&lt; OverexcLim2.voimax).  Typical value = -9999. Default: 0.0
	:ifdlim: Limit value of rated field current (<i>I</i><i><sub>FDLIM</sub></i>).  Typical value = 1,05. Default: 0.0
		'''

	cgmesProfile = OverexcitationLimiterDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'koi': [cgmesProfile.DY.value, ],
						'voimax': [cgmesProfile.DY.value, ],
						'voimin': [cgmesProfile.DY.value, ],
						'ifdlim': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

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
