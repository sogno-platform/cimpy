from cimpy.cgmes_v2_4_15.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class PssELIN2(PowerSystemStabilizerDynamics):
	'''
	Power system stabilizer typically associated with ExcELIN2 (though PssIEEE2B or Pss2B can also be used).

	:ts1: Time constant (Ts1).  Typical Value = 0. Default: 
	:ts2: Time constant (Ts2).  Typical Value = 1. Default: 
	:ts3: Time constant (Ts3).  Typical Value = 1. Default: 
	:ts4: Time constant (Ts4).  Typical Value = 0.1. Default: 
	:ts5: Time constant (Ts5).  Typical Value = 0. Default: 
	:ts6: Time constant (Ts6).  Typical Value = 1. Default: 
	:ks1: Gain (Ks1).  Typical Value = 1. Default: 
	:ks2: Gain (Ks2).  Typical Value = 0.1. Default: 
	:ppss: Coefficient (p_PSS) (>=0 and <=4).  Typical Value = 0.1. Default: 
	:apss: Coefficient (a_PSS).  Typical Value = 0.1. Default: 
	:psslim: PSS limiter (psslim).  Typical Value = 0.1. Default: 
		'''

	cgmesProfile = PowerSystemStabilizerDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'ts1': [cgmesProfile.DY.value, ],
						'ts2': [cgmesProfile.DY.value, ],
						'ts3': [cgmesProfile.DY.value, ],
						'ts4': [cgmesProfile.DY.value, ],
						'ts5': [cgmesProfile.DY.value, ],
						'ts6': [cgmesProfile.DY.value, ],
						'ks1': [cgmesProfile.DY.value, ],
						'ks2': [cgmesProfile.DY.value, ],
						'ppss': [cgmesProfile.DY.value, ],
						'apss': [cgmesProfile.DY.value, ],
						'psslim': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemStabilizerDynamics: \n' + PowerSystemStabilizerDynamics.__doc__ 

	def __init__(self, ts1 = , ts2 = , ts3 = , ts4 = , ts5 = , ts6 = , ks1 = , ks2 = , ppss = , apss = , psslim = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ts1 = ts1
		self.ts2 = ts2
		self.ts3 = ts3
		self.ts4 = ts4
		self.ts5 = ts5
		self.ts6 = ts6
		self.ks1 = ks1
		self.ks2 = ks2
		self.ppss = ppss
		self.apss = apss
		self.psslim = psslim
		
	def __str__(self):
		str = 'class=PssELIN2\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
