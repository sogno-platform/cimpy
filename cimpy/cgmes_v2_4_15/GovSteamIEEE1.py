from cimpy.cgmes_v2_4_15_flat.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovSteamIEEE1(TurbineGovernorDynamics):
	'''
	IEEE steam turbine governor model.  Ref

	:mwbase: Base for power values (MWbase) (> 0) Default: 0.0
	:k: Governor gain (reciprocal of droop) (K) (> 0).  Typical Value = 25. Default: 0.0
	:t1: Governor lag time constant (T1).  Typical Value = 0. Default: 0.0
	:t2: Governor lead time constant (T2).  Typical Value = 0. Default: 0.0
	:t3: Valve positioner time constant (T3) (> 0).  Typical Value = 0.1. Default: 0.0
	:uo: Maximum valve opening velocity (Uo) (> 0).  Unit = PU/sec.  Typical Value = 1. Default: 0.0
	:uc: Maximum valve closing velocity (Uc) (< 0).  Unit = PU/sec.  Typical Value = -10. Default: 0.0
	:pmax: Maximum valve opening (Pmax) (> Pmin).  Typical Value = 1. Default: 0.0
	:pmin: Minimum valve opening (Pmin) (>= 0).  Typical Value = 0. Default: 0.0
	:t4: Inlet piping/steam bowl time constant (T4).  Typical Value = 0.3. Default: 0.0
	:k1: Fraction of HP shaft power after first boiler pass (K1).  Typical Value = 0.2. Default: 0.0
	:k2: Fraction of LP shaft power after first boiler pass (K2).  Typical Value = 0. Default: 0.0
	:t5: Time constant of second boiler pass (T5).  Typical Value = 5. Default: 0.0
	:k3: Fraction of HP shaft power after second boiler pass (K3).  Typical Value = 0.3. Default: 0.0
	:k4: Fraction of LP shaft power after second boiler pass (K4).  Typical Value = 0. Default: 0.0
	:t6: Time constant of third boiler pass (T6).  Typical Value = 0.5. Default: 0.0
	:k5: Fraction of HP shaft power after third boiler pass (K5).  Typical Value = 0.5. Default: 0.0
	:k6: Fraction of LP shaft power after third boiler pass (K6).  Typical Value = 0. Default: 0.0
	:t7: Time constant of fourth boiler pass (T7).  Typical Value = 0. Default: 0.0
	:k7: Fraction of HP shaft power after fourth boiler pass (K7).  Typical Value = 0. Default: 0.0
	:k8: Fraction of LP shaft power after fourth boiler pass (K8).  Typical Value = 0. Default: 0.0
		'''

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
						'k2': [cgmesProfile.DY.value, ],
						't5': [cgmesProfile.DY.value, ],
						'k3': [cgmesProfile.DY.value, ],
						'k4': [cgmesProfile.DY.value, ],
						't6': [cgmesProfile.DY.value, ],
						'k5': [cgmesProfile.DY.value, ],
						'k6': [cgmesProfile.DY.value, ],
						't7': [cgmesProfile.DY.value, ],
						'k7': [cgmesProfile.DY.value, ],
						'k8': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = 0.0, k = 0.0, t1 = 0.0, t2 = 0.0, t3 = 0.0, uo = 0.0, uc = 0.0, pmax = 0.0, pmin = 0.0, t4 = 0.0, k1 = 0.0, k2 = 0.0, t5 = 0.0, k3 = 0.0, k4 = 0.0, t6 = 0.0, k5 = 0.0, k6 = 0.0, t7 = 0.0, k7 = 0.0, k8 = 0.0,  *args, **kw_args):
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
		self.k2 = k2
		self.t5 = t5
		self.k3 = k3
		self.k4 = k4
		self.t6 = t6
		self.k5 = k5
		self.k6 = k6
		self.t7 = t7
		self.k7 = k7
		self.k8 = k8
		
	def __str__(self):
		str = 'class=GovSteamIEEE1\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
