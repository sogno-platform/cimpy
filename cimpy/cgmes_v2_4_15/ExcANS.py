from cimpy.cgmes_v2_4_15.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcANS(ExcitationSystemDynamics):
	'''
	Italian excitation system. It represents static field voltage or excitation current feedback excitation system.

	:k3: AVR gain (K).  Typical Value = 1000. Default: 
	:k2: Exciter gain (K).  Typical Value = 20. Default: 
	:kce: Ceiling factor (K).  Typical Value = 1. Default: 
	:t3: Time constant (T).  Typical Value = 1.6. Default: 
	:t2: Time constant (T).  Typical Value = 0.05. Default: 
	:t1: Time constant (T).  Typical Value = 20. Default: 
	:blint: Governor Control Flag (BLINT).  0 = lead-lag regulator 1 = proportional integral regulator. Typical Value = 0. Default: 
	:kvfif: Rate feedback signal flag (K).  0 = output voltage of the exciter 1 = exciter field current. Typical Value = 0. Default: 
	:ifmn: Minimum exciter current (I).  Typical Value = -5.2. Default: 
	:ifmx: Maximum exciter current (I).  Typical Value = 6.5. Default: 
	:vrmn: Maximum AVR output (V).  Typical Value = -5.2. Default: 
	:vrmx: Minimum AVR output (V).  Typical Value = 6.5. Default: 
	:krvecc: Feedback enabling (K).  0 = Open loop control 1 = Closed loop control. Typical Value = 1. Default: 
	:tb: Exciter time constant (T).  Typical Value = 0.04. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'k3': [cgmesProfile.DY.value, ],
						'k2': [cgmesProfile.DY.value, ],
						'kce': [cgmesProfile.DY.value, ],
						't3': [cgmesProfile.DY.value, ],
						't2': [cgmesProfile.DY.value, ],
						't1': [cgmesProfile.DY.value, ],
						'blint': [cgmesProfile.DY.value, ],
						'kvfif': [cgmesProfile.DY.value, ],
						'ifmn': [cgmesProfile.DY.value, ],
						'ifmx': [cgmesProfile.DY.value, ],
						'vrmn': [cgmesProfile.DY.value, ],
						'vrmx': [cgmesProfile.DY.value, ],
						'krvecc': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, k3 = , k2 = , kce = , t3 = , t2 = , t1 = , blint = , kvfif = , ifmn = , ifmx = , vrmn = , vrmx = , krvecc = , tb = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.k3 = k3
		self.k2 = k2
		self.kce = kce
		self.t3 = t3
		self.t2 = t2
		self.t1 = t1
		self.blint = blint
		self.kvfif = kvfif
		self.ifmn = ifmn
		self.ifmx = ifmx
		self.vrmn = vrmn
		self.vrmx = vrmx
		self.krvecc = krvecc
		self.tb = tb
		
	def __str__(self):
		str = 'class=ExcANS\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
