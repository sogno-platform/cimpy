from cimpy.output.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEAC7B(ExcitationSystemDynamics):
	'''
	The class represents IEEE Std 421.5-2005 type AC7B model. The model represents excitation systems which consist of an ac alternator with either stationary or rotating rectifiers to produce the dc field requirements. It is an upgrade to earlier ac excitation systems, which replace only the controls but retain the ac alternator and diode rectifier bridge.  Reference: IEEE Standard 421.5-2005 Section 6.7.  In the IEEE Standard 421.5 - 2005, the [1 / sT] block is shown as [1 / (1 + sT)], which is incorrect.

	:kpr: Voltage regulator proportional gain (K).  Typical Value = 4.24. Default: 
	:kir: Voltage regulator integral gain (K).  Typical Value = 4.24. Default: 
	:kdr: Voltage regulator derivative gain (K).  Typical Value = 0. Default: 
	:tdr: Lag time constant (T).  Typical Value = 0. Default: 
	:vrmax: Maximum voltage regulator output (V).  Typical Value = 5.79. Default: 
	:vrmin: Minimum voltage regulator output (V).  Typical Value = -5.79. Default: 
	:kpa: Voltage regulator proportional gain (K).  Typical Value = 65.36. Default: 
	:kia: Voltage regulator integral gain (K).  Typical Value = 59.69. Default: 
	:vamax: Maximum voltage regulator output (V).  Typical Value = 1. Default: 
	:vamin: Minimum voltage regulator output (V).  Typical Value = -0.95. Default: 
	:kp: Potential circuit gain coefficient (K).  Typical Value = 4.96. Default: 
	:kl: Exciter field voltage lower limit parameter (K).  Typical Value = 10. Default: 
	:te: Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 1.1. Default: 
	:vfemax: Exciter field current limit reference (V).  Typical Value = 6.9. Default: 
	:vemin: Minimum exciter voltage output (V).  Typical Value = 0. Default: 
	:ke: Exciter constant related to self-excited field (K).  Typical Value = 1. Default: 
	:kc: Rectifier loading factor proportional to commutating reactance (K). Typical Value = 0.18. Default: 
	:kd: Demagnetizing factor, a function of exciter alternator reactances (K).  Typical Value = 0.02. Default: 
	:kf1: Excitation control system stabilizer gain (K).  Typical Value = 0.212. Default: 
	:kf2: Excitation control system stabilizer gain (K).  Typical Value = 0. Default: 
	:kf3: Excitation control system stabilizer gain (K).  Typical Value = 0. Default: 
	:tf: Excitation control system stabilizer time constant (T).  Typical Value = 1. Default: 
	:ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (V) equals V (V).  Typical Value = 6.3. Default: 
	:seve1: Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 0.44. Default: 
	:ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (V).  Typical Value = 3.02. Default: 
	:seve2: Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 0.075. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kpr': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kir': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kdr': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tdr': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kpa': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kia': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vamax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vamin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kp': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kl': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'te': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vfemax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vemin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ke': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kd': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kf1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kf2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kf3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tf': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						've1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'seve1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						've2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'seve2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, kpr = , kir = , kdr = , tdr = , vrmax = , vrmin = , kpa = , kia = , vamax = , vamin = , kp = , kl = , te = , vfemax = , vemin = , ke = , kc = , kd = , kf1 = , kf2 = , kf3 = , tf = , ve1 = , seve1 = , ve2 = , seve2 = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.kpr = kpr
		self.kir = kir
		self.kdr = kdr
		self.tdr = tdr
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.kpa = kpa
		self.kia = kia
		self.vamax = vamax
		self.vamin = vamin
		self.kp = kp
		self.kl = kl
		self.te = te
		self.vfemax = vfemax
		self.vemin = vemin
		self.ke = ke
		self.kc = kc
		self.kd = kd
		self.kf1 = kf1
		self.kf2 = kf2
		self.kf3 = kf3
		self.tf = tf
		self.ve1 = ve1
		self.seve1 = seve1
		self.ve2 = ve2
		self.seve2 = seve2
		
	def __str__(self):
		str = 'class=ExcIEEEAC7B\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
