from cimpy.output.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcST2A(ExcitationSystemDynamics):
	'''
	Modified IEEE ST2A static excitation system - another lead-lag block added to match  the model defined by WECC.

	:ka: Voltage regulator gain (Ka).  Typical Value = 120. Default: 
	:ta: Voltage regulator time constant (Ta).  Typical Value = 0.15. Default: 
	:vrmax: Maximum voltage regulator outputs (Vrmax).  Typical Value = 1. Default: 
	:vrmin: Minimum voltage regulator outputs (Vrmin).  Typical Value = -1. Default: 
	:ke: Exciter constant related to self-excited field (Ke).  Typical Value = 1. Default: 
	:te: Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 0.5. Default: 
	:kf: Excitation control system stabilizer gains (Kf).  Typical Value = 0.05. Default: 
	:tf: Excitation control system stabilizer time constant (Tf).  Typical Value = 0.7. Default: 
	:kp: Potential circuit gain coefficient (Kp).  Typical Value = 4.88. Default: 
	:ki: Potential circuit gain coefficient (Ki).  Typical Value = 8. Default: 
	:kc: Rectifier loading factor proportional to commutating reactance (Kc).  Typical Value = 1.82. Default: 
	:efdmax: Maximum field voltage (Efdmax).  Typical Value = 99. Default: 
	:uelin: UEL input (UELin). true = HV gate false = add to error signal. Typical Value = false. Default: 
	:tb: Voltage regulator time constant (Tb).  Typical Value = 0. Default: 
	:tc: Voltage regulator time constant (Tc).  Typical Value = 0. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ka': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ta': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ke': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'te': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kf': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tf': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kp': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ki': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'efdmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'uelin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tb': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ka = , ta = , vrmax = , vrmin = , ke = , te = , kf = , tf = , kp = , ki = , kc = , efdmax = , uelin = , tb = , tc = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ka = ka
		self.ta = ta
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.ke = ke
		self.te = te
		self.kf = kf
		self.tf = tf
		self.kp = kp
		self.ki = ki
		self.kc = kc
		self.efdmax = efdmax
		self.uelin = uelin
		self.tb = tb
		self.tc = tc
		
	def __str__(self):
		str = 'class=ExcST2A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
