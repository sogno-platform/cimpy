from cimpy.cgmes_v2_4_15.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEAC2A(ExcitationSystemDynamics):
	'''
	The class represents IEEE Std 421.5-2005 type AC2A model. The model represents a high initial response field-controlled alternator-rectifier excitation system. The alternator main exciter is used with non-controlled rectifiers. The Type AC2A model is similar to that of Type AC1A except for the inclusion of exciter time constant compensation and exciter field current limiting elements.  Reference: IEEE Standard 421.5-2005 Section 6.2.

	:tb: Voltage regulator time constant (T).  Typical Value = 0. Default: 0.0
	:tc: Voltage regulator time constant (T).  Typical Value = 0. Default: 0.0
	:ka: Voltage regulator gain (K).  Typical Value = 400. Default: 0.0
	:ta: Voltage regulator time constant (T).  Typical Value = 0.02. Default: 0.0
	:vamax: Maximum voltage regulator output (V).  Typical Value = 8. Default: 0.0
	:vamin: Minimum voltage regulator output (V).  Typical Value = -8. Default: 0.0
	:kb: Second stage regulator gain (K).  Typical Value = 25. Default: 0.0
	:vrmax: Maximum voltage regulator outputs (V).  Typical Value = 105. Default: 0.0
	:vrmin: Minimum voltage regulator outputs (V).  Typical Value = -95. Default: 0.0
	:te: Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 0.6. Default: 0.0
	:vfemax: Exciter field current limit reference (V).  Typical Value = 4.4. Default: 0.0
	:kh: Exciter field current feedback gain (K).  Typical Value = 1. Default: 0.0
	:kf: Excitation control system stabilizer gains (K).  Typical Value = 0.03. Default: 0.0
	:tf: Excitation control system stabilizer time constant (T).  Typical Value = 1. Default: 0.0
	:kc: Rectifier loading factor proportional to commutating reactance (K).  Typical Value = 0.28. Default: 0.0
	:kd: Demagnetizing factor, a function of exciter alternator reactances (K).  Typical Value = 0.35. Default: 0.0
	:ke: Exciter constant related to self-excited field (K).  Typical Value = 1. Default: 0.0
	:ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (V).  Typical Value = 4.4. Default: 0.0
	:seve1: Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 0.037. Default: 0.0
	:ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (V).  Typical Value = 3.3. Default: 0.0
	:seve2: Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 0.012. Default: 0.0
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
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'vfemax': [cgmesProfile.DY.value, ],
						'kh': [cgmesProfile.DY.value, ],
						'kf': [cgmesProfile.DY.value, ],
						'tf': [cgmesProfile.DY.value, ],
						'kc': [cgmesProfile.DY.value, ],
						'kd': [cgmesProfile.DY.value, ],
						'ke': [cgmesProfile.DY.value, ],
						've1': [cgmesProfile.DY.value, ],
						'seve1': [cgmesProfile.DY.value, ],
						've2': [cgmesProfile.DY.value, ],
						'seve2': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, tb = 0.0, tc = 0.0, ka = 0.0, ta = 0.0, vamax = 0.0, vamin = 0.0, kb = 0.0, vrmax = 0.0, vrmin = 0.0, te = 0.0, vfemax = 0.0, kh = 0.0, kf = 0.0, tf = 0.0, kc = 0.0, kd = 0.0, ke = 0.0, ve1 = 0.0, seve1 = 0.0, ve2 = 0.0, seve2 = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.tb = tb
		self.tc = tc
		self.ka = ka
		self.ta = ta
		self.vamax = vamax
		self.vamin = vamin
		self.kb = kb
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.te = te
		self.vfemax = vfemax
		self.kh = kh
		self.kf = kf
		self.tf = tf
		self.kc = kc
		self.kd = kd
		self.ke = ke
		self.ve1 = ve1
		self.seve1 = seve1
		self.ve2 = ve2
		self.seve2 = seve2
		
	def __str__(self):
		str = 'class=ExcIEEEAC2A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
