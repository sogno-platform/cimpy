from cimpy.output.ExcitationSystemDynamics import ExcitationSystemDynamics


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

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vimax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vimin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tb': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ka': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ta': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kf': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tf': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tc1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tb1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vamax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vamin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ilr': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'klr': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'xe': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
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
