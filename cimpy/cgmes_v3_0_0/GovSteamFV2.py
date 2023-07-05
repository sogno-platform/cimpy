from .TurbineGovernorDynamics import TurbineGovernorDynamics


class GovSteamFV2(TurbineGovernorDynamics):
	'''
	Steam turbine governor with reheat time constants and modelling of the effects of fast valve closing to reduce mechanical power.

	:mwbase: Alternate base used instead of machine base in equipment model if necessary (<i>MWbase</i>) (&gt; 0).  Unit = MW. Default: 0.0
	:t1: Governor time constant (<i>T1</i>) (&gt;= 0). Default: 0
	:vmax: (<i>Vmax</i>) (&gt; GovSteamFV2.vmin). Default: 0.0
	:vmin: (<i>Vmin</i>) (&lt; GovSteamFV2.vmax). Default: 0.0
	:k: Fraction of the turbine power developed by turbine sections not involved in fast valving (<i>K</i>). Default: 0.0
	:t3: Reheater time constant (<i>T3</i>) (&gt;= 0). Default: 0
	:dt: (<i>Dt</i>). Default: 0.0
	:tt: Time constant with which power falls off after intercept valve closure (<i>Tt</i>) (&gt;= 0). Default: 0
	:r: (<i>R</i>). Default: 0.0
	:ta: Time after initial time for valve to close (<i>Ta</i>) (&gt;= 0). Default: 0
	:tb: Time after initial time for valve to begin opening (<i>Tb</i>) (&gt;= 0). Default: 0
	:tc: Time after initial time for valve to become fully open (<i>Tc</i>) (&gt;= 0). Default: 0
		'''

	cgmesProfile = TurbineGovernorDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'mwbase': [cgmesProfile.DY.value, ],
						't1': [cgmesProfile.DY.value, ],
						'vmax': [cgmesProfile.DY.value, ],
						'vmin': [cgmesProfile.DY.value, ],
						'k': [cgmesProfile.DY.value, ],
						't3': [cgmesProfile.DY.value, ],
						'dt': [cgmesProfile.DY.value, ],
						'tt': [cgmesProfile.DY.value, ],
						'r': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = 0.0, t1 = 0, vmax = 0.0, vmin = 0.0, k = 0.0, t3 = 0, dt = 0.0, tt = 0, r = 0.0, ta = 0, tb = 0, tc = 0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mwbase = mwbase
		self.t1 = t1
		self.vmax = vmax
		self.vmin = vmin
		self.k = k
		self.t3 = t3
		self.dt = dt
		self.tt = tt
		self.r = r
		self.ta = ta
		self.tb = tb
		self.tc = tc
		
	def __str__(self):
		str = 'class=GovSteamFV2\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
