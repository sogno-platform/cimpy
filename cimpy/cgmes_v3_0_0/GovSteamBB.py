from .TurbineGovernorDynamics import TurbineGovernorDynamics


class GovSteamBB(TurbineGovernorDynamics):
	'''
	European governor model.

	:fcut: Frequency deadband (<i>f</i><i><sub>cut</sub></i>) (&gt;= 0).  Typical value = 0,002. Default: 0.0
	:ks: Gain (<i>Ks</i>).  Typical value = 21,0. Default: 0.0
	:kls: Gain (<i>Kls</i>) (&gt; 0).  Typical value = 0,1. Default: 0.0
	:kg: Gain (<i>Kg</i>).  Typical value = 1,0. Default: 0.0
	:t1: Time constant (<i>T1</i>).  Typical value = 0,05. Default: 0
	:kp: Gain (<i>Kp</i>).  Typical value = 1,0. Default: 0.0
	:tn: Time constant (<i>Tn</i>) (&gt; 0).  Typical value = 1,0. Default: 0
	:kd: Gain (<i>Kd</i>).  Typical value = 1,0. Default: 0.0
	:td: Time constant (<i>Td</i>) (&gt; 0).  Typical value = 1,0. Default: 0
	:pmax: High power limit (<i>Pmax</i>) (&gt; GovSteamBB.pmin).  Typical value = 1,0. Default: 0.0
	:pmin: Low power limit (<i>Pmin</i>) (&lt; GovSteamBB.pmax).  Typical value = 0. Default: 0.0
	:t4: Time constant (<i>T4</i>).  Typical value = 0,15. Default: 0
	:k2: Gain (<i>K2</i>).  Typical value = 0,75. Default: 0.0
	:t5: Time constant (<i>T5</i>).  Typical value = 12,0. Default: 0
	:k3: Gain (<i>K3</i>).  Typical value = 0,5. Default: 0.0
	:t6: Time constant (<i>T6</i>).  Typical value = 0,75. Default: 0
	:peflag: Electric power input selection (Peflag).   true = electric power input false = feedback signal. Typical value = false. Default: False
		'''

	cgmesProfile = TurbineGovernorDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'fcut': [cgmesProfile.DY.value, ],
						'ks': [cgmesProfile.DY.value, ],
						'kls': [cgmesProfile.DY.value, ],
						'kg': [cgmesProfile.DY.value, ],
						't1': [cgmesProfile.DY.value, ],
						'kp': [cgmesProfile.DY.value, ],
						'tn': [cgmesProfile.DY.value, ],
						'kd': [cgmesProfile.DY.value, ],
						'td': [cgmesProfile.DY.value, ],
						'pmax': [cgmesProfile.DY.value, ],
						'pmin': [cgmesProfile.DY.value, ],
						't4': [cgmesProfile.DY.value, ],
						'k2': [cgmesProfile.DY.value, ],
						't5': [cgmesProfile.DY.value, ],
						'k3': [cgmesProfile.DY.value, ],
						't6': [cgmesProfile.DY.value, ],
						'peflag': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, fcut = 0.0, ks = 0.0, kls = 0.0, kg = 0.0, t1 = 0, kp = 0.0, tn = 0, kd = 0.0, td = 0, pmax = 0.0, pmin = 0.0, t4 = 0, k2 = 0.0, t5 = 0, k3 = 0.0, t6 = 0, peflag = False,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.fcut = fcut
		self.ks = ks
		self.kls = kls
		self.kg = kg
		self.t1 = t1
		self.kp = kp
		self.tn = tn
		self.kd = kd
		self.td = td
		self.pmax = pmax
		self.pmin = pmin
		self.t4 = t4
		self.k2 = k2
		self.t5 = t5
		self.k3 = k3
		self.t6 = t6
		self.peflag = peflag
		
	def __str__(self):
		str = 'class=GovSteamBB\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
