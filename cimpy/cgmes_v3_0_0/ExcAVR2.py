from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAVR2(ExcitationSystemDynamics):
	'''
	Italian excitation system corresponding to IEEE (1968) type 2 model. It represents an alternator and rotating diodes and electromechanic voltage regulators.

	:ka: AVR gain (<i>K</i><i><sub>A</sub></i>).  Typical value = 500. Default: 0.0
	:vrmn: Minimum AVR output (<i>V</i><i><sub>RMN</sub></i>).  Typical value = -6. Default: 0.0
	:vrmx: Maximum AVR output (<i>V</i><i><sub>RMX</sub></i>).  Typical value = 7. Default: 0.0
	:ta: AVR time constant (<i>T</i><i><sub>A</sub></i>) (&gt;= 0).  Typical value = 0,02. Default: 0
	:tb: AVR time constant (<i>T</i><i><sub>B</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
	:te: Exciter time constant (<i>T</i><i><sub>E</sub></i>) (&gt;= 0).  Typical value = 1. Default: 0
	:e1: Field voltage value 1 (<i>E</i><i><sub>1</sub></i>).  Typical value = 4,18. Default: 0.0
	:se1: Saturation factor at <i>E</i><i><sub>1</sub></i> (<i>S[E</i><i><sub>1</sub></i><i>]</i>).  Typical value = 0.1. Default: 0.0
	:e2: Field voltage value 2 (<i>E</i><i><sub>2</sub></i>).  Typical value = 3,14. Default: 0.0
	:se2: Saturation factor at <i>E</i><i><sub>2</sub></i> (<i>S[E</i><i><sub>2</sub></i><i>]</i>).  Typical value = 0,03. Default: 0.0
	:kf: Rate feedback gain (<i>K</i><i><sub>F</sub></i>).  Typical value = 0,12. Default: 0.0
	:tf1: Rate feedback time constant (<i>T</i><i><sub>F1</sub></i>) (&gt;= 0).  Typical value = 1. Default: 0
	:tf2: Rate feedback time constant (<i>T</i><i><sub>F2</sub></i>) (&gt;= 0).  Typical value = 1. Default: 0
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'vrmn': [cgmesProfile.DY.value, ],
						'vrmx': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'e1': [cgmesProfile.DY.value, ],
						'se1': [cgmesProfile.DY.value, ],
						'e2': [cgmesProfile.DY.value, ],
						'se2': [cgmesProfile.DY.value, ],
						'kf': [cgmesProfile.DY.value, ],
						'tf1': [cgmesProfile.DY.value, ],
						'tf2': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ka = 0.0, vrmn = 0.0, vrmx = 0.0, ta = 0, tb = 0, te = 0, e1 = 0.0, se1 = 0.0, e2 = 0.0, se2 = 0.0, kf = 0.0, tf1 = 0, tf2 = 0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ka = ka
		self.vrmn = vrmn
		self.vrmx = vrmx
		self.ta = ta
		self.tb = tb
		self.te = te
		self.e1 = e1
		self.se1 = se1
		self.e2 = e2
		self.se2 = se2
		self.kf = kf
		self.tf1 = tf1
		self.tf2 = tf2
		
	def __str__(self):
		str = 'class=ExcAVR2\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
