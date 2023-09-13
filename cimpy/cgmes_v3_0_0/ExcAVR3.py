from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAVR3(ExcitationSystemDynamics):
	'''
	Italian excitation system. It represents an exciter dynamo and electric regulator.

	:ka: AVR gain (<i>K</i><i><sub>A</sub></i>).  Typical value = 100. Default: 0.0
	:vrmn: Minimum AVR output (<i>V</i><i><sub>RMN</sub></i>).  Typical value = -7,5. Default: 0.0
	:vrmx: Maximum AVR output (<i>V</i><i><sub>RMX</sub></i>).  Typical value = 7,5. Default: 0.0
	:t1: AVR time constant (<i>T</i><i><sub>1</sub></i>) (&gt;= 0).  Typical value = 20. Default: 0
	:t2: AVR time constant (<i>T</i><i><sub>2</sub></i>) (&gt;= 0).  Typical value = 1,6. Default: 0
	:t3: AVR time constant (<i>T</i><i><sub>3</sub></i>) (&gt;= 0).  Typical value = 0,66. Default: 0
	:t4: AVR time constant (<i>T</i><i><sub>4</sub></i>) (&gt;= 0).  Typical value = 0,07. Default: 0
	:te: Exciter time constant (<i>T</i><i><sub>E</sub></i>) (&gt;= 0).  Typical value = 1. Default: 0
	:e1: Field voltage value 1 (<i>E</i><i><sub>1</sub></i>).  Typical value = 4,18. Default: 0.0
	:se1: Saturation factor at <i>E</i><i><sub>1</sub></i><i> </i>(<i>S[E</i><i><sub>1</sub></i><i>]</i>).  Typical value = 0,1. Default: 0.0
	:e2: Field voltage value 2 (<i>E</i><i><sub>2</sub></i>).  Typical value = 3,14. Default: 0.0
	:se2: Saturation factor at <i>E</i><i><sub>2</sub></i><i> </i>(<i>S[E</i><i><sub>2</sub></i><i>]</i>).  Typical value = 0,03. Default: 0.0
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'vrmn': [cgmesProfile.DY.value, ],
						'vrmx': [cgmesProfile.DY.value, ],
						't1': [cgmesProfile.DY.value, ],
						't2': [cgmesProfile.DY.value, ],
						't3': [cgmesProfile.DY.value, ],
						't4': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'e1': [cgmesProfile.DY.value, ],
						'se1': [cgmesProfile.DY.value, ],
						'e2': [cgmesProfile.DY.value, ],
						'se2': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ka = 0.0, vrmn = 0.0, vrmx = 0.0, t1 = 0, t2 = 0, t3 = 0, t4 = 0, te = 0, e1 = 0.0, se1 = 0.0, e2 = 0.0, se2 = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ka = ka
		self.vrmn = vrmn
		self.vrmx = vrmx
		self.t1 = t1
		self.t2 = t2
		self.t3 = t3
		self.t4 = t4
		self.te = te
		self.e1 = e1
		self.se1 = se1
		self.e2 = e2
		self.se2 = se2
		
	def __str__(self):
		str = 'class=ExcAVR3\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
