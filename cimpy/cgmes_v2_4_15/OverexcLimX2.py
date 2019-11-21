from cimpy.cgmes_v2_4_15_flat.OverexcitationLimiterDynamics import OverexcitationLimiterDynamics


class OverexcLimX2(OverexcitationLimiterDynamics):
	'''
	Field Voltage or Current overexcitation limiter designed to protect the generator field of an AC machine with automatic excitation control from overheating due to prolonged overexcitation.

	:m: (m). true = IFD limiting false = EFD limiting. Default: False
	:efdrated: Rated field voltage if m=F or field current if m=T (EFD).  Typical Value = 1.05. Default: 0.0
	:efd1: Low voltage or current point on the inverse time characteristic (EFD).  Typical Value = 1.1. Default: 0.0
	:t1: Time to trip the exciter at the low voltage or current point on the inverse time characteristic (TIME).  Typical Value = 120. Default: 0.0
	:efd2: Mid voltage or current point on the inverse time characteristic (EFD).  Typical Value = 1.2. Default: 0.0
	:t2: Time to trip the exciter at the mid voltage or current point on the inverse time characteristic (TIME).  Typical Value = 40. Default: 0.0
	:efd3: High voltage or current point on the inverse time characteristic (EFD).  Typical Value = 1.5. Default: 0.0
	:t3: Time to trip the exciter at the high voltage or current point on the inverse time characteristic (TIME).  Typical Value = 15. Default: 0.0
	:efddes: Desired field voltage if m=F or field current if m=T (EFD).  Typical Value = 1. Default: 0.0
	:kmx: Gain (K).  Typical Value = 0.002. Default: 0.0
	:vlow: Low voltage limit (V) (>0). Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'm': [cgmesProfile.DY.value, ],
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

	readInProfile = {}

	__doc__ += '\n Documentation of parent class OverexcitationLimiterDynamics: \n' + OverexcitationLimiterDynamics.__doc__ 

	def __init__(self, m = False, efdrated = 0.0, efd1 = 0.0, t1 = 0.0, efd2 = 0.0, t2 = 0.0, efd3 = 0.0, t3 = 0.0, efddes = 0.0, kmx = 0.0, vlow = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.m = m
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
		str = 'class=OverexcLimX2\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
