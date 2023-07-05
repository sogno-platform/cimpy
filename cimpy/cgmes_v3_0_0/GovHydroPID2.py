from .TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydroPID2(TurbineGovernorDynamics):
	'''
	Hydro turbine and governor. Represents plants with straightforward penstock configurations and "three term" electro-hydraulic governors (i.e. Woodward<sup>TM</sup> electronic). [Footnote: Woodward electronic governors are an example of suitable products available commercially. This information is given for the convenience of users of this document and does not constitute an endorsement by IEC of these products.]

	:mwbase: Base for power values (<i>MWbase</i>) (&gt;0).  Unit = MW. Default: 0.0
	:treg: Speed detector time constant (<i>Treg</i>) (&gt;= 0).  Typical value = 0. Default: 0
	:rperm: Permanent drop (<i>Rperm</i>).  Typical value = 0. Default: 0.0
	:kp: Proportional gain (<i>Kp</i>).  Typical value = 0. Default: 0.0
	:ki: Reset gain (<i>Ki</i>).  Unit = PU/s.  Typical value = 0. Default: 0.0
	:kd: Derivative gain (<i>Kd</i>).  Typical value = 0. Default: 0.0
	:ta: Controller time constant (<i>Ta</i>) (&gt;= 0).  Typical value = 0. Default: 0
	:tb: Gate servo time constant (<i>Tb</i>) (&gt; 0). Default: 0
	:velmax: Maximum gate opening velocity (<i>Velmax</i>) (&lt; GovHydroPID2.velmin).  Unit = PU / s.  Typical value = 0. Default: 0.0
	:velmin: Maximum gate closing velocity (<i>Velmin</i>) (&gt; GovHydroPID2.velmax).  Unit = PU / s.  Typical value = 0. Default: 0.0
	:gmax: Maximum gate opening (<i>Gmax</i>) (&gt; GovHydroPID2.gmin).  Typical value = 0. Default: 0.0
	:gmin: Minimum gate opening (<i>Gmin</i>) (&gt; GovHydroPID2.gmax).  Typical value = 0. Default: 0.0
	:tw: Water inertia time constant (<i>Tw</i>) (&gt;= 0).  Typical value = 0. Default: 0
	:d: Turbine damping factor (<i>D</i>).  Unit = delta P / delta speed.  Typical value = 0. Default: 0.0
	:g0: Gate opening at speed no load (<i>G0</i>).  Typical value = 0. Default: 0.0
	:g1: Intermediate gate opening (<i>G1</i>).  Typical value = 0. Default: 0.0
	:p1: Power at gate opening <i>G1</i> (<i>P1</i>).  Typical value = 0. Default: 0.0
	:g2: Intermediate gate opening (<i>G2</i>).  Typical value = 0. Default: 0.0
	:p2: Power at gate opening G2 (<i>P2</i>).  Typical value = 0. Default: 0.0
	:p3: Power at full opened gate (<i>P3</i>).  Typical value = 0. Default: 0.0
	:atw: Factor multiplying <i>Tw</i> (<i>Atw</i>).  Typical value = 0. Default: 0.0
	:feedbackSignal: Feedback signal type flag (<i>Flag</i>). true = use gate position feedback signal false = use Pe. Default: False
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

	def __init__(self, mwbase = 0.0, treg = 0, rperm = 0.0, kp = 0.0, ki = 0.0, kd = 0.0, ta = 0, tb = 0, velmax = 0.0, velmin = 0.0, gmax = 0.0, gmin = 0.0, tw = 0, d = 0.0, g0 = 0.0, g1 = 0.0, p1 = 0.0, g2 = 0.0, p2 = 0.0, p3 = 0.0, atw = 0.0, feedbackSignal = False,  *args, **kw_args):
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
