from cimpy.cgmes_v2_4_15.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEST6B(ExcitationSystemDynamics):
	'''
	The class represents IEEE Std 421.5-2005 type ST6B model. This model consists of a PI voltage regulator with an inner loop field voltage regulator and pre-control. The field voltage regulator implements a proportional control. The pre-control and the delay in the feedback circuit increase the dynamic response.  Reference: IEEE Standard 421.5-2005 Section 7.6.

	:ilr: Exciter output current limit reference (I).  Typical Value = 4.164. Default: 
	:kci: Exciter output current limit adjustment (K).  Typical Value = 1.0577. Default: 
	:kff: Pre-control gain constant of the inner loop field regulator (K). Typical Value = 1. Default: 
	:kg: Feedback gain constant of the inner loop field regulator (K).  Typical Value = 1. Default: 
	:kia: Voltage regulator integral gain (K).  Typical Value = 45.094. Default: 
	:klr: Exciter output current limiter gain (K).  Typical Value = 17.33. Default: 
	:km: Forward gain constant of the inner loop field regulator (K).  Typical Value = 1. Default: 
	:kpa: Voltage regulator proportional gain (K).  Typical Value = 18.038. Default: 
	:oelin: OEL input selector (OELin). Typical Value = noOELinput. Default: 
	:tg: Feedback time constant of inner loop field voltage regulator (T). Typical Value = 0.02. Default: 
	:vamax: Maximum voltage regulator output (V).  Typical Value = 4.81. Default: 
	:vamin: Minimum voltage regulator output (V).  Typical Value = -3.85. Default: 
	:vrmax: Maximum voltage regulator output (V).  Typical Value = 4.81. Default: 
	:vrmin: Minimum voltage regulator output (V).  Typical Value = -3.85. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'ilr': [cgmesProfile.DY.value, ],
						'kci': [cgmesProfile.DY.value, ],
						'kff': [cgmesProfile.DY.value, ],
						'kg': [cgmesProfile.DY.value, ],
						'kia': [cgmesProfile.DY.value, ],
						'klr': [cgmesProfile.DY.value, ],
						'km': [cgmesProfile.DY.value, ],
						'kpa': [cgmesProfile.DY.value, ],
						'oelin': [cgmesProfile.DY.value, ],
						'tg': [cgmesProfile.DY.value, ],
						'vamax': [cgmesProfile.DY.value, ],
						'vamin': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ilr = , kci = , kff = , kg = , kia = , klr = , km = , kpa = , oelin = , tg = , vamax = , vamin = , vrmax = , vrmin = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ilr = ilr
		self.kci = kci
		self.kff = kff
		self.kg = kg
		self.kia = kia
		self.klr = klr
		self.km = km
		self.kpa = kpa
		self.oelin = oelin
		self.tg = tg
		self.vamax = vamax
		self.vamin = vamin
		self.vrmax = vrmax
		self.vrmin = vrmin
		
	def __str__(self):
		str = 'class=ExcIEEEST6B\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
