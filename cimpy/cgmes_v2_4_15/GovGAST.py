from cimpy.output.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovGAST(TurbineGovernorDynamics):
	'''
	Single shaft gas turbine.

	:mwbase: Base for power values (MWbase) (> 0). Default: 
	:r: Permanent droop (R).  Typical Value = 0.04. Default: 
	:t1: Governor mechanism time constant (T1).  T1 represents the natural valve positioning time constant of the governor for small disturbances, as seen when rate limiting is not in effect.  Typical Value = 0.5. Default: 
	:t2: Turbine power time constant (T2).  T2 represents delay due to internal energy storage of the gas turbine engine. T2 can be used to give a rough approximation to the delay associated with acceleration of the compressor spool of a multi-shaft engine, or with the compressibility of gas in the plenum of a the free power turbine of an aero-derivative unit, for example.  Typical Value = 0.5. Default: 
	:t3: Turbine exhaust temperature time constant (T3).  Typical Value = 3. Default: 
	:at: Ambient temperature load limit (Load Limit).  Typical Value = 1. Default: 
	:kt: Temperature limiter gain (Kt).  Typical Value = 3. Default: 
	:vmax: Maximum turbine power, PU of MWbase (Vmax).  Typical Value = 1. Default: 
	:vmin: Minimum turbine power, PU of MWbase (Vmin).  Typical Value = 0. Default: 
	:dturb: Turbine damping factor (Dturb).  Typical Value = 0.18. Default: 
		'''

	cgmesProfile = TurbineGovernorDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'mwbase': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'r': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'at': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kt': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'dturb': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = , r = , t1 = , t2 = , t3 = , at = , kt = , vmax = , vmin = , dturb = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mwbase = mwbase
		self.r = r
		self.t1 = t1
		self.t2 = t2
		self.t3 = t3
		self.at = at
		self.kt = kt
		self.vmax = vmax
		self.vmin = vmin
		self.dturb = dturb
		
	def __str__(self):
		str = 'class=GovGAST\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
