from cimpy.cgmes_v2_4_15.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAVR4(ExcitationSystemDynamics):
	'''
	Italian excitation system. It represents static exciter and electric voltage regulator.

	:ka: AVR gain (K).  Typical Value = 300. Default: 
	:vrmn: Maximum AVR output (V).  Typical Value = 0. Default: 
	:vrmx: Minimum AVR output (V).  Typical Value = 5. Default: 
	:t1: AVR time constant (T).  Typical Value = 4.8. Default: 
	:t2: AVR time constant (T).  Typical Value = 1.5. Default: 
	:t3: AVR time constant (T).  Typical Value = 0. Default: 
	:t4: AVR time constant (T).  Typical Value = 0. Default: 
	:ke: Exciter gain (K).  Typical Value = 1. Default: 
	:vfmx: Maximum exciter output (V).  Typical Value = 5. Default: 
	:vfmn: Minimum exciter output (V).  Typical Value = 0. Default: 
	:kif: Exciter internal reactance (K).  Typical Value = 0. Default: 
	:tif: Exciter current feedback time constant (T).  Typical Value = 0. Default: 
	:t1if: Exciter current feedback time constant (T).  Typical Value = 60. Default: 
	:imul: AVR output voltage dependency selector (Imul). true = selector is connected false = selector is not connected. Typical Value = true. Default: 
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

	def __init__(self, ka = , vrmn = , vrmx = , t1 = , t2 = , t3 = , t4 = , ke = , vfmx = , vfmn = , kif = , tif = , t1if = , imul = ,  *args, **kw_args):
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
