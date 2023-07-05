from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEAC2A(ExcitationSystemDynamics):
	'''
	IEEE 421.5-2005 type AC2A model. The model represents a high initial response field-controlled alternator-rectifier excitation system. The alternator main exciter is used with non-controlled rectifiers. The type AC2A model is similar to that of type AC1A except for the inclusion of exciter time constant compensation and exciter field current limiting elements. Reference: IEEE 421.5-2005, 6.2.

	:tb: Voltage regulator time constant (<i>T</i><i><sub>B</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
	:tc: Voltage regulator time constant (<i>T</i><i><sub>C</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
	:ka: Voltage regulator gain (<i>K</i><i><sub>A</sub></i>) (&gt; 0).  Typical value = 400. Default: 0.0
	:ta: Voltage regulator time constant (<i>T</i><i><sub>A</sub></i>) (&gt; 0).  Typical value = 0,02. Default: 0
	:vamax: Maximum voltage regulator output (<i>V</i><i><sub>AMAX</sub></i>) (&gt; 0).  Typical value = 8. Default: 0.0
	:vamin: Minimum voltage regulator output (<i>V</i><i><sub>AMIN</sub></i>) (&lt; 0).  Typical value = -8. Default: 0.0
	:kb: Second stage regulator gain (<i>K</i><i><sub>B</sub></i>) (&gt; 0).  Typical value = 25. Default: 0.0
	:vrmax: Maximum voltage regulator outputs (<i>V</i><i><sub>RMAX</sub></i>) (&gt; 0).  Typical value = 105. Default: 0.0
	:vrmin: Minimum voltage regulator outputs (<i>V</i><i><sub>RMIN</sub></i>) (&lt; 0).  Typical value = -95. Default: 0.0
	:te: Exciter time constant, integration rate associated with exciter control (<i>T</i><i><sub>E</sub></i>) (&gt; 0).  Typical value = 0,6. Default: 0
	:vfemax: Exciter field current limit reference (<i>V</i><i><sub>FEMAX</sub></i>) (&gt; 0).  Typical value = 4,4. Default: 0.0
	:kh: Exciter field current feedback gain (<i>K</i><i><sub>H</sub></i>) (&gt;= 0).  Typical value = 1. Default: 0.0
	:kf: Excitation control system stabilizer gains (<i>K</i><i><sub>F</sub></i>) (&gt;= 0).  Typical value = 0,03. Default: 0.0
	:tf: Excitation control system stabilizer time constant (<i>T</i><i><sub>F</sub></i>) (&gt; 0).  Typical value = 1. Default: 0
	:kc: Rectifier loading factor proportional to commutating reactance (<i>K</i><i><sub>C</sub></i>) (&gt;= 0).  Typical value = 0,28. Default: 0.0
	:kd: Demagnetizing factor, a function of exciter alternator reactances (<i>K</i><i><sub>D</sub></i>) (&gt;= 0).  Typical value = 0,35. Default: 0.0
	:ke: Exciter constant related to self-excited field (<i>K</i><i><sub>E</sub></i>) (&gt;= 0).  Typical value = 1. Default: 0.0
	:ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (<i>V</i><i><sub>E1</sub></i>) (&gt; 0).  Typical value = 4,4. Default: 0.0
	:seve1: Exciter saturation function value at the corresponding exciter voltage, <i>V</i><i><sub>E1</sub></i>, back of commutating reactance (<i>S</i><i><sub>E</sub></i><i>[V</i><i><sub>E1</sub></i><i>]</i>) (&gt;= 0).  Typical value = 0,037. Default: 0.0
	:ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (<i>V</i><i><sub>E2</sub></i>) (&gt; 0).  Typical value = 3,3. Default: 0.0
	:seve2: Exciter saturation function value at the corresponding exciter voltage, <i>V</i><i><sub>E2</sub></i>, back of commutating reactance (<i>S</i><i><sub>E</sub></i><i>[V</i><i><sub>E2</sub></i><i>]</i>) (&gt;= 0).  Typical value = 0,012. Default: 0.0
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'vamax': [cgmesProfile.DY.value, ],
						'vamin': [cgmesProfile.DY.value, ],
						'kb': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'vfemax': [cgmesProfile.DY.value, ],
						'kh': [cgmesProfile.DY.value, ],
						'kf': [cgmesProfile.DY.value, ],
						'tf': [cgmesProfile.DY.value, ],
						'kc': [cgmesProfile.DY.value, ],
						'kd': [cgmesProfile.DY.value, ],
						'ke': [cgmesProfile.DY.value, ],
						've1': [cgmesProfile.DY.value, ],
						'seve1': [cgmesProfile.DY.value, ],
						've2': [cgmesProfile.DY.value, ],
						'seve2': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, tb = 0, tc = 0, ka = 0.0, ta = 0, vamax = 0.0, vamin = 0.0, kb = 0.0, vrmax = 0.0, vrmin = 0.0, te = 0, vfemax = 0.0, kh = 0.0, kf = 0.0, tf = 0, kc = 0.0, kd = 0.0, ke = 0.0, ve1 = 0.0, seve1 = 0.0, ve2 = 0.0, seve2 = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.tb = tb
		self.tc = tc
		self.ka = ka
		self.ta = ta
		self.vamax = vamax
		self.vamin = vamin
		self.kb = kb
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.te = te
		self.vfemax = vfemax
		self.kh = kh
		self.kf = kf
		self.tf = tf
		self.kc = kc
		self.kd = kd
		self.ke = ke
		self.ve1 = ve1
		self.seve1 = seve1
		self.ve2 = ve2
		self.seve2 = seve2
		
	def __str__(self):
		str = 'class=ExcIEEEAC2A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
