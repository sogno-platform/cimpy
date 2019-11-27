from cimpy.cgmes_v2_4_15.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovSteamFV3(TurbineGovernorDynamics):
	'''
	Simplified GovSteamIEEE1 Steam turbine governor model with Prmax limit and fast valving.

	:mwbase: Base for power values (MWbase) (>0).  Unit = MW. Default: 0.0
	:k: Governor gain, (reciprocal of droop) (K).  Typical Value = 20. Default: 0.0
	:t1: Governor lead time constant (T1).  Typical Value = 0. Default: 0.0
	:t2: Governor lag time constant (T2).  Typical Value = 0. Default: 0.0
	:t3: Valve positioner time constant (T3).  Typical Value = 0. Default: 0.0
	:uo: Maximum valve opening velocity (Uo).  Unit = PU/sec.  Typical Value = 0.1. Default: 0.0
	:uc: Maximum valve closing velocity (Uc).  Unit = PU/sec.  Typical Value = -1. Default: 0.0
	:pmax: Maximum valve opening, PU of MWbase (Pmax).  Typical Value = 1. Default: 0.0
	:pmin: Minimum valve opening, PU of MWbase (Pmin).  Typical Value = 0. Default: 0.0
	:t4: Inlet piping/steam bowl time constant (T4).  Typical Value = 0.2. Default: 0.0
	:k1: Fraction of turbine power developed after first boiler pass (K1).  Typical Value = 0.2. Default: 0.0
	:t5: Time constant of second boiler pass (i.e. reheater) (T5).  Typical Value = 0.5. Default: 0.0
	:k2: Fraction of turbine power developed after second boiler pass (K2).  Typical Value = 0.2. Default: 0.0
	:t6: Time constant of crossover or third boiler pass (T6).  Typical Value = 10. Default: 0.0
	:k3: Fraction of hp turbine power developed after crossover or third boiler pass (K3). Typical Value = 0.6. Default: 0.0
	:ta: Time to close intercept valve (IV) (Ta).  Typical Value = 0.97. Default: 0.0
	:tb: Time until IV starts to reopen (Tb).  Typical Value = 0.98. Default: 0.0
	:tc: Time until IV is fully open (Tc).  Typical Value = 0.99. Default: 0.0
	:prmax: Max. pressure in reheater (Prmax).  Typical Value = 1. Default: 0.0
		'''

	cgmesProfile = TurbineGovernorDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'mwbase': [cgmesProfile.DY.value, ],
						'k': [cgmesProfile.DY.value, ],
						't1': [cgmesProfile.DY.value, ],
						't2': [cgmesProfile.DY.value, ],
						't3': [cgmesProfile.DY.value, ],
						'uo': [cgmesProfile.DY.value, ],
						'uc': [cgmesProfile.DY.value, ],
						'pmax': [cgmesProfile.DY.value, ],
						'pmin': [cgmesProfile.DY.value, ],
						't4': [cgmesProfile.DY.value, ],
						'k1': [cgmesProfile.DY.value, ],
						't5': [cgmesProfile.DY.value, ],
						'k2': [cgmesProfile.DY.value, ],
						't6': [cgmesProfile.DY.value, ],
						'k3': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						'prmax': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = 0.0, k = 0.0, t1 = 0.0, t2 = 0.0, t3 = 0.0, uo = 0.0, uc = 0.0, pmax = 0.0, pmin = 0.0, t4 = 0.0, k1 = 0.0, t5 = 0.0, k2 = 0.0, t6 = 0.0, k3 = 0.0, ta = 0.0, tb = 0.0, tc = 0.0, prmax = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mwbase = mwbase
		self.k = k
		self.t1 = t1
		self.t2 = t2
		self.t3 = t3
		self.uo = uo
		self.uc = uc
		self.pmax = pmax
		self.pmin = pmin
		self.t4 = t4
		self.k1 = k1
		self.t5 = t5
		self.k2 = k2
		self.t6 = t6
		self.k3 = k3
		self.ta = ta
		self.tb = tb
		self.tc = tc
		self.prmax = prmax
		
	def __str__(self):
		str = 'class=GovSteamFV3\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
