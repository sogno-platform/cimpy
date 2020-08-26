from cimpy.output.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAVR3(ExcitationSystemDynamics):
	'''
	Italian excitation system. It represents exciter dynamo and electric regulator.

	:ka: AVR gain (K).  Typical Value = 3000. Default: 
	:vrmn: Maximum AVR output (V).  Typical Value = -7.5. Default: 
	:vrmx: Minimum AVR output (V).  Typical Value = 7.5. Default: 
	:t1: AVR time constant (T).  Typical Value = 220. Default: 
	:t2: AVR time constant (T).  Typical Value = 1.6. Default: 
	:t3: AVR time constant (T).  Typical Value = 0.66. Default: 
	:t4: AVR time constant (T).  Typical Value = 0.07. Default: 
	:te: Exciter time constant (T).  Typical Value = 1. Default: 
	:e1: Field voltage value 1 (E1).  Typical Value = 4.18. Default: 
	:se1: Saturation factor at E1 (S(E1)).  Typical Value = 0.1. Default: 
	:e2: Field voltage value 2 (E2).  Typical Value = 3.14. Default: 
	:se2: Saturation factor at E2 (S(E2)).  Typical Value = 0.03. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ka': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmn': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmx': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't4': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'te': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'e1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'se1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'e2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'se2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ka = , vrmn = , vrmx = , t1 = , t2 = , t3 = , t4 = , te = , e1 = , se1 = , e2 = , se2 = ,  *args, **kw_args):
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
