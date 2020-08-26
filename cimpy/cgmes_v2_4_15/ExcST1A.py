from cimpy.cgmes_v2_4_15.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcST1A(ExcitationSystemDynamics):
	'''
	Modification of an old IEEE ST1A static excitation system without overexcitation limiter (OEL) and underexcitation limiter (UEL).

	:vimax: Maximum voltage regulator input limit (Vimax).  Typical Value = 999. Default: 
	:vimin: Minimum voltage regulator input limit (Vimin).  Typical Value = -999. Default: 
	:tc: Voltage regulator time constant (Tc).  Typical Value = 1. Default: 
	:tb: Voltage regulator time constant (Tb).  Typical Value = 10. Default: 
	:ka: Voltage regulator gain (Ka).  Typical Value = 190. Default: 
	:ta: Voltage regulator time constant (Ta).  Typical Value = 0.02. Default: 
	:vrmax: Maximum voltage regulator outputs (Vrmax).  Typical Value = 7.8. Default: 
	:vrmin: Minimum voltage regulator outputs (Vrmin).  Typical Value = -6.7. Default: 
	:kc: Rectifier loading factor proportional to commutating reactance (Kc). Typical Value = 0.05. Default: 
	:kf: Excitation control system stabilizer gains (Kf).  Typical Value = 0. Default: 
	:tf: Excitation control system stabilizer time constant (Tf).  Typical Value = 1. Default: 
	:tc1: Voltage regulator time constant (Tc).  Typical Value = 0. Default: 
	:tb1: Voltage regulator time constant (Tb).  Typical Value = 0. Default: 
	:vamax: Maximum voltage regulator output (Vamax).  Typical Value = 999. Default: 
	:vamin: Minimum voltage regulator output (Vamin).  Typical Value = -999. Default: 
	:ilr: Exciter output current limit reference (Ilr).  Typical Value = 0. Default: 
	:klr: Exciter output current limiter gain (Klr).  Typical Value = 0. Default: 
	:xe: Excitation xfmr effective reactance (Xe).  Typical Value = 0.04. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'vimax': [cgmesProfile.DY.value, ],
						'vimin': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'kc': [cgmesProfile.DY.value, ],
						'kf': [cgmesProfile.DY.value, ],
						'tf': [cgmesProfile.DY.value, ],
						'tc1': [cgmesProfile.DY.value, ],
						'tb1': [cgmesProfile.DY.value, ],
						'vamax': [cgmesProfile.DY.value, ],
						'vamin': [cgmesProfile.DY.value, ],
						'ilr': [cgmesProfile.DY.value, ],
						'klr': [cgmesProfile.DY.value, ],
						'xe': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, vimax = , vimin = , tc = , tb = , ka = , ta = , vrmax = , vrmin = , kc = , kf = , tf = , tc1 = , tb1 = , vamax = , vamin = , ilr = , klr = , xe = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.vimax = vimax
		self.vimin = vimin
		self.tc = tc
		self.tb = tb
		self.ka = ka
		self.ta = ta
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.kc = kc
		self.kf = kf
		self.tf = tf
		self.tc1 = tc1
		self.tb1 = tb1
		self.vamax = vamax
		self.vamin = vamin
		self.ilr = ilr
		self.klr = klr
		self.xe = xe
		
	def __str__(self):
		str = 'class=ExcST1A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
