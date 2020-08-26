from cimpy.output.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovSteamFV2(TurbineGovernorDynamics):
	'''
	Steam turbine governor with reheat time constants and modeling of the effects of fast valve closing to reduce mechanical power.

	:mwbase: Alternate Base used instead of Machine base in equipment model if necessary (MWbase) (>0).  Unit = MW. Default: 
	:r: (R). Default: 
	:t1: Governor time constant (T1). Default: 
	:vmax: (Vmax). Default: 
	:vmin: (Vmin). Default: 
	:k: Fraction of the turbine power developed by turbine sections not involved in fast valving (K). Default: 
	:t3: Reheater time constant (T3). Default: 
	:dt: (Dt). Default: 
	:tt: Time constant with which power falls off after intercept valve closure (Tt). Default: 
	:ta: Time after initial time for valve to close (Ta). Default: 
	:tb: Time after initial time for valve to begin opening (Tb). Default: 
	:tc: Time after initial time for valve to become fully open (Tc). Default: 
	:ti: Initial time to begin fast valving (Ti). Default: 
		'''

	cgmesProfile = TurbineGovernorDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'mwbase': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'r': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'dt': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tt': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ta': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tb': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ti': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = , r = , t1 = , vmax = , vmin = , k = , t3 = , dt = , tt = , ta = , tb = , tc = , ti = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mwbase = mwbase
		self.r = r
		self.t1 = t1
		self.vmax = vmax
		self.vmin = vmin
		self.k = k
		self.t3 = t3
		self.dt = dt
		self.tt = tt
		self.ta = ta
		self.tb = tb
		self.tc = tc
		self.ti = ti
		
	def __str__(self):
		str = 'class=GovSteamFV2\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
