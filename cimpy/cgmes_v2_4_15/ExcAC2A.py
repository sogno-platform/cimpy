from cimpy.output.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAC2A(ExcitationSystemDynamics):
	'''
	Modified IEEE AC2A alternator-supplied rectifier excitation system with different field current limit.

	:tb: Voltage regulator time constant (Tb).  Typical Value = 0. Default: 
	:tc: Voltage regulator time constant (T).  Typical Value = 0. Default: 
	:ka: Voltage regulator gain (Ka).  Typical Value = 400. Default: 
	:ta: Voltage regulator time constant (Ta).  Typical Value = 0.02. Default: 
	:vamax: Maximum voltage regulator output (V).  Typical Value = 8. Default: 
	:vamin: Minimum voltage regulator output (V).  Typical Value = -8. Default: 
	:kb: Second stage regulator gain (Kb) (>0).  Exciter field current controller gain.  Typical Value = 25. Default: 
	:kb1: Second stage regulator gain (Kb1). It is exciter field current controller gain used as alternative to Kb to represent a variant of the ExcAC2A model.  Typical Value = 25. Default: 
	:vrmax: Maximum voltage regulator outputs (Vrmax).  Typical Value = 105. Default: 
	:vrmin: Minimum voltage regulator outputs (Vrmin).  Typical Value = -95. Default: 
	:te: Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 0.6. Default: 
	:vfemax: Exciter field current limit reference (Vfemax).  Typical Value = 4.4. Default: 
	:kh: Exciter field current feedback gain (Kh).  Typical Value = 1. Default: 
	:kf: Excitation control system stabilizer gains (Kf).  Typical Value = 0.03. Default: 
	:kl: Exciter field current limiter gain (Kl).  Typical Value = 10. Default: 
	:vlr: Maximum exciter field current (Vlr).  Typical Value = 4.4. Default: 
	:kl1: Coefficient to allow different usage of the model (Kl1).  Typical Value = 1. Default: 
	:ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0. Default: 
	:tf: Excitation control system stabilizer time constant (Tf).  Typical Value = 1. Default: 
	:kc: Rectifier loading factor proportional to commutating reactance (Kc).  Typical Value = 0.28. Default: 
	:kd: Demagnetizing factor, a function of exciter alternator reactances (Kd).  Typical Value = 0.35. Default: 
	:ke: Exciter constant related to self-excited field (Ke).  Typical Value = 1. Default: 
	:ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve).  Typical Value = 4.4. Default: 
	:seve1: Exciter saturation function value at the corresponding exciter voltage, Ve, back of commutating reactance (Se[Ve]).  Typical Value = 0.037. Default: 
	:ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve).  Typical Value = 3.3. Default: 
	:seve2: Exciter saturation function value at the corresponding exciter voltage, Ve, back of commutating reactance (Se[Ve]).  Typical Value = 0.012. Default: 
	:hvgate: Indicates if HV gate is active (HVgate). true = gate is used false = gate is not used. Typical Value = true. Default: 
	:lvgate: Indicates if LV gate is active (LVgate). true = gate is used false = gate is not used. Typical Value = true. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'vamax': [cgmesProfile.DY.value, ],
						'vamin': [cgmesProfile.DY.value, ],
						'kb': [cgmesProfile.DY.value, ],
						'kb1': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'vfemax': [cgmesProfile.DY.value, ],
						'kh': [cgmesProfile.DY.value, ],
						'kf': [cgmesProfile.DY.value, ],
						'kl': [cgmesProfile.DY.value, ],
						'vlr': [cgmesProfile.DY.value, ],
						'kl1': [cgmesProfile.DY.value, ],
						'ks': [cgmesProfile.DY.value, ],
						'tf': [cgmesProfile.DY.value, ],
						'kc': [cgmesProfile.DY.value, ],
						'kd': [cgmesProfile.DY.value, ],
						'ke': [cgmesProfile.DY.value, ],
						've1': [cgmesProfile.DY.value, ],
						'seve1': [cgmesProfile.DY.value, ],
						've2': [cgmesProfile.DY.value, ],
						'seve2': [cgmesProfile.DY.value, ],
						'hvgate': [cgmesProfile.DY.value, ],
						'lvgate': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, tb = , tc = , ka = , ta = , vamax = , vamin = , kb = , kb1 = , vrmax = , vrmin = , te = , vfemax = , kh = , kf = , kl = , vlr = , kl1 = , ks = , tf = , kc = , kd = , ke = , ve1 = , seve1 = , ve2 = , seve2 = , hvgate = , lvgate = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.tb = tb
		self.tc = tc
		self.ka = ka
		self.ta = ta
		self.vamax = vamax
		self.vamin = vamin
		self.kb = kb
		self.kb1 = kb1
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.te = te
		self.vfemax = vfemax
		self.kh = kh
		self.kf = kf
		self.kl = kl
		self.vlr = vlr
		self.kl1 = kl1
		self.ks = ks
		self.tf = tf
		self.kc = kc
		self.kd = kd
		self.ke = ke
		self.ve1 = ve1
		self.seve1 = seve1
		self.ve2 = ve2
		self.seve2 = seve2
		self.hvgate = hvgate
		self.lvgate = lvgate
		
	def __str__(self):
		str = 'class=ExcAC2A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
