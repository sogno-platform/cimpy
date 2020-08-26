from cimpy.output.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class Pss5(PowerSystemStabilizerDynamics):
	'''
	Italian PSS - Detailed PSS.

	:kpe: Electric power input gain (K).  Typical Value = 0.3. Default: 
	:kf: Frequency/shaft speed input gain (K).  Typical Value = 5. Default: 
	:isfreq: Selector for Frequency/shaft speed input (IsFreq). true = speed false = frequency. Typical Value = true. Default: 
	:kpss: PSS gain (K).  Typical Value = 1. Default: 
	:ctw2: Selector for Second washout enabling (C). true = second washout filter is bypassed false = second washout filter in use. Typical Value = true. Default: 
	:tw1: First WashOut (T).  Typical Value = 3.5. Default: 
	:tw2: Second WashOut (T).  Typical Value = 0. Default: 
	:tl1: Lead/lag time constant (T).  Typical Value = 0. Default: 
	:tl2: Lead/lag time constant (T).  Typical Value = 0. Default: 
	:tl3: Lead/lag time constant (T).  Typical Value = 0. Default: 
	:tl4: Lead/lag time constant (T).  Typical Value = 0. Default: 
	:vsmn: Stabilizer output max limit (V).  Typical Value = -0.1. Default: 
	:vsmx: Stabilizer output min limit (V).  Typical Value = 0.1. Default: 
	:tpe: Electric power filter time constant (T).  Typical Value = 0.05. Default: 
	:pmm: Minimum power PSS enabling (P).  Typical Value = 0.25. Default: 
	:deadband: Stabilizer output dead band (DeadBand).  Typical Value = 0. Default: 
	:vadat:  Default: 
		'''

	cgmesProfile = PowerSystemStabilizerDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'kpe': [cgmesProfile.DY.value, ],
						'kf': [cgmesProfile.DY.value, ],
						'isfreq': [cgmesProfile.DY.value, ],
						'kpss': [cgmesProfile.DY.value, ],
						'ctw2': [cgmesProfile.DY.value, ],
						'tw1': [cgmesProfile.DY.value, ],
						'tw2': [cgmesProfile.DY.value, ],
						'tl1': [cgmesProfile.DY.value, ],
						'tl2': [cgmesProfile.DY.value, ],
						'tl3': [cgmesProfile.DY.value, ],
						'tl4': [cgmesProfile.DY.value, ],
						'vsmn': [cgmesProfile.DY.value, ],
						'vsmx': [cgmesProfile.DY.value, ],
						'tpe': [cgmesProfile.DY.value, ],
						'pmm': [cgmesProfile.DY.value, ],
						'deadband': [cgmesProfile.DY.value, ],
						'vadat': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemStabilizerDynamics: \n' + PowerSystemStabilizerDynamics.__doc__ 

	def __init__(self, kpe = , kf = , isfreq = , kpss = , ctw2 = , tw1 = , tw2 = , tl1 = , tl2 = , tl3 = , tl4 = , vsmn = , vsmx = , tpe = , pmm = , deadband = , vadat = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.kpe = kpe
		self.kf = kf
		self.isfreq = isfreq
		self.kpss = kpss
		self.ctw2 = ctw2
		self.tw1 = tw1
		self.tw2 = tw2
		self.tl1 = tl1
		self.tl2 = tl2
		self.tl3 = tl3
		self.tl4 = tl4
		self.vsmn = vsmn
		self.vsmx = vsmx
		self.tpe = tpe
		self.pmm = pmm
		self.deadband = deadband
		self.vadat = vadat
		
	def __str__(self):
		str = 'class=Pss5\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
