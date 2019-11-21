from cimpy.cgmes_v2_4_15_flat.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydro3(TurbineGovernorDynamics):
	'''
	Modified IEEE Hydro Governor-Turbine Model.  This model differs from that defined in the IEEE modeling guideline paper in that the limits on gate position and velocity do not permit "wind up" of the upstream signals.

	:mwbase: Base for power values (MWbase) (> 0).  Unit = MW. Default: 0.0
	:pmax: Maximum gate opening, PU of MWbase (Pmax).  Typical Value = 1. Default: 0.0
	:pmin: Minimum gate opening, PU of MWbase (Pmin).  Typical Value = 0. Default: 0.0
	:governorControl: Governor control flag (Cflag). true = PID control is active false = double derivative control is active. Typical Value = true. Default: False
	:rgate: Steady-state droop, PU, for governor output feedback (Rgate).  Typical Value = 0. Default: 0.0
	:relec: Steady-state droop, PU, for electrical power feedback (Relec).  Typical Value = 0.05. Default: 0.0
	:td: Input filter time constant (Td).  Typical Value = 0.05. Default: 0.0
	:tf: Washout time constant (Tf).  Typical Value = 0.1. Default: 0.0
	:tp: Gate servo time constant (Tp).  Typical Value = 0.05. Default: 0.0
	:velop: Maximum gate opening velocity (Velop).  Unit = PU/sec. Typical Value = 0.2. Default: 0.0
	:velcl: Maximum gate closing velocity (Velcl).  Unit = PU/sec.  Typical Value = -0.2. Default: 0.0
	:k1: Derivative gain (K1).  Typical Value = 0.01. Default: 0.0
	:k2: Double derivative gain, if Cflag = -1 (K2).  Typical Value = 2.5. Default: 0.0
	:ki: Integral gain (Ki).  Typical Value = 0.5. Default: 0.0
	:kg: Gate servo gain (Kg).  Typical Value = 2. Default: 0.0
	:tt: Power feedback time constant (Tt).  Typical Value = 0.2. Default: 0.0
	:db1: Intentional dead-band width (db1).  Unit = Hz.  Typical Value = 0. Default: 0.0
	:eps: Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0. Default: 0.0
	:db2: Unintentional dead-band (db2).  Unit = MW.  Typical Value = 0. Default: 0.0
	:tw: Water inertia time constant (Tw).  Typical Value = 1. Default: 0.0
	:at: Turbine gain (At).  Typical Value = 1.2. Default: 0.0
	:dturb: Turbine damping factor (Dturb).  Typical Value = 0.2. Default: 0.0
	:qnl: No-load turbine flow at nominal head (Qnl).  Typical Value = 0.08. Default: 0.0
	:h0: Turbine nominal head (H0).  Typical Value = 1. Default: 0.0
	:gv1: Nonlinear gain point 1, PU gv (Gv1).  Typical Value = 0. Default: 0.0
	:pgv1: Nonlinear gain point 1, PU power (Pgv1).  Typical Value = 0. Default: 0.0
	:gv2: Nonlinear gain point 2, PU gv (Gv2).  Typical Value = 0. Default: 0.0
	:pgv2: Nonlinear gain point 2, PU power (Pgv2).  Typical Value = 0. Default: 0.0
	:gv3: Nonlinear gain point 3, PU gv (Gv3).  Typical Value = 0. Default: 0.0
	:pgv3: Nonlinear gain point 3, PU power (Pgv3).  Typical Value = 0. Default: 0.0
	:gv4: Nonlinear gain point 4, PU gv (Gv4).  Typical Value = 0. Default: 0.0
	:pgv4: Nonlinear gain point 4, PU power (Pgv4).  Typical Value = 0. Default: 0.0
	:gv5: Nonlinear gain point 5, PU gv (Gv5).  Typical Value = 0. Default: 0.0
	:pgv5: Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0. Default: 0.0
	:gv6: Nonlinear gain point 6, PU gv (Gv6).  Typical Value = 0. Default: 0.0
	:pgv6: Nonlinear gain point 6, PU power (Pgv6).  Typical Value = 0. Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'mwbase': [cgmesProfile.DY.value, ],
						'pmax': [cgmesProfile.DY.value, ],
						'pmin': [cgmesProfile.DY.value, ],
						'governorControl': [cgmesProfile.DY.value, ],
						'rgate': [cgmesProfile.DY.value, ],
						'relec': [cgmesProfile.DY.value, ],
						'td': [cgmesProfile.DY.value, ],
						'tf': [cgmesProfile.DY.value, ],
						'tp': [cgmesProfile.DY.value, ],
						'velop': [cgmesProfile.DY.value, ],
						'velcl': [cgmesProfile.DY.value, ],
						'k1': [cgmesProfile.DY.value, ],
						'k2': [cgmesProfile.DY.value, ],
						'ki': [cgmesProfile.DY.value, ],
						'kg': [cgmesProfile.DY.value, ],
						'tt': [cgmesProfile.DY.value, ],
						'db1': [cgmesProfile.DY.value, ],
						'eps': [cgmesProfile.DY.value, ],
						'db2': [cgmesProfile.DY.value, ],
						'tw': [cgmesProfile.DY.value, ],
						'at': [cgmesProfile.DY.value, ],
						'dturb': [cgmesProfile.DY.value, ],
						'qnl': [cgmesProfile.DY.value, ],
						'h0': [cgmesProfile.DY.value, ],
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

	readInProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = 0.0, pmax = 0.0, pmin = 0.0, governorControl = False, rgate = 0.0, relec = 0.0, td = 0.0, tf = 0.0, tp = 0.0, velop = 0.0, velcl = 0.0, k1 = 0.0, k2 = 0.0, ki = 0.0, kg = 0.0, tt = 0.0, db1 = 0.0, eps = 0.0, db2 = 0.0, tw = 0.0, at = 0.0, dturb = 0.0, qnl = 0.0, h0 = 0.0, gv1 = 0.0, pgv1 = 0.0, gv2 = 0.0, pgv2 = 0.0, gv3 = 0.0, pgv3 = 0.0, gv4 = 0.0, pgv4 = 0.0, gv5 = 0.0, pgv5 = 0.0, gv6 = 0.0, pgv6 = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mwbase = mwbase
		self.pmax = pmax
		self.pmin = pmin
		self.governorControl = governorControl
		self.rgate = rgate
		self.relec = relec
		self.td = td
		self.tf = tf
		self.tp = tp
		self.velop = velop
		self.velcl = velcl
		self.k1 = k1
		self.k2 = k2
		self.ki = ki
		self.kg = kg
		self.tt = tt
		self.db1 = db1
		self.eps = eps
		self.db2 = db2
		self.tw = tw
		self.at = at
		self.dturb = dturb
		self.qnl = qnl
		self.h0 = h0
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
		str = 'class=GovHydro3\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
