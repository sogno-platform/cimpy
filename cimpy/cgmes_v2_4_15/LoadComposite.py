from cimpy.output.LoadDynamics import LoadDynamics


class LoadComposite(LoadDynamics):
	'''
	This models combines static load and induction motor load effects. The dynamics of the motor are simplified by linearizing the induction machine equations.

	:epvs: Active load-voltage dependence index (static) (Epvs).  Typical Value = 0.7. Default: 
	:epfs: Active load-frequency dependence index (static) (Epfs).  Typical Value = 1.5. Default: 
	:eqvs: Reactive load-voltage dependence index (static) (Eqvs).  Typical Value = 2. Default: 
	:eqfs: Reactive load-frequency dependence index (static) (Eqfs).  Typical Value = 0. Default: 
	:epvd: Active load-voltage dependence index (dynamic) (Epvd).  Typical Value = 0.7. Default: 
	:epfd: Active load-frequency dependence index (dynamic) (Epfd).  Typical Value = 1.5. Default: 
	:eqvd: Reactive load-voltage dependence index (dynamic) (Eqvd).  Typical Value = 2. Default: 
	:eqfd: Reactive load-frequency dependence index (dynamic) (Eqfd).  Typical Value = 0. Default: 
	:lfrac: Loading factor - ratio of initial P to motor MVA base (Lfrac).  Typical Value = 0.8. Default: 
	:h: Inertia constant (H).  Typical Value = 2.5. Default: 
	:pfrac: Fraction of constant-power load to be represented by this motor model (Pfrac) (>=0.0 and <=1.0).  Typical Value = 0.5. Default: 
		'''

	cgmesProfile = LoadDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'epvs': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'epfs': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'eqvs': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'eqfs': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'epvd': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'epfd': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'eqvd': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'eqfd': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'lfrac': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'h': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'pfrac': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class LoadDynamics: \n' + LoadDynamics.__doc__ 

	def __init__(self, epvs = , epfs = , eqvs = , eqfs = , epvd = , epfd = , eqvd = , eqfd = , lfrac = , h = , pfrac = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.epvs = epvs
		self.epfs = epfs
		self.eqvs = eqvs
		self.eqfs = eqfs
		self.epvd = epvd
		self.epfd = epfd
		self.eqvd = eqvd
		self.eqfd = eqfd
		self.lfrac = lfrac
		self.h = h
		self.pfrac = pfrac
		
	def __str__(self):
		str = 'class=LoadComposite\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
