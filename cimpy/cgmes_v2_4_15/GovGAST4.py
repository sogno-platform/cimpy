from cimpy.output.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovGAST4(TurbineGovernorDynamics):
	'''
	Generic turbogas.

	:bp: Droop (bp).  Typical Value = 0.05. Default: 
	:tv: Time constant of fuel valve positioner (T).  Typical Value = 0.1. Default: 
	:ta: Maximum gate opening velocity (T).  Typical Value = 3. Default: 
	:tc: Maximum gate closing velocity (T).  Typical Value = 0.5. Default: 
	:tcm: Fuel control time constant (T).  Typical Value = 0.1. Default: 
	:ktm: Compressor gain (K).  Typical Value = 0. Default: 
	:tm: Compressor discharge volume time constant (T).  Typical Value = 0.2. Default: 
	:rymx: Maximum valve opening (RYMX).  Typical Value = 1.1. Default: 
	:rymn: Minimum valve opening (RYMN).  Typical Value = 0. Default: 
	:mxef: Fuel flow maximum positive error value (MX).  Typical Value = 0.05. Default: 
	:mnef: Fuel flow maximum negative error value (MN).  Typical Value = -0.05. Default: 
		'''

	cgmesProfile = TurbineGovernorDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'bp': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tv': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ta': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tcm': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ktm': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tm': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'rymx': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'rymn': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'mxef': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'mnef': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, bp = , tv = , ta = , tc = , tcm = , ktm = , tm = , rymx = , rymn = , mxef = , mnef = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.bp = bp
		self.tv = tv
		self.ta = ta
		self.tc = tc
		self.tcm = tcm
		self.ktm = ktm
		self.tm = tm
		self.rymx = rymx
		self.rymn = rymn
		self.mxef = mxef
		self.mnef = mnef
		
	def __str__(self):
		str = 'class=GovGAST4\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
