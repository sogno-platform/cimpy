from cimpy.output.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEAC1A(ExcitationSystemDynamics):
	'''
	The class represents IEEE Std 421.5-2005 type AC1A model. The model represents the field-controlled alternator-rectifier excitation systems designated Type AC1A. These excitation systems consist of an alternator main exciter with non-controlled rectifiers.  Reference: IEEE Standard 421.5-2005 Section 6.1.

	:tb: Voltage regulator time constant (T).  Typical Value = 0. Default: 
	:tc: Voltage regulator time constant (T).  Typical Value = 0. Default: 
	:ka: Voltage regulator gain (K).  Typical Value = 400. Default: 
	:ta: Voltage regulator time constant (T).  Typical Value = 0.02. Default: 
	:vamax: Maximum voltage regulator output (V).  Typical Value = 14.5. Default: 
	:vamin: Minimum voltage regulator output (V).  Typical Value = -14.5. Default: 
	:te: Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 0.8. Default: 
	:kf: Excitation control system stabilizer gains (K).  Typical Value = 0.03. Default: 
	:tf: Excitation control system stabilizer time constant (T).  Typical Value = 1. Default: 
	:kc: Rectifier loading factor proportional to commutating reactance (K).  Typical Value = 0.2. Default: 
	:kd: Demagnetizing factor, a function of exciter alternator reactances (K).  Typical Value = 0.38. Default: 
	:ke: Exciter constant related to self-excited field (K).  Typical Value = 1. Default: 
	:ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (V).  Typical Value = 4.18. Default: 
	:seve1: Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 0.1. Default: 
	:ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (V).  Typical Value = 3.14. Default: 
	:seve2: Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 0.03. Default: 
	:vrmax: Maximum voltage regulator outputs (V).  Typical Value = 6.03. Default: 
	:vrmin: Minimum voltage regulator outputs (V).  Typical Value = -5.43. Default: 
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
						'kf': [cgmesProfile.DY.value, ],
						'tf': [cgmesProfile.DY.value, ],
						'kc': [cgmesProfile.DY.value, ],
						'kd': [cgmesProfile.DY.value, ],
						'ke': [cgmesProfile.DY.value, ],
						've1': [cgmesProfile.DY.value, ],
						'seve1': [cgmesProfile.DY.value, ],
						've2': [cgmesProfile.DY.value, ],
						'seve2': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, tb = , tc = , ka = , ta = , vamax = , vamin = , te = , kf = , tf = , kc = , kd = , ke = , ve1 = , seve1 = , ve2 = , seve2 = , vrmax = , vrmin = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.tb = tb
		self.tc = tc
		self.ka = ka
		self.ta = ta
		self.vamax = vamax
		self.vamin = vamin
		self.te = te
		self.kf = kf
		self.tf = tf
		self.kc = kc
		self.kd = kd
		self.ke = ke
		self.ve1 = ve1
		self.seve1 = seve1
		self.ve2 = ve2
		self.seve2 = seve2
		self.vrmax = vrmax
		self.vrmin = vrmin
		
	def __str__(self):
		str = 'class=ExcIEEEAC1A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
