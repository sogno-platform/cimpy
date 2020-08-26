from cimpy.output.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydroPID(TurbineGovernorDynamics):
	'''
	PID governor and turbine.

	:mwbase: Base for power values (MWbase) (>0).  Unit = MW. Default: 
	:pmax: Maximum gate opening, PU of MWbase (Pmax).  Typical Value = 1. Default: 
	:pmin: Minimum gate opening, PU of MWbase (Pmin).  Typical Value = 0. Default: 
	:r: Steady state droop (R).  Typical Value = 0.05. Default: 
	:td: Input filter time constant (Td).  Typical Value = 0. Default: 
	:tf: Washout time constant (Tf).  Typical Value = 0.1. Default: 
	:tp: Gate servo time constant (Tp).  Typical Value = 0.35. Default: 
	:velop: Maximum gate opening velocity (Velop).  Unit = PU/sec.  Typical Value = 0.09. Default: 
	:velcl: Maximum gate closing velocity (Velcl).  Unit = PU/sec.  Typical Value = -0.14. Default: 
	:kd: Derivative gain (Kd).  Typical Value = 1.11. Default: 
	:kp: Proportional gain (Kp).  Typical Value = 0.1. Default: 
	:ki: Integral gain (Ki).  Typical Value = 0.36. Default: 
	:kg: Gate servo gain (Kg).  Typical Value = 2.5. Default: 
	:tturb: Turbine time constant (Tturb) (note 3).  Typical Value = 0.8. Default: 
	:aturb: Turbine numerator multiplier (Aturb) (note 3).  Typical Value -1. Default: 
	:bturb: Turbine denominator multiplier (Bturb) (note 3).  Typical Value = 0.5. Default: 
	:tt: Power feedback time constant (Tt).  Typical Value = 0.02. Default: 
	:db1: Intentional dead-band width (db1).  Unit = Hz.  Typical Value = 0. Default: 
	:inputSignal: Input signal switch (Flag).  true = Pe input is used false = feedback is received from CV. Flag is normally dependent on Tt.  If Tf is zero, Flag is set to false. If Tf is not zero, Flag is set to true.  Typical Value = true. Default: 
	:eps: Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0. Default: 
	:db2: Unintentional dead-band (db2).  Unit = MW.  Typical Value = 0. Default: 
	:gv1: Nonlinear gain point 1, PU gv (Gv1).  Typical Value = 0. Default: 
	:pgv1: Nonlinear gain point 1, PU power (Pgv1).  Typical Value = 0. Default: 
	:gv2: Nonlinear gain point 2, PU gv (Gv2).  Typical Value = 0. Default: 
	:pgv2: Nonlinear gain point 2, PU power (Pgv2).  Typical Value = 0. Default: 
	:gv3: Nonlinear gain point 3, PU gv (Gv3).  Typical Value = 0. Default: 
	:pgv3: Nonlinear gain point 3, PU power (Pgv3).  Typical Value = 0. Default: 
	:gv4: Nonlinear gain point 4, PU gv (Gv4).  Typical Value = 0. Default: 
	:pgv4: Nonlinear gain point 4, PU power (Pgv4).  Typical Value = 0. Default: 
	:gv5: Nonlinear gain point 5, PU gv (Gv5).  Typical Value = 0. Default: 
	:pgv5: Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0. Default: 
	:gv6: Nonlinear gain point 6, PU gv (Gv6).  Typical Value = 0. Default: 
	:pgv6: Nonlinear gain point 6, PU power (Pgv6).  Typical Value = 0. Default: 
		'''

	cgmesProfile = TurbineGovernorDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'mwbase': [cgmesProfile.DY.value, ],
						'pmax': [cgmesProfile.DY.value, ],
						'pmin': [cgmesProfile.DY.value, ],
						'r': [cgmesProfile.DY.value, ],
						'td': [cgmesProfile.DY.value, ],
						'tf': [cgmesProfile.DY.value, ],
						'tp': [cgmesProfile.DY.value, ],
						'velop': [cgmesProfile.DY.value, ],
						'velcl': [cgmesProfile.DY.value, ],
						'kd': [cgmesProfile.DY.value, ],
						'kp': [cgmesProfile.DY.value, ],
						'ki': [cgmesProfile.DY.value, ],
						'kg': [cgmesProfile.DY.value, ],
						'tturb': [cgmesProfile.DY.value, ],
						'aturb': [cgmesProfile.DY.value, ],
						'bturb': [cgmesProfile.DY.value, ],
						'tt': [cgmesProfile.DY.value, ],
						'db1': [cgmesProfile.DY.value, ],
						'inputSignal': [cgmesProfile.DY.value, ],
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
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = , pmax = , pmin = , r = , td = , tf = , tp = , velop = , velcl = , kd = , kp = , ki = , kg = , tturb = , aturb = , bturb = , tt = , db1 = , inputSignal = , eps = , db2 = , gv1 = , pgv1 = , gv2 = , pgv2 = , gv3 = , pgv3 = , gv4 = , pgv4 = , gv5 = , pgv5 = , gv6 = , pgv6 = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mwbase = mwbase
		self.pmax = pmax
		self.pmin = pmin
		self.r = r
		self.td = td
		self.tf = tf
		self.tp = tp
		self.velop = velop
		self.velcl = velcl
		self.kd = kd
		self.kp = kp
		self.ki = ki
		self.kg = kg
		self.tturb = tturb
		self.aturb = aturb
		self.bturb = bturb
		self.tt = tt
		self.db1 = db1
		self.inputSignal = inputSignal
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
		
	def __str__(self):
		str = 'class=GovHydroPID\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
