from .TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydroPID(TurbineGovernorDynamics):
	'''
	PID governor and turbine.

	:mwbase: Base for power values (<i>MWbase</i>) (&gt; 0).  Unit = MW. Default: 0.0
	:pmax: Maximum gate opening, PU of MWbase (<i>Pmax</i>) (&gt; GovHydroPID.pmin).  Typical value = 1. Default: 0.0
	:pmin: Minimum gate opening, PU of MWbase (<i>Pmin</i>) (&lt; GovHydroPID.pmax).  Typical value = 0. Default: 0.0
	:r: Steady state droop (<i>R</i>).  Typical value = 0,05. Default: 0.0
	:td: Input filter time constant (<i>Td</i>) (&gt;= 0).  If = 0, block is bypassed.  Typical value = 0. Default: 0
	:tf: Washout time constant (<i>Tf</i>) (&gt;= 0).  Typical value = 0,1. Default: 0
	:tp: Gate servo time constant (<i>Tp</i>) (&gt;= 0).  If = 0, block is bypassed.  Typical value = 0,35. Default: 0
	:velop: Maximum gate opening velocity (<i>Velop</i>).  Unit = PU / s.  Typical value = 0,09. Default: 0.0
	:velcl: Maximum gate closing velocity (<i>Velcl</i>).  Unit = PU / s.  Typical value = -0,14. Default: 0.0
	:kd: Derivative gain (<i>Kd</i>).  Typical value = 1,11. Default: 0.0
	:kp: Proportional gain (<i>Kp</i>).  Typical value = 0,1. Default: 0.0
	:ki: Integral gain (<i>Ki</i>).  Typical value = 0,36. Default: 0.0
	:kg: Gate servo gain (<i>Kg</i>).  Typical value = 2,5. Default: 0.0
	:tturb: Turbine time constant (<i>Tturb</i>) (&gt;= 0). See Parameter detail 3.  Typical value = 0,8. Default: 0
	:aturb: Turbine numerator multiplier (<i>Aturb</i>) (see parameter detail 3).  Typical value -1. Default: 0.0
	:bturb: Turbine denominator multiplier (<i>Bturb</i>) (see parameter detail 3).  Typical value = 0,5. Default: 0.0
	:tt: Power feedback time constant (<i>Tt</i>) (&gt;= 0).  If = 0, block is bypassed.  Typical value = 0,02. Default: 0
	:db1: Intentional dead-band width (<i>db1</i>).  Unit = Hz.  Typical value = 0. Default: 0.0
	:inputSignal: Input signal switch (<i>Flag</i>).  true = <i>Pe</i> input is used false = feedback is received from <i>CV</i>. <i>Flag</i> is normally dependent on <i>Tt</i>.  If <i>Tt </i>is zero, <i>Flag</i> is set to false. If <i>Tt</i> is not zero, <i>Flag</i> is set to true.   Typical value = true. Default: False
	:eps: Intentional db hysteresis (<i>eps</i>).  Unit = Hz.  Typical value = 0. Default: 0.0
	:db2: Unintentional dead-band (<i>db2</i>).  Unit = MW.  Typical value = 0. Default: 0.0
	:gv1: Nonlinear gain point 1, PU gv (<i>Gv1</i>).  Typical value = 0. Default: 0.0
	:pgv1: Nonlinear gain point 1, PU power (<i>Pgv1</i>).  Typical value = 0. Default: 0.0
	:gv2: Nonlinear gain point 2, PU gv (<i>Gv2</i>).  Typical value = 0. Default: 0.0
	:pgv2: Nonlinear gain point 2, PU power (<i>Pgv2</i>).  Typical value = 0. Default: 0.0
	:gv3: Nonlinear gain point 3, PU gv (<i>Gv3</i>).  Typical value = 0. Default: 0.0
	:pgv3: Nonlinear gain point 3, PU power (<i>Pgv3</i>).  Typical value = 0. Default: 0.0
	:gv4: Nonlinear gain point 4, PU gv (<i>Gv4</i>).  Typical value = 0. Default: 0.0
	:pgv4: Nonlinear gain point 4, PU power (<i>Pgv4</i>).  Typical value = 0. Default: 0.0
	:gv5: Nonlinear gain point 5, PU gv (<i>Gv5</i>).  Typical value = 0. Default: 0.0
	:pgv5: Nonlinear gain point 5, PU power (<i>Pgv5</i>).  Typical value = 0. Default: 0.0
	:gv6: Nonlinear gain point 6, PU gv (<i>Gv6</i>).  Typical value = 0. Default: 0.0
	:pgv6: Nonlinear gain point 6, PU power (<i>Pgv6</i>).  Typical value = 0. Default: 0.0
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

	def __init__(self, mwbase = 0.0, pmax = 0.0, pmin = 0.0, r = 0.0, td = 0, tf = 0, tp = 0, velop = 0.0, velcl = 0.0, kd = 0.0, kp = 0.0, ki = 0.0, kg = 0.0, tturb = 0, aturb = 0.0, bturb = 0.0, tt = 0, db1 = 0.0, inputSignal = False, eps = 0.0, db2 = 0.0, gv1 = 0.0, pgv1 = 0.0, gv2 = 0.0, pgv2 = 0.0, gv3 = 0.0, pgv3 = 0.0, gv4 = 0.0, pgv4 = 0.0, gv5 = 0.0, pgv5 = 0.0, gv6 = 0.0, pgv6 = 0.0,  *args, **kw_args):
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
