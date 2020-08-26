from cimpy.cgmes_v2_4_15.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovSteamCC(TurbineGovernorDynamics):
	'''
	Cross compound turbine governor model.

	:mwbase: Base for power values (MWbase) (>0).  Unit = MW. Default: 
	:pmaxhp: Maximum HP value position (Pmaxhp).  Typical Value = 1. Default: 
	:rhp: HP governor droop (Rhp).  Typical Value = 0.05. Default: 
	:t1hp: HP governor time constant (T1hp).  Typical Value = 0.1. Default: 
	:t3hp: HP turbine time constant (T3hp).  Typical Value = 0.1. Default: 
	:t4hp: HP turbine time constant (T4hp).  Typical Value = 0.1. Default: 
	:t5hp: HP reheater time constant (T5hp).  Typical Value = 10. Default: 
	:fhp: Fraction of HP power ahead of reheater (Fhp).  Typical Value = 0.3. Default: 
	:dhp: HP damping factor (Dhp).  Typical Value = 0. Default: 
	:pmaxlp: Maximum LP value position (Pmaxlp).  Typical Value = 1. Default: 
	:rlp: LP governor droop (Rlp).  Typical Value = 0.05. Default: 
	:t1lp: LP governor time constant (T1lp).  Typical Value = 0.1. Default: 
	:t3lp: LP turbine time constant (T3lp).  Typical Value = 0.1. Default: 
	:t4lp: LP turbine time constant (T4lp).  Typical Value = 0.1. Default: 
	:t5lp: LP reheater time constant (T5lp).  Typical Value = 10. Default: 
	:flp: Fraction of LP power ahead of reheater (Flp).  Typical Value = 0.7. Default: 
	:dlp: LP damping factor (Dlp).  Typical Value = 0. Default: 
		'''

	cgmesProfile = TurbineGovernorDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'mwbase': [cgmesProfile.DY.value, ],
						'pmaxhp': [cgmesProfile.DY.value, ],
						'rhp': [cgmesProfile.DY.value, ],
						't1hp': [cgmesProfile.DY.value, ],
						't3hp': [cgmesProfile.DY.value, ],
						't4hp': [cgmesProfile.DY.value, ],
						't5hp': [cgmesProfile.DY.value, ],
						'fhp': [cgmesProfile.DY.value, ],
						'dhp': [cgmesProfile.DY.value, ],
						'pmaxlp': [cgmesProfile.DY.value, ],
						'rlp': [cgmesProfile.DY.value, ],
						't1lp': [cgmesProfile.DY.value, ],
						't3lp': [cgmesProfile.DY.value, ],
						't4lp': [cgmesProfile.DY.value, ],
						't5lp': [cgmesProfile.DY.value, ],
						'flp': [cgmesProfile.DY.value, ],
						'dlp': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = , pmaxhp = , rhp = , t1hp = , t3hp = , t4hp = , t5hp = , fhp = , dhp = , pmaxlp = , rlp = , t1lp = , t3lp = , t4lp = , t5lp = , flp = , dlp = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mwbase = mwbase
		self.pmaxhp = pmaxhp
		self.rhp = rhp
		self.t1hp = t1hp
		self.t3hp = t3hp
		self.t4hp = t4hp
		self.t5hp = t5hp
		self.fhp = fhp
		self.dhp = dhp
		self.pmaxlp = pmaxlp
		self.rlp = rlp
		self.t1lp = t1lp
		self.t3lp = t3lp
		self.t4lp = t4lp
		self.t5lp = t5lp
		self.flp = flp
		self.dlp = dlp
		
	def __str__(self):
		str = 'class=GovSteamCC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
