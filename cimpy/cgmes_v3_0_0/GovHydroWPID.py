from .TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydroWPID(TurbineGovernorDynamics):
	'''
	Woodward<sup>TM</sup> PID hydro governor. [Footnote: Woodward PID hydro governors are an example of suitable products available commercially. This information is given for the convenience of users of this document and does not constitute an endorsement by IEC of these products.]

	:mwbase: Base for power values  (<i>MWbase</i>) (&gt; 0).  Unit = MW. Default: 0.0
	:treg: Speed detector time constant (<i>Treg</i>) (&gt;= 0). Default: 0
	:reg: Permanent drop (<i>Reg</i>). Default: 0.0
	:kp: Proportional gain (<i>Kp</i>).  Typical value = 0,1. Default: 0.0
	:ki: Reset gain (<i>Ki</i>).  Typical value = 0,36. Default: 0.0
	:kd: Derivative gain (<i>Kd</i>).  Typical value = 1,11. Default: 0.0
	:ta: Controller time constant (<i>Ta</i>) (&gt;= 0).  Typical value = 0. Default: 0
	:tb: Gate servo time constant (<i>Tb</i>) (&gt;= 0).  Typical value = 0. Default: 0
	:velmax: Maximum gate opening velocity (<i>Velmax</i>) (&gt; GovHydroWPID.velmin).  Unit = PU / s.  Typical value = 0. Default: 0.0
	:velmin: Maximum gate closing velocity (<i>Velmin</i>) (&lt; GovHydroWPID.velmax).  Unit = PU / s.  Typical value = 0. Default: 0.0
	:gatmax: Gate opening limit maximum (<i>Gatmax</i>) (&gt; GovHydroWPID.gatmin). Default: 0.0
	:gatmin: Gate opening limit minimum (<i>Gatmin</i>) (&lt; GovHydroWPID.gatmax). Default: 0.0
	:tw: Water inertia time constant (<i>Tw</i>) (&gt;= 0).  Typical value = 0. Default: 0
	:pmax: Maximum power output (<i>Pmax</i>) (&gt; GovHydroWPID.pmin). Default: 0.0
	:pmin: Minimum power output (<i>Pmin</i>) (&lt; GovHydroWPID.pmax). Default: 0.0
	:d: Turbine damping factor (<i>D</i>).  Unit = delta P / delta speed. Default: 0.0
	:gv3: Gate position 3 (<i>Gv3</i>) (= 1,0). Default: 0.0
	:gv1: Gate position 1 (<i>Gv1</i>). Default: 0.0
	:pgv1: Output at <i>Gv1</i> PU of <i>MWbase</i> (<i>Pgv1</i>). Default: 0.0
	:gv2: Gate position 2 (<i>Gv2</i>). Default: 0.0
	:pgv2: Output at <i>Gv2</i> PU of <i>MWbase</i> (<i>Pgv2</i>). Default: 0.0
	:pgv3: Output at <i>Gv3</i> PU of <i>MWbase</i> (<i>Pgv3</i>). Default: 0.0
		'''

	cgmesProfile = TurbineGovernorDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'mwbase': [cgmesProfile.DY.value, ],
						'treg': [cgmesProfile.DY.value, ],
						'reg': [cgmesProfile.DY.value, ],
						'kp': [cgmesProfile.DY.value, ],
						'ki': [cgmesProfile.DY.value, ],
						'kd': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						'velmax': [cgmesProfile.DY.value, ],
						'velmin': [cgmesProfile.DY.value, ],
						'gatmax': [cgmesProfile.DY.value, ],
						'gatmin': [cgmesProfile.DY.value, ],
						'tw': [cgmesProfile.DY.value, ],
						'pmax': [cgmesProfile.DY.value, ],
						'pmin': [cgmesProfile.DY.value, ],
						'd': [cgmesProfile.DY.value, ],
						'gv3': [cgmesProfile.DY.value, ],
						'gv1': [cgmesProfile.DY.value, ],
						'pgv1': [cgmesProfile.DY.value, ],
						'gv2': [cgmesProfile.DY.value, ],
						'pgv2': [cgmesProfile.DY.value, ],
						'pgv3': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = 0.0, treg = 0, reg = 0.0, kp = 0.0, ki = 0.0, kd = 0.0, ta = 0, tb = 0, velmax = 0.0, velmin = 0.0, gatmax = 0.0, gatmin = 0.0, tw = 0, pmax = 0.0, pmin = 0.0, d = 0.0, gv3 = 0.0, gv1 = 0.0, pgv1 = 0.0, gv2 = 0.0, pgv2 = 0.0, pgv3 = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mwbase = mwbase
		self.treg = treg
		self.reg = reg
		self.kp = kp
		self.ki = ki
		self.kd = kd
		self.ta = ta
		self.tb = tb
		self.velmax = velmax
		self.velmin = velmin
		self.gatmax = gatmax
		self.gatmin = gatmin
		self.tw = tw
		self.pmax = pmax
		self.pmin = pmin
		self.d = d
		self.gv3 = gv3
		self.gv1 = gv1
		self.pgv1 = pgv1
		self.gv2 = gv2
		self.pgv2 = pgv2
		self.pgv3 = pgv3
		
	def __str__(self):
		str = 'class=GovHydroWPID\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
