from cimpy.cgmes_v2_4_15_flat.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovGAST(TurbineGovernorDynamics):
	'''
	Single shaft gas turbine.

	:mwbase: Base for power values (MWbase) (> 0). Default: 0.0
	:r: Permanent droop (R).  Typical Value = 0.04. Default: 0.0
	:t1: Governor mechanism time constant (T1).  T1 represents the natural valve positioning time constant of the governor for small disturbances, as seen when rate limiting is not in effect.  Typical Value = 0.5. Default: 0.0
	:t2: Turbine power time constant (T2).  T2 represents delay due to internal energy storage of the gas turbine engine. T2 can be used to give a rough approximation to the delay associated with acceleration of the compressor spool of a multi-shaft engine, or with the compressibility of gas in the plenum of a the free power turbine of an aero-derivative unit, for example.  Typical Value = 0.5. Default: 0.0
	:t3: Turbine exhaust temperature time constant (T3).  Typical Value = 3. Default: 0.0
	:at: Ambient temperature load limit (Load Limit).  Typical Value = 1. Default: 0.0
	:kt: Temperature limiter gain (Kt).  Typical Value = 3. Default: 0.0
	:vmax: Maximum turbine power, PU of MWbase (Vmax).  Typical Value = 1. Default: 0.0
	:vmin: Minimum turbine power, PU of MWbase (Vmin).  Typical Value = 0. Default: 0.0
	:dturb: Turbine damping factor (Dturb).  Typical Value = 0.18. Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'mwbase': [cgmesProfile.DY.value, ],
						'r': [cgmesProfile.DY.value, ],
						't1': [cgmesProfile.DY.value, ],
						't2': [cgmesProfile.DY.value, ],
						't3': [cgmesProfile.DY.value, ],
						'at': [cgmesProfile.DY.value, ],
						'kt': [cgmesProfile.DY.value, ],
						'vmax': [cgmesProfile.DY.value, ],
						'vmin': [cgmesProfile.DY.value, ],
						'dturb': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = 0.0, r = 0.0, t1 = 0.0, t2 = 0.0, t3 = 0.0, at = 0.0, kt = 0.0, vmax = 0.0, vmin = 0.0, dturb = 0.0,  *args, **kw_args):
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
