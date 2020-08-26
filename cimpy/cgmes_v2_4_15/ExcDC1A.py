from cimpy.output.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcDC1A(ExcitationSystemDynamics):
	'''
	Modified IEEE DC1A direct current commutator exciter with speed input and without underexcitation limiters (UEL) inputs.

	:ka: Voltage regulator gain (Ka).  Typical Value = 46. Default: 
	:ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0. Default: 
	:ta: Voltage regulator time constant (Ta).  Typical Value = 0.06. Default: 
	:tb: Voltage regulator time constant (Tb).  Typical Value = 0. Default: 
	:tc: Voltage regulator time constant (Tc).  Typical Value = 0. Default: 
	:vrmax: Maximum voltage regulator output (Vrmax).  Typical Value = 1. Default: 
	:vrmin: Minimum voltage regulator output (Vrmin).  Typical Value = -0.9. Default: 
	:ke: Exciter constant related to self-excited field (Ke).  Typical Value = 0. Default: 
	:te: Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 0.46. Default: 
	:kf: Excitation control system stabilizer gain (Kf).  Typical Value = 0.1. Default: 
	:tf: Excitation control system stabilizer time constant (Tf).  Typical Value = 1. Default: 
	:efd1: Exciter voltage at which exciter saturation is defined (Efd1).  Typical Value = 3.1. Default: 
	:seefd1: Exciter saturation function value at the corresponding exciter voltage, Efd1 (Se[Eefd1]).  Typical Value = 0.33. Default: 
	:efd2: Exciter voltage at which exciter saturation is defined (Efd2).  Typical Value = 2.3. Default: 
	:seefd2: Exciter saturation function value at the corresponding exciter voltage, Efd1 (Se[Eefd1]).  Typical Value = 0.33. Default: 
	:exclim: (exclim). IEEE standard is ambiguous about lower limit on exciter output.  true = a lower limit of zero is applied to integrator output false = a lower limit of zero is not applied to integrator output. Typical Value = true. Default: 
	:efdmin: Minimum voltage exciter output limiter (Efdmin).  Typical Value = -99. Default: 
	:edfmax: Maximum voltage exciter output limiter (Efdmax).  Typical Value = 99. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ka': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ks': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ta': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tb': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ke': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'te': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kf': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tf': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'efd1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'seefd1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'efd2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'seefd2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'exclim': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'efdmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'edfmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ka = , ks = , ta = , tb = , tc = , vrmax = , vrmin = , ke = , te = , kf = , tf = , efd1 = , seefd1 = , efd2 = , seefd2 = , exclim = , efdmin = , edfmax = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ka = ka
		self.ks = ks
		self.ta = ta
		self.tb = tb
		self.tc = tc
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.ke = ke
		self.te = te
		self.kf = kf
		self.tf = tf
		self.efd1 = efd1
		self.seefd1 = seefd1
		self.efd2 = efd2
		self.seefd2 = seefd2
		self.exclim = exclim
		self.efdmin = efdmin
		self.edfmax = edfmax
		
	def __str__(self):
		str = 'class=ExcDC1A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
