from cimpy.output.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovSteamFV3(TurbineGovernorDynamics):
	'''
	Simplified GovSteamIEEE1 Steam turbine governor model with Prmax limit and fast valving.

	:mwbase: Base for power values (MWbase) (>0).  Unit = MW. Default: 
	:k: Governor gain, (reciprocal of droop) (K).  Typical Value = 20. Default: 
	:t1: Governor lead time constant (T1).  Typical Value = 0. Default: 
	:t2: Governor lag time constant (T2).  Typical Value = 0. Default: 
	:t3: Valve positioner time constant (T3).  Typical Value = 0. Default: 
	:uo: Maximum valve opening velocity (Uo).  Unit = PU/sec.  Typical Value = 0.1. Default: 
	:uc: Maximum valve closing velocity (Uc).  Unit = PU/sec.  Typical Value = -1. Default: 
	:pmax: Maximum valve opening, PU of MWbase (Pmax).  Typical Value = 1. Default: 
	:pmin: Minimum valve opening, PU of MWbase (Pmin).  Typical Value = 0. Default: 
	:t4: Inlet piping/steam bowl time constant (T4).  Typical Value = 0.2. Default: 
	:k1: Fraction of turbine power developed after first boiler pass (K1).  Typical Value = 0.2. Default: 
	:t5: Time constant of second boiler pass (i.e. reheater) (T5).  Typical Value = 0.5. Default: 
	:k2: Fraction of turbine power developed after second boiler pass (K2).  Typical Value = 0.2. Default: 
	:t6: Time constant of crossover or third boiler pass (T6).  Typical Value = 10. Default: 
	:k3: Fraction of hp turbine power developed after crossover or third boiler pass (K3). Typical Value = 0.6. Default: 
	:ta: Time to close intercept valve (IV) (Ta).  Typical Value = 0.97. Default: 
	:tb: Time until IV starts to reopen (Tb).  Typical Value = 0.98. Default: 
	:tc: Time until IV is fully open (Tc).  Typical Value = 0.99. Default: 
	:prmax: Max. pressure in reheater (Prmax).  Typical Value = 1. Default: 
		'''

	cgmesProfile = TurbineGovernorDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'mwbase': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'uo': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'uc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'pmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'pmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't4': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't5': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't6': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ta': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tb': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'prmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = , k = , t1 = , t2 = , t3 = , uo = , uc = , pmax = , pmin = , t4 = , k1 = , t5 = , k2 = , t6 = , k3 = , ta = , tb = , tc = , prmax = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mwbase = mwbase
		self.k = k
		self.t1 = t1
		self.t2 = t2
		self.t3 = t3
		self.uo = uo
		self.uc = uc
		self.pmax = pmax
		self.pmin = pmin
		self.t4 = t4
		self.k1 = k1
		self.t5 = t5
		self.k2 = k2
		self.t6 = t6
		self.k3 = k3
		self.ta = ta
		self.tb = tb
		self.tc = tc
		self.prmax = prmax
		
	def __str__(self):
		str = 'class=GovSteamFV3\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
