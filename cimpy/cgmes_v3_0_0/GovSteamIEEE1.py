from .TurbineGovernorDynamics import TurbineGovernorDynamics


class GovSteamIEEE1(TurbineGovernorDynamics):
	'''
	IEEE steam turbine governor model. Ref<font color="#0f0f0f">erence: IEEE Transactions on Power Apparatus and Systems, November/December 1973, Volume PAS-92, Number 6, <i><u>Dynamic Models for Steam and Hydro Turbines in Power System Studies</u></i>, page 1904.</font>

	:mwbase: Base for power values (<i>MWbase</i>) (&gt; 0)<i>. </i>Unit = MW. Default: 0.0
	:k: Governor gain (reciprocal of droop) (<i>K</i>) (&gt; 0).  Typical value = 25. Default: 0.0
	:t1: Governor lag time constant (<i>T1</i>) (&gt;= 0).  Typical value = 0. Default: 0
	:t2: Governor lead time constant (<i>T2</i>) (&gt;= 0).  Typical value = 0. Default: 0
	:t3: Valve positioner time constant (<i>T3</i>) (&gt; 0).  Typical value = 0,1. Default: 0
	:uo: Maximum valve opening velocity (<i>Uo</i>) (&gt; 0).  Unit = PU / s.  Typical value = 1. Default: 0.0
	:uc: Maximum valve closing velocity (<i>Uc</i>) (&lt; 0).  Unit = PU / s.  Typical value = -10. Default: 0.0
	:pmax: Maximum valve opening (<i>Pmax</i>) (&gt; GovSteamIEEE1.pmin).  Typical value = 1. Default: 0.0
	:pmin: Minimum valve opening (<i>Pmin</i>) (&gt;= 0 and &lt; GovSteamIEEE1.pmax).  Typical value = 0. Default: 0.0
	:t4: Inlet piping/steam bowl time constant (<i>T4</i>) (&gt;= 0).  Typical value = 0,3. Default: 0
	:k1: Fraction of HP shaft power after first boiler pass (<i>K1</i>).  Typical value = 0,2. Default: 0.0
	:k2: Fraction of LP shaft power after first boiler pass (<i>K2</i>).  Typical value = 0. Default: 0.0
	:t5: Time constant of second boiler pass (<i>T5</i>) (&gt;= 0).  Typical value = 5. Default: 0
	:k3: Fraction of HP shaft power after second boiler pass (<i>K3</i>).  Typical value = 0,3. Default: 0.0
	:k4: Fraction of LP shaft power after second boiler pass (<i>K4</i>).  Typical value = 0. Default: 0.0
	:t6: Time constant of third boiler pass (<i>T6</i>) (&gt;= 0).  Typical value = 0,5. Default: 0
	:k5: Fraction of HP shaft power after third boiler pass (<i>K5</i>).  Typical value = 0,5. Default: 0.0
	:k6: Fraction of LP shaft power after third boiler pass (<i>K6</i>).  Typical value = 0. Default: 0.0
	:t7: Time constant of fourth boiler pass (<i>T7</i>) (&gt;= 0).  Typical value = 0. Default: 0
	:k7: Fraction of HP shaft power after fourth boiler pass (<i>K7</i>).  Typical value = 0. Default: 0.0
	:k8: Fraction of LP shaft power after fourth boiler pass (<i>K8</i>).  Typical value = 0. Default: 0.0
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

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = 0.0, k = 0.0, t1 = 0, t2 = 0, t3 = 0, uo = 0.0, uc = 0.0, pmax = 0.0, pmin = 0.0, t4 = 0, k1 = 0.0, k2 = 0.0, t5 = 0, k3 = 0.0, k4 = 0.0, t6 = 0, k5 = 0.0, k6 = 0.0, t7 = 0, k7 = 0.0, k8 = 0.0,  *args, **kw_args):
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
