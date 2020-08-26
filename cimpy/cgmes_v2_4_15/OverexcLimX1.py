from cimpy.cgmes_v2_4_15.OverexcitationLimiterDynamics import OverexcitationLimiterDynamics


class OverexcLimX1(OverexcitationLimiterDynamics):
	'''
	Field voltage over excitation limiter.

	:efdrated: Rated field voltage (EFD).  Typical Value = 1.05. Default: 
	:efd1: Low voltage point on the inverse time characteristic (EFD).  Typical Value = 1.1. Default: 
	:t1: Time to trip the exciter at the low voltage point on the inverse time characteristic (TIME).  Typical Value = 120. Default: 
	:efd2: Mid voltage point on the inverse time characteristic (EFD).  Typical Value = 1.2. Default: 
	:t2: Time to trip the exciter at the mid voltage point on the inverse time characteristic (TIME).  Typical Value = 40. Default: 
	:efd3: High voltage point on the inverse time characteristic (EFD).  Typical Value = 1.5. Default: 
	:t3: Time to trip the exciter at the high voltage point on the inverse time characteristic (TIME).  Typical Value = 15. Default: 
	:efddes: Desired field voltage (EFD).  Typical Value = 0.9. Default: 
	:kmx: Gain (K).  Typical Value = 0.01. Default: 
	:vlow: Low voltage limit (V) (>0). Default: 
		'''

	cgmesProfile = OverexcitationLimiterDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'efdrated': [cgmesProfile.DY.value, ],
						'efd1': [cgmesProfile.DY.value, ],
						't1': [cgmesProfile.DY.value, ],
						'efd2': [cgmesProfile.DY.value, ],
						't2': [cgmesProfile.DY.value, ],
						'efd3': [cgmesProfile.DY.value, ],
						't3': [cgmesProfile.DY.value, ],
						'efddes': [cgmesProfile.DY.value, ],
						'kmx': [cgmesProfile.DY.value, ],
						'vlow': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class OverexcitationLimiterDynamics: \n' + OverexcitationLimiterDynamics.__doc__ 

	def __init__(self, efdrated = , efd1 = , t1 = , efd2 = , t2 = , efd3 = , t3 = , efddes = , kmx = , vlow = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.efdrated = efdrated
		self.efd1 = efd1
		self.t1 = t1
		self.efd2 = efd2
		self.t2 = t2
		self.efd3 = efd3
		self.t3 = t3
		self.efddes = efddes
		self.kmx = kmx
		self.vlow = vlow
		
	def __str__(self):
		str = 'class=OverexcLimX1\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
