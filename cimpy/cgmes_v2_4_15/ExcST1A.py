from cimpy.cgmes_v2_4_15.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcST1A(ExcitationSystemDynamics):
	'''
	Modification of an old IEEE ST1A static excitation system without overexcitation limiter (OEL) and underexcitation limiter (UEL).

	:vimax: Maximum voltage regulator input limit (Vimax).  Typical Value = 999. Default: 0.0
	:vimin: Minimum voltage regulator input limit (Vimin).  Typical Value = -999. Default: 0.0
	:tc: Voltage regulator time constant (Tc).  Typical Value = 1. Default: 0.0
	:tb: Voltage regulator time constant (Tb).  Typical Value = 10. Default: 0.0
	:ka: Voltage regulator gain (Ka).  Typical Value = 190. Default: 0.0
	:ta: Voltage regulator time constant (Ta).  Typical Value = 0.02. Default: 0.0
	:vrmax: Maximum voltage regulator outputs (Vrmax).  Typical Value = 7.8. Default: 0.0
	:vrmin: Minimum voltage regulator outputs (Vrmin).  Typical Value = -6.7. Default: 0.0
	:kc: Rectifier loading factor proportional to commutating reactance (Kc). Typical Value = 0.05. Default: 0.0
	:kf: Excitation control system stabilizer gains (Kf).  Typical Value = 0. Default: 0.0
	:tf: Excitation control system stabilizer time constant (Tf).  Typical Value = 1. Default: 0.0
	:tc1: Voltage regulator time constant (Tc).  Typical Value = 0. Default: 0.0
	:tb1: Voltage regulator time constant (Tb).  Typical Value = 0. Default: 0.0
	:vamax: Maximum voltage regulator output (Vamax).  Typical Value = 999. Default: 0.0
	:vamin: Minimum voltage regulator output (Vamin).  Typical Value = -999. Default: 0.0
	:ilr: Exciter output current limit reference (Ilr).  Typical Value = 0. Default: 0.0
	:klr: Exciter output current limiter gain (Klr).  Typical Value = 0. Default: 0.0
	:xe: Excitation xfmr effective reactance (Xe).  Typical Value = 0.04. Default: 0.0
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

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, vimax = 0.0, vimin = 0.0, tc = 0.0, tb = 0.0, ka = 0.0, ta = 0.0, vrmax = 0.0, vrmin = 0.0, kc = 0.0, kf = 0.0, tf = 0.0, tc1 = 0.0, tb1 = 0.0, vamax = 0.0, vamin = 0.0, ilr = 0.0, klr = 0.0, xe = 0.0,  *args, **kw_args):
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
