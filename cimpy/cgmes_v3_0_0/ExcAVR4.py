from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAVR4(ExcitationSystemDynamics):
	'''
	Italian excitation system. It represents a static exciter and electric voltage regulator.

	:ka: AVR gain (<i>K</i><i><sub>A</sub></i>).  Typical value = 300. Default: 0.0
	:vrmn: Minimum AVR output (<i>V</i><i><sub>RMN</sub></i>).  Typical value = 0. Default: 0.0
	:vrmx: Maximum AVR output (<i>V</i><i><sub>RMX</sub></i>).  Typical value = 5. Default: 0.0
	:t1: AVR time constant (<i>T</i><i><sub>1</sub></i>) (&gt;= 0).  Typical value = 4,8. Default: 0
	:t2: AVR time constant (<i>T</i><i><sub>2</sub></i>) (&gt;= 0).  Typical value = 1,5. Default: 0
	:t3: AVR time constant (<i>T</i><i><sub>3</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
	:t4: AVR time constant (<i>T</i><i><sub>4</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
	:ke: Exciter gain (<i>K</i><i><sub>E</sub></i><i>)</i>.  Typical value = 1. Default: 0.0
	:vfmx: Maximum exciter output (<i>V</i><i><sub>FMX</sub></i>).  Typical value = 5. Default: 0.0
	:vfmn: Minimum exciter output (<i>V</i><i><sub>FMN</sub></i>).  Typical value = 0. Default: 0.0
	:kif: Exciter internal reactance (<i>K</i><i><sub>IF</sub></i>).  Typical value = 0. Default: 0.0
	:tif: Exciter current feedback time constant (<i>T</i><i><sub>IF</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
	:t1if: Exciter current feedback time constant (<i>T</i><i><sub>1IF</sub></i>) (&gt;= 0).  Typical value = 60. Default: 0
	:imul: AVR output voltage dependency selector (<i>I</i><i><sub>MUL</sub></i>). true = selector is connected false = selector is not connected. Typical value = true. Default: False
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
						'ke': [cgmesProfile.DY.value, ],
						'vfmx': [cgmesProfile.DY.value, ],
						'vfmn': [cgmesProfile.DY.value, ],
						'kif': [cgmesProfile.DY.value, ],
						'tif': [cgmesProfile.DY.value, ],
						't1if': [cgmesProfile.DY.value, ],
						'imul': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ka = 0.0, vrmn = 0.0, vrmx = 0.0, t1 = 0, t2 = 0, t3 = 0, t4 = 0, ke = 0.0, vfmx = 0.0, vfmn = 0.0, kif = 0.0, tif = 0, t1if = 0, imul = False,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ka = ka
		self.vrmn = vrmn
		self.vrmx = vrmx
		self.t1 = t1
		self.t2 = t2
		self.t3 = t3
		self.t4 = t4
		self.ke = ke
		self.vfmx = vfmx
		self.vfmn = vfmn
		self.kif = kif
		self.tif = tif
		self.t1if = t1if
		self.imul = imul
		
	def __str__(self):
		str = 'class=ExcAVR4\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
