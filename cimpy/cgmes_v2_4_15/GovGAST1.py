from cimpy.output.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovGAST1(TurbineGovernorDynamics):
	'''
	Modified single shaft gas turbine.

	:mwbase: Base for power values (MWbase) (> 0).  Unit = MW. Default: 
	:r: Permanent droop (R).  Typical Value = 0.04. Default: 
	:t1: Governor mechanism time constant (T1).  T1 represents the natural valve positioning time constant of the governor for small disturbances, as seen when rate limiting is not in effect.  Typical Value = 0.5. Default: 
	:t2: Turbine power time constant (T2).  T2 represents delay due to internal energy storage of the gas turbine engine. T2 can be used to give a rough approximation to the delay associated with acceleration of the compressor spool of a multi-shaft engine, or with the compressibility of gas in the plenum of the free power turbine of an aero-derivative unit, for example.  Typical Value = 0.5. Default: 
	:t3: Turbine exhaust temperature time constant (T3).  T3 represents delay in the exhaust temperature and load limiting system. Typical Value = 3. Default: 
	:lmax: Ambient temperature load limit (Lmax).  Lmax is the turbine power output corresponding to the limiting exhaust gas temperature.  Typical Value = 1. Default: 
	:kt: Temperature limiter gain (Kt).  Typical Value = 3. Default: 
	:vmax: Maximum turbine power, PU of MWbase (Vmax).  Typical Value = 1. Default: 
	:vmin: Minimum turbine power, PU of MWbase (Vmin).  Typical Value = 0. Default: 
	:fidle: Fuel flow at zero power output (Fidle).  Typical Value = 0.18. Default: 
	:rmax: Maximum fuel valve opening rate (Rmax).  Unit = PU/sec.  Typical Value = 1. Default: 
	:loadinc: Valve position change allowed at fast rate (Loadinc).  Typical Value = 0.05. Default: 
	:tltr: Valve position averaging time constant (Tltr).  Typical Value = 10. Default: 
	:ltrate: Maximum long term fuel valve opening rate (Ltrate).  Typical Value = 0.02. Default: 
	:a: Turbine power time constant numerator scale factor (a).  Typical Value = 0.8. Default: 
	:b: Turbine power time constant denominator scale factor (b).  Typical Value = 1. Default: 
	:db1: Intentional dead-band width (db1).  Unit = Hz.  Typical Value = 0. Default: 
	:eps: Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0. Default: 
	:db2: Unintentional dead-band (db2).  Unit = MW.  Typical Value = 0. Default: 
	:gv1: Nonlinear gain point 1, PU gv (Gv1).  Typical Value = 0. Default: 
	:pgv1: Nonlinear gain point 1, PU power (Pgv1).  Typical Value = 0. Default: 
	:gv2: Nonlinear gain point 2,PU gv (Gv2).  Typical Value = 0. Default: 
	:pgv2: Nonlinear gain point 2, PU power (Pgv2).  Typical Value = 0. Default: 
	:gv3: Nonlinear gain point 3, PU gv (Gv3).  Typical Value = 0. Default: 
	:pgv3: Nonlinear gain point 3, PU power (Pgv3).  Typical Value = 0. Default: 
	:gv4: Nonlinear gain point 4, PU gv (Gv4).  Typical Value = 0. Default: 
	:pgv4: Nonlinear gain point 4, PU power (Pgv4).  Typical Value = 0. Default: 
	:gv5: Nonlinear gain point 5, PU gv (Gv5).  Typical Value = 0. Default: 
	:pgv5: Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0. Default: 
	:gv6: Nonlinear gain point 6, PU gv (Gv6).  Typical Value = 0. Default: 
	:pgv6: Nonlinear gain point 6, PU power (Pgv6).  Typical Value = 0. Default: 
	:ka: Governor gain (Ka).  Typical Value = 0. Default: 
	:t4: Governor lead time constant (T4).  Typical Value = 0. Default: 
	:t5: Governor lag time constant (T5).  Typical Value = 0. Default: 
		'''

	cgmesProfile = TurbineGovernorDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'mwbase': [cgmesProfile.DY.value, ],
						'r': [cgmesProfile.DY.value, ],
						't1': [cgmesProfile.DY.value, ],
						't2': [cgmesProfile.DY.value, ],
						't3': [cgmesProfile.DY.value, ],
						'lmax': [cgmesProfile.DY.value, ],
						'kt': [cgmesProfile.DY.value, ],
						'vmax': [cgmesProfile.DY.value, ],
						'vmin': [cgmesProfile.DY.value, ],
						'fidle': [cgmesProfile.DY.value, ],
						'rmax': [cgmesProfile.DY.value, ],
						'loadinc': [cgmesProfile.DY.value, ],
						'tltr': [cgmesProfile.DY.value, ],
						'ltrate': [cgmesProfile.DY.value, ],
						'a': [cgmesProfile.DY.value, ],
						'b': [cgmesProfile.DY.value, ],
						'db1': [cgmesProfile.DY.value, ],
						'eps': [cgmesProfile.DY.value, ],
						'db2': [cgmesProfile.DY.value, ],
						'gv1': [cgmesProfile.DY.value, ],
						'pgv1': [cgmesProfile.DY.value, ],
						'gv2': [cgmesProfile.DY.value, ],
						'pgv2': [cgmesProfile.DY.value, ],
						'gv3': [cgmesProfile.DY.value, ],
						'pgv3': [cgmesProfile.DY.value, ],
						'gv4': [cgmesProfile.DY.value, ],
						'pgv4': [cgmesProfile.DY.value, ],
						'gv5': [cgmesProfile.DY.value, ],
						'pgv5': [cgmesProfile.DY.value, ],
						'gv6': [cgmesProfile.DY.value, ],
						'pgv6': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						't4': [cgmesProfile.DY.value, ],
						't5': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = , r = , t1 = , t2 = , t3 = , lmax = , kt = , vmax = , vmin = , fidle = , rmax = , loadinc = , tltr = , ltrate = , a = , b = , db1 = , eps = , db2 = , gv1 = , pgv1 = , gv2 = , pgv2 = , gv3 = , pgv3 = , gv4 = , pgv4 = , gv5 = , pgv5 = , gv6 = , pgv6 = , ka = , t4 = , t5 = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mwbase = mwbase
		self.r = r
		self.t1 = t1
		self.t2 = t2
		self.t3 = t3
		self.lmax = lmax
		self.kt = kt
		self.vmax = vmax
		self.vmin = vmin
		self.fidle = fidle
		self.rmax = rmax
		self.loadinc = loadinc
		self.tltr = tltr
		self.ltrate = ltrate
		self.a = a
		self.b = b
		self.db1 = db1
		self.eps = eps
		self.db2 = db2
		self.gv1 = gv1
		self.pgv1 = pgv1
		self.gv2 = gv2
		self.pgv2 = pgv2
		self.gv3 = gv3
		self.pgv3 = pgv3
		self.gv4 = gv4
		self.pgv4 = pgv4
		self.gv5 = gv5
		self.pgv5 = pgv5
		self.gv6 = gv6
		self.pgv6 = pgv6
		self.ka = ka
		self.t4 = t4
		self.t5 = t5
		
	def __str__(self):
		str = 'class=GovGAST1\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
