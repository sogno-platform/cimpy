from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcANS(ExcitationSystemDynamics):
	'''
	Italian excitation system. It represents static field voltage or excitation current feedback excitation system.

	:k3: AVR gain (<i>K</i><i><sub>3</sub></i>).  Typical value = 1000. Default: 0.0
	:k2: Exciter gain (<i>K</i><i><sub>2</sub></i>).  Typical value = 20. Default: 0.0
	:kce: Ceiling factor (<i>K</i><i><sub>CE</sub></i>).  Typical value = 1. Default: 0.0
	:t3: Time constant (<i>T</i><i><sub>3</sub></i>) (&gt;= 0).  Typical value = 1,6. Default: 0
	:t2: Time constant (<i>T</i><i><sub>2</sub></i>) (&gt;= 0).  Typical value = 0,05. Default: 0
	:t1: Time constant (<i>T</i><i><sub>1</sub></i>) (&gt;= 0).  Typical value = 20. Default: 0
	:blint: Governor control flag (<i>BLINT</i>).  0 = lead-lag regulator 1 = proportional integral regulator. Typical value = 0. Default: 0
	:kvfif: Rate feedback signal flag (<i>K</i><i><sub>VFIF</sub></i>).  0 = output voltage of the exciter 1 = exciter field current. Typical value = 0. Default: 0
	:ifmn: Minimum exciter current (<i>I</i><i><sub>FMN</sub></i>).  Typical value = -5,2. Default: 0.0
	:ifmx: Maximum exciter current (<i>I</i><i><sub>FMX</sub></i>).  Typical value = 6,5. Default: 0.0
	:vrmn: Minimum AVR output (<i>V</i><i><sub>RMN</sub></i>).  Typical value = -5,2. Default: 0.0
	:vrmx: Maximum AVR output (<i>V</i><i><sub>RMX</sub></i>).  Typical value = 6,5. Default: 0.0
	:krvecc: Feedback enabling (<i>K</i><i><sub>RVECC</sub></i>).  0 = open loop control 1 = closed loop control. Typical value = 1. Default: 0
	:tb: Exciter time constant (<i>T</i><i><sub>B</sub></i>) (&gt;= 0).  Typical value = 0,04. Default: 0
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

	def __init__(self, k3 = 0.0, k2 = 0.0, kce = 0.0, t3 = 0, t2 = 0, t1 = 0, blint = 0, kvfif = 0, ifmn = 0.0, ifmx = 0.0, vrmn = 0.0, vrmx = 0.0, krvecc = 0, tb = 0,  *args, **kw_args):
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
