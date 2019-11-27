from cimpy.cgmes_v2_4_15.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAC3A(ExcitationSystemDynamics):
	'''
	Modified IEEE AC3A alternator-supplied rectifier excitation system with different field current limit.

	:tb: Voltage regulator time constant (Tb).  Typical Value = 0. Default: 0.0
	:tc: Voltage regulator time constant (T).  Typical Value = 0. Default: 0.0
	:ka: Voltage regulator gain (Ka).  Typical Value = 45.62. Default: 0.0
	:ta: Voltage regulator time constant (Ta).  Typical Value = 0.013. Default: 0.0
	:vamax: Maximum voltage regulator output (V).  Typical Value = 1. Default: 0.0
	:vamin: Minimum voltage regulator output (V).  Typical Value = -0.95. Default: 0.0
	:te: Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 1.17. Default: 0.0
	:vemin: Minimum exciter voltage output (Vemin).  Typical Value = 0.1. Default: 0.0
	:kr: Constant associated with regulator and alternator field power supply (Kr).  Typical Value =3.77. Default: 0.0
	:kf: Excitation control system stabilizer gains (Kf).  Typical Value = 0.143. Default: 0.0
	:tf: Excitation control system stabilizer time constant (Tf).  Typical Value = 1. Default: 0.0
	:kn: Excitation control system stabilizer gain (Kn).  Typical Value =0.05. Default: 0.0
	:efdn: Value of at which feedback gain changes (Efdn).  Typical Value = 2.36. Default: 0.0
	:kc: Rectifier loading factor proportional to commutating reactance (Kc).  Typical Value = 0.104. Default: 0.0
	:kd: Demagnetizing factor, a function of exciter alternator reactances (Kd).  Typical Value = 0.499. Default: 0.0
	:ke: Exciter constant related to self-excited field (Ke).  Typical Value = 1. Default: 0.0
	:klv: Gain used in the minimum field voltage limiter loop (Klv).  Typical Value = 0.194. Default: 0.0
	:kf1: Coefficient to allow different usage of the model (Kf1).  Typical Value = 1. Default: 0.0
	:kf2: Coefficient to allow different usage of the model (Kf2).  Typical Value = 0. Default: 0.0
	:ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0. Default: 0.0
	:vfemax: Exciter field current limit reference (Vfemax).  Typical Value = 16. Default: 0.0
	:ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1) equals Vemax (Ve1).  Typical Value = 6.24. Default: 0.0
	:seve1: Exciter saturation function value at the corresponding exciter voltage, Ve, back of commutating reactance (Se[Ve]).  Typical Value = 1.143. Default: 0.0
	:ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve).  Typical Value = 4.68. Default: 0.0
	:seve2: Exciter saturation function value at the corresponding exciter voltage, Ve, back of commutating reactance (Se[Ve]).  Typical Value = 0.1. Default: 0.0
	:vlv: Field voltage used in the minimum field voltage limiter loop (Vlv).  Typical Value = 0.79. Default: 0.0
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'vamax': [cgmesProfile.DY.value, ],
						'vamin': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'vemin': [cgmesProfile.DY.value, ],
						'kr': [cgmesProfile.DY.value, ],
						'kf': [cgmesProfile.DY.value, ],
						'tf': [cgmesProfile.DY.value, ],
						'kn': [cgmesProfile.DY.value, ],
						'efdn': [cgmesProfile.DY.value, ],
						'kc': [cgmesProfile.DY.value, ],
						'kd': [cgmesProfile.DY.value, ],
						'ke': [cgmesProfile.DY.value, ],
						'klv': [cgmesProfile.DY.value, ],
						'kf1': [cgmesProfile.DY.value, ],
						'kf2': [cgmesProfile.DY.value, ],
						'ks': [cgmesProfile.DY.value, ],
						'vfemax': [cgmesProfile.DY.value, ],
						've1': [cgmesProfile.DY.value, ],
						'seve1': [cgmesProfile.DY.value, ],
						've2': [cgmesProfile.DY.value, ],
						'seve2': [cgmesProfile.DY.value, ],
						'vlv': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, tb = 0.0, tc = 0.0, ka = 0.0, ta = 0.0, vamax = 0.0, vamin = 0.0, te = 0.0, vemin = 0.0, kr = 0.0, kf = 0.0, tf = 0.0, kn = 0.0, efdn = 0.0, kc = 0.0, kd = 0.0, ke = 0.0, klv = 0.0, kf1 = 0.0, kf2 = 0.0, ks = 0.0, vfemax = 0.0, ve1 = 0.0, seve1 = 0.0, ve2 = 0.0, seve2 = 0.0, vlv = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.tb = tb
		self.tc = tc
		self.ka = ka
		self.ta = ta
		self.vamax = vamax
		self.vamin = vamin
		self.te = te
		self.vemin = vemin
		self.kr = kr
		self.kf = kf
		self.tf = tf
		self.kn = kn
		self.efdn = efdn
		self.kc = kc
		self.kd = kd
		self.ke = ke
		self.klv = klv
		self.kf1 = kf1
		self.kf2 = kf2
		self.ks = ks
		self.vfemax = vfemax
		self.ve1 = ve1
		self.seve1 = seve1
		self.ve2 = ve2
		self.seve2 = seve2
		self.vlv = vlv
		
	def __str__(self):
		str = 'class=ExcAC3A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
