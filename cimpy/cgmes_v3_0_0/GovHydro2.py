from .TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydro2(TurbineGovernorDynamics):
	'''
	IEEE hydro turbine governor with straightforward penstock configuration and hydraulic-dashpot governor.

	:mwbase: Base for power values (<i>MWbase</i>) (&gt; 0).  Unit = MW. Default: 0.0
	:tg: Gate servo time constant (<i>Tg</i>) (&gt; 0).  Typical value = 0,5. Default: 0
	:tp: Pilot servo valve time constant (<i>Tp</i>) (&gt;= 0).  Typical value = 0,03. Default: 0
	:uo: Maximum gate opening velocity (<i>Uo</i>).  Unit = PU / s.  Typical value = 0,1. Default: 0.0
	:uc: Maximum gate closing velocity (<i>Uc</i>) (&lt; 0).  Unit = PU / s.   Typical value = -0,1. Default: 0.0
	:pmax: Maximum gate opening (<i>Pmax</i>) (&gt; GovHydro2.pmin).  Typical value = 1. Default: 0.0
	:pmin: Minimum gate opening (<i>Pmin</i>) (&lt; GovHydro2.pmax).  Typical value = 0. Default: 0.0
	:rperm: Permanent droop (<i>Rperm</i>).  Typical value = 0,05. Default: 0.0
	:rtemp: Temporary droop (<i>Rtemp</i>).  Typical value = 0,5. Default: 0.0
	:tr: Dashpot time constant (<i>Tr</i>) (&gt;= 0).  Typical value = 12. Default: 0
	:tw: Water inertia time constant (<i>Tw</i>) (&gt;= 0).  Typical value = 2. Default: 0
	:kturb: Turbine gain (<i>Kturb</i>).  Typical value = 1. Default: 0.0
	:aturb: Turbine numerator multiplier (<i>Aturb</i>).  Typical value = -1. Default: 0.0
	:bturb: Turbine denominator multiplier (<i>Bturb</i>) (&gt; 0).  Typical value = 0,5. Default: 0.0
	:db1: Intentional deadband width (<i>db1</i>).  Unit = Hz.  Typical value = 0. Default: 0.0
	:eps: Intentional db hysteresis (<i>eps</i>).  Unit = Hz.  Typical value = 0. Default: 0.0
	:db2: Unintentional deadband (<i>db2</i>).  Unit = MW.  Typical value = 0. Default: 0.0
	:gv1: Nonlinear gain point 1, PU gv (<i>Gv1</i>).  Typical value = 0. Default: 0.0
	:pgv1: Nonlinear gain point 1, PU power (<i>Pgv1</i>).  Typical value = 0. Default: 0.0
	:gv2: Nonlinear gain point 2, PU gv (<i>Gv2</i>).  Typical value = 0. Default: 0.0
	:pgv2: Nonlinear gain point 2, PU power (<i>Pgv2</i>).  Typical value = 0. Default: 0.0
	:gv3: Nonlinear gain point 3, PU gv (<i>Gv3</i>).  Typical value = 0. Default: 0.0
	:pgv3: Nonlinear gain point 3, PU power (<i>Pgv3</i>).  Typical value = 0. Default: 0.0
	:gv4: Nonlinear gain point 4, PU gv (<i>Gv4</i>).  Typical value = 0. Default: 0.0
	:pgv4: Nonlinear gain point 4, PU power (P<i>gv4</i>).  Typical value = 0. Default: 0.0
	:gv5: Nonlinear gain point 5, PU gv (<i>Gv5</i>).  Typical value = 0. Default: 0.0
	:pgv5: Nonlinear gain point 5, PU power (<i>Pgv5</i>).  Typical value = 0. Default: 0.0
	:gv6: Nonlinear gain point 6, PU gv (<i>Gv6</i>).  Typical value = 0. Default: 0.0
	:pgv6: Nonlinear gain point 6, PU power (<i>Pgv6</i>).  Typical value = 0. Default: 0.0
		'''

	cgmesProfile = TurbineGovernorDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'mwbase': [cgmesProfile.DY.value, ],
						'tg': [cgmesProfile.DY.value, ],
						'tp': [cgmesProfile.DY.value, ],
						'uo': [cgmesProfile.DY.value, ],
						'uc': [cgmesProfile.DY.value, ],
						'pmax': [cgmesProfile.DY.value, ],
						'pmin': [cgmesProfile.DY.value, ],
						'rperm': [cgmesProfile.DY.value, ],
						'rtemp': [cgmesProfile.DY.value, ],
						'tr': [cgmesProfile.DY.value, ],
						'tw': [cgmesProfile.DY.value, ],
						'kturb': [cgmesProfile.DY.value, ],
						'aturb': [cgmesProfile.DY.value, ],
						'bturb': [cgmesProfile.DY.value, ],
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
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = 0.0, tg = 0, tp = 0, uo = 0.0, uc = 0.0, pmax = 0.0, pmin = 0.0, rperm = 0.0, rtemp = 0.0, tr = 0, tw = 0, kturb = 0.0, aturb = 0.0, bturb = 0.0, db1 = 0.0, eps = 0.0, db2 = 0.0, gv1 = 0.0, pgv1 = 0.0, gv2 = 0.0, pgv2 = 0.0, gv3 = 0.0, pgv3 = 0.0, gv4 = 0.0, pgv4 = 0.0, gv5 = 0.0, pgv5 = 0.0, gv6 = 0.0, pgv6 = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mwbase = mwbase
		self.tg = tg
		self.tp = tp
		self.uo = uo
		self.uc = uc
		self.pmax = pmax
		self.pmin = pmin
		self.rperm = rperm
		self.rtemp = rtemp
		self.tr = tr
		self.tw = tw
		self.kturb = kturb
		self.aturb = aturb
		self.bturb = bturb
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
		
	def __str__(self):
		str = 'class=GovHydro2\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
