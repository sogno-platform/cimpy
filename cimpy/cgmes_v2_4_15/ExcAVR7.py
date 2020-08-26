from cimpy.cgmes_v2_4_15.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAVR7(ExcitationSystemDynamics):
	'''
	IVO excitation system.

	:k1: Gain (K1).  Typical Value = 1. Default: 
	:a1: Lead coefficient (A1).  Typical Value = 0.5. Default: 
	:a2: Lag coefficient (A2).  Typical Value = 0.5. Default: 
	:t1: Lead time constant (T1).  Typical Value = 0.05. Default: 
	:t2: Lag time constant (T2).  Typical Value = 0.1. Default: 
	:vmax1: Lead-lag max. limit (Vmax1).  Typical Value = 5. Default: 
	:vmin1: Lead-lag min. limit (Vmin1).  Typical Value = -5. Default: 
	:k3: Gain (K3).  Typical Value = 3. Default: 
	:a3: Lead coefficient (A3).  Typical Value = 0.5. Default: 
	:a4: Lag coefficient (A4).  Typical Value = 0.5. Default: 
	:t3: Lead time constant (T3).  Typical Value = 0.1. Default: 
	:t4: Lag time constant (T4).  Typical Value = 0.1. Default: 
	:vmax3: Lead-lag max. limit (Vmax3).  Typical Value = 5. Default: 
	:vmin3: Lead-lag min. limit (Vmin3).  Typical Value = -5. Default: 
	:k5: Gain (K5).  Typical Value = 1. Default: 
	:a5: Lead coefficient (A5).  Typical Value = 0.5. Default: 
	:a6: Lag coefficient (A6).  Typical Value = 0.5. Default: 
	:t5: Lead time constant (T5).  Typical Value = 0.1. Default: 
	:t6: Lag time constant (T6).  Typical Value = 0.1. Default: 
	:vmax5: Lead-lag max. limit (Vmax5).  Typical Value = 5. Default: 
	:vmin5: Lead-lag min. limit (Vmin5).  Typical Value = -2. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'k1': [cgmesProfile.DY.value, ],
						'a1': [cgmesProfile.DY.value, ],
						'a2': [cgmesProfile.DY.value, ],
						't1': [cgmesProfile.DY.value, ],
						't2': [cgmesProfile.DY.value, ],
						'vmax1': [cgmesProfile.DY.value, ],
						'vmin1': [cgmesProfile.DY.value, ],
						'k3': [cgmesProfile.DY.value, ],
						'a3': [cgmesProfile.DY.value, ],
						'a4': [cgmesProfile.DY.value, ],
						't3': [cgmesProfile.DY.value, ],
						't4': [cgmesProfile.DY.value, ],
						'vmax3': [cgmesProfile.DY.value, ],
						'vmin3': [cgmesProfile.DY.value, ],
						'k5': [cgmesProfile.DY.value, ],
						'a5': [cgmesProfile.DY.value, ],
						'a6': [cgmesProfile.DY.value, ],
						't5': [cgmesProfile.DY.value, ],
						't6': [cgmesProfile.DY.value, ],
						'vmax5': [cgmesProfile.DY.value, ],
						'vmin5': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, k1 = , a1 = , a2 = , t1 = , t2 = , vmax1 = , vmin1 = , k3 = , a3 = , a4 = , t3 = , t4 = , vmax3 = , vmin3 = , k5 = , a5 = , a6 = , t5 = , t6 = , vmax5 = , vmin5 = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.k1 = k1
		self.a1 = a1
		self.a2 = a2
		self.t1 = t1
		self.t2 = t2
		self.vmax1 = vmax1
		self.vmin1 = vmin1
		self.k3 = k3
		self.a3 = a3
		self.a4 = a4
		self.t3 = t3
		self.t4 = t4
		self.vmax3 = vmax3
		self.vmin3 = vmin3
		self.k5 = k5
		self.a5 = a5
		self.a6 = a6
		self.t5 = t5
		self.t6 = t6
		self.vmax5 = vmax5
		self.vmin5 = vmin5
		
	def __str__(self):
		str = 'class=ExcAVR7\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
