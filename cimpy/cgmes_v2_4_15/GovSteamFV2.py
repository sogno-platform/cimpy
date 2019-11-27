from cimpy.cgmes_v2_4_15.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovSteamFV2(TurbineGovernorDynamics):
	'''
	Steam turbine governor with reheat time constants and modeling of the effects of fast valve closing to reduce mechanical power.

	:mwbase: Alternate Base used instead of Machine base in equipment model if necessary (MWbase) (>0).  Unit = MW. Default: 0.0
	:r: (R). Default: 0.0
	:t1: Governor time constant (T1). Default: 0.0
	:vmax: (Vmax). Default: 0.0
	:vmin: (Vmin). Default: 0.0
	:k: Fraction of the turbine power developed by turbine sections not involved in fast valving (K). Default: 0.0
	:t3: Reheater time constant (T3). Default: 0.0
	:dt: (Dt). Default: 0.0
	:tt: Time constant with which power falls off after intercept valve closure (Tt). Default: 0.0
	:ta: Time after initial time for valve to close (Ta). Default: 0.0
	:tb: Time after initial time for valve to begin opening (Tb). Default: 0.0
	:tc: Time after initial time for valve to become fully open (Tc). Default: 0.0
	:ti: Initial time to begin fast valving (Ti). Default: 0.0
		'''

	cgmesProfile = TurbineGovernorDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'mwbase': [cgmesProfile.DY.value, ],
						'r': [cgmesProfile.DY.value, ],
						't1': [cgmesProfile.DY.value, ],
						'vmax': [cgmesProfile.DY.value, ],
						'vmin': [cgmesProfile.DY.value, ],
						'k': [cgmesProfile.DY.value, ],
						't3': [cgmesProfile.DY.value, ],
						'dt': [cgmesProfile.DY.value, ],
						'tt': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						'ti': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = 0.0, r = 0.0, t1 = 0.0, vmax = 0.0, vmin = 0.0, k = 0.0, t3 = 0.0, dt = 0.0, tt = 0.0, ta = 0.0, tb = 0.0, tc = 0.0, ti = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mwbase = mwbase
		self.r = r
		self.t1 = t1
		self.vmax = vmax
		self.vmin = vmin
		self.k = k
		self.t3 = t3
		self.dt = dt
		self.tt = tt
		self.ta = ta
		self.tb = tb
		self.tc = tc
		self.ti = ti
		
	def __str__(self):
		str = 'class=GovSteamFV2\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
