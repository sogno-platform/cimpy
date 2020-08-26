from cimpy.output.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovSteamSGO(TurbineGovernorDynamics):
	'''
	Simplified Steam turbine governor model.

	:mwbase: Base for power values (MWbase) (>0).  Unit = MW. Default: 
	:t1: Controller lag (T1). Default: 
	:t2: Controller lead compensation (T2). Default: 
	:t3: Governor lag (T3) (>0). Default: 
	:t4: Delay due to steam inlet volumes associated with steam chest and inlet piping (T4). Default: 
	:t5: Reheater delay including hot and cold leads (T5). Default: 
	:t6: Delay due to IP-LP turbine, crossover pipes and LP end hoods (T6). Default: 
	:k1: One/per unit regulation (K1). Default: 
	:k2: Fraction (K2). Default: 
	:k3: Fraction (K3). Default: 
	:pmax: Upper power limit (Pmax). Default: 
	:pmin: Lower power limit (Pmin). Default: 
		'''

	cgmesProfile = TurbineGovernorDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'mwbase': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't4': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't5': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't6': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'pmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'pmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = , t1 = , t2 = , t3 = , t4 = , t5 = , t6 = , k1 = , k2 = , k3 = , pmax = , pmin = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mwbase = mwbase
		self.t1 = t1
		self.t2 = t2
		self.t3 = t3
		self.t4 = t4
		self.t5 = t5
		self.t6 = t6
		self.k1 = k1
		self.k2 = k2
		self.k3 = k3
		self.pmax = pmax
		self.pmin = pmin
		
	def __str__(self):
		str = 'class=GovSteamSGO\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
