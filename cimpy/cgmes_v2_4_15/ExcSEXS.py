from cimpy.output.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcSEXS(ExcitationSystemDynamics):
	'''
	Simplified Excitation System Model.

	:tatb: Ta/Tb - gain reduction ratio of lag-lead element (TaTb).  Typical Value = 0.1. Default: 
	:tb: Denominator time constant of lag-lead block (Tb).  Typical Value = 10. Default: 
	:k: Gain (K) (>0).  Typical Value = 100. Default: 
	:te: Time constant of gain block (Te).  Typical Value = 0.05. Default: 
	:emin: Minimum field voltage output (Emin).  Typical Value = -5. Default: 
	:emax: Maximum field voltage output (Emax).  Typical Value = 5. Default: 
	:kc: PI controller gain (Kc).  Typical Value = 0.08. Default: 
	:tc: PI controller phase lead time constant (Tc).  Typical Value = 0. Default: 
	:efdmin: Field voltage clipping minimum limit (Efdmin).  Typical Value = -5. Default: 
	:efdmax: Field voltage clipping maximum limit (Efdmax).  Typical Value = 5. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tatb': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tb': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'te': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'emin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'emax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'efdmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'efdmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, tatb = , tb = , k = , te = , emin = , emax = , kc = , tc = , efdmin = , efdmax = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.tatb = tatb
		self.tb = tb
		self.k = k
		self.te = te
		self.emin = emin
		self.emax = emax
		self.kc = kc
		self.tc = tc
		self.efdmin = efdmin
		self.efdmax = efdmax
		
	def __str__(self):
		str = 'class=ExcSEXS\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
