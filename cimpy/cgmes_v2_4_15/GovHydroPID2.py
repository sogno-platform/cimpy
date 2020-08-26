from cimpy.cgmes_v2_4_15.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydroPID2(TurbineGovernorDynamics):
	'''
	Hydro turbine and governor. Represents plants with straight forward penstock configurations and "three term" electro-hydraulic governors (i.e. Woodard electronic).

	:mwbase: Base for power values (MWbase) (>0).  Unit = MW. Default: 
	:treg: Speed detector time constant (Treg).  Typical Value = 0. Default: 
	:rperm: Permanent drop (Rperm).  Typical Value = 0. Default: 
	:kp: Proportional gain (Kp).  Typical Value = 0. Default: 
	:ki: Reset gain (Ki).  Unit = PU/ sec.  Typical Value = 0. Default: 
	:kd: Derivative gain (Kd).  Typical Value = 0. Default: 
	:ta: Controller time constant (Ta) (>0).  Typical Value = 0. Default: 
	:tb: Gate servo time constant (Tb) (>0).  Typical Value = 0. Default: 
	:velmax: Maximum gate opening velocity (Velmax).  Unit = PU/sec.  Typical Value = 0. Default: 
	:velmin: Maximum gate closing velocity (Velmin).  Unit = PU/sec.  Typical Value = 0. Default: 
	:gmax: Maximum gate opening (Gmax).  Typical Value = 0. Default: 
	:gmin: Minimum gate opening (Gmin).  Typical Value = 0. Default: 
	:tw: Water inertia time constant (Tw) (>0).  Typical Value = 0. Default: 
	:d: Turbine damping factor (D).  Unit = delta P / delta speed.  Typical Value = 0. Default: 
	:g0: Gate opening at speed no load (G0).  Typical Value = 0. Default: 
	:g1: Intermediate gate opening (G1).  Typical Value = 0. Default: 
	:p1: Power at gate opening G1 (P1).  Typical Value = 0. Default: 
	:g2: Intermediate gate opening (G2).  Typical Value = 0. Default: 
	:p2: Power at gate opening G2 (P2).  Typical Value = 0. Default: 
	:p3: Power at full opened gate (P3).  Typical Value = 0. Default: 
	:atw: Factor multiplying Tw (Atw).  Typical Value = 0. Default: 
	:feedbackSignal: Feedback signal type flag (Flag). true = use gate position feedback signal false = use Pe. Default: 
		'''

	cgmesProfile = TurbineGovernorDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'mwbase': [cgmesProfile.DY.value, ],
						'treg': [cgmesProfile.DY.value, ],
						'rperm': [cgmesProfile.DY.value, ],
						'kp': [cgmesProfile.DY.value, ],
						'ki': [cgmesProfile.DY.value, ],
						'kd': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						'velmax': [cgmesProfile.DY.value, ],
						'velmin': [cgmesProfile.DY.value, ],
						'gmax': [cgmesProfile.DY.value, ],
						'gmin': [cgmesProfile.DY.value, ],
						'tw': [cgmesProfile.DY.value, ],
						'd': [cgmesProfile.DY.value, ],
						'g0': [cgmesProfile.DY.value, ],
						'g1': [cgmesProfile.DY.value, ],
						'p1': [cgmesProfile.DY.value, ],
						'g2': [cgmesProfile.DY.value, ],
						'p2': [cgmesProfile.DY.value, ],
						'p3': [cgmesProfile.DY.value, ],
						'atw': [cgmesProfile.DY.value, ],
						'feedbackSignal': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = , treg = , rperm = , kp = , ki = , kd = , ta = , tb = , velmax = , velmin = , gmax = , gmin = , tw = , d = , g0 = , g1 = , p1 = , g2 = , p2 = , p3 = , atw = , feedbackSignal = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mwbase = mwbase
		self.treg = treg
		self.rperm = rperm
		self.kp = kp
		self.ki = ki
		self.kd = kd
		self.ta = ta
		self.tb = tb
		self.velmax = velmax
		self.velmin = velmin
		self.gmax = gmax
		self.gmin = gmin
		self.tw = tw
		self.d = d
		self.g0 = g0
		self.g1 = g1
		self.p1 = p1
		self.g2 = g2
		self.p2 = p2
		self.p3 = p3
		self.atw = atw
		self.feedbackSignal = feedbackSignal
		
	def __str__(self):
		str = 'class=GovHydroPID2\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
