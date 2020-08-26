from cimpy.cgmes_v2_4_15.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovSteamFV2(TurbineGovernorDynamics):
	'''
	Steam turbine governor with reheat time constants and modeling of the effects of fast valve closing to reduce mechanical power.

	:mwbase: Alternate Base used instead of Machine base in equipment model if necessary (MWbase) (>0).  Unit = MW. Default: 
	:r: (R). Default: 
	:t1: Governor time constant (T1). Default: 
	:vmax: (Vmax). Default: 
	:vmin: (Vmin). Default: 
	:k: Fraction of the turbine power developed by turbine sections not involved in fast valving (K). Default: 
	:t3: Reheater time constant (T3). Default: 
	:dt: (Dt). Default: 
	:tt: Time constant with which power falls off after intercept valve closure (Tt). Default: 
	:ta: Time after initial time for valve to close (Ta). Default: 
	:tb: Time after initial time for valve to begin opening (Tb). Default: 
	:tc: Time after initial time for valve to become fully open (Tc). Default: 
	:ti: Initial time to begin fast valving (Ti). Default: 
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

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = , r = , t1 = , vmax = , vmin = , k = , t3 = , dt = , tt = , ta = , tb = , tc = , ti = ,  *args, **kw_args):
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
