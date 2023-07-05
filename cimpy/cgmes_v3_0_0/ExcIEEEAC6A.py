from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEAC6A(ExcitationSystemDynamics):
	'''
	IEEE 421.5-2005 type AC6A model. The model represents field-controlled alternator-rectifier excitation systems with system-supplied electronic voltage regulators.  The maximum output of the regulator, <i>V</i><i><sub>R</sub></i>, is a function of terminal voltage, <i>V</i><i><sub>T</sub></i>. The field current limiter included in the original model AC6A remains in the 2005 update. Reference: IEEE 421.5-2005, 6.6.

	:ka: Voltage regulator gain (<i>K</i><i><sub>A</sub></i>) (&gt; 0).  Typical value = 536. Default: 0.0
	:ta: Voltage regulator time constant (<i>T</i><i><sub>A</sub></i>) (&gt;= 0).  Typical value = 0,086. Default: 0
	:tk: Voltage regulator time constant (<i>T</i><i><sub>K</sub></i>) (&gt;= 0).  Typical value = 0,18. Default: 0
	:tb: Voltage regulator time constant (<i>T</i><i><sub>B</sub></i>) (&gt;= 0).  Typical value = 9. Default: 0
	:tc: Voltage regulator time constant (<i>T</i><i><sub>C</sub></i>) (&gt;= 0).  Typical value = 3. Default: 0
	:vamax: Maximum voltage regulator output (<i>V</i><i><sub>AMAX</sub></i>) (&gt; 0).  Typical value = 75. Default: 0.0
	:vamin: Minimum voltage regulator output (V<sub>AMIN</sub>) (&lt; 0).  Typical value = -75. Default: 0.0
	:vrmax: Maximum voltage regulator output (<i>V</i><i><sub>RMAX</sub></i>) (&gt; 0).  Typical value = 44. Default: 0.0
	:vrmin: Minimum voltage regulator output (<i>V</i><i><sub>RMIN</sub></i>) (&lt; 0).  Typical value = -36. Default: 0.0
	:te: Exciter time constant, integration rate associated with exciter control (<i>T</i><i><sub>E</sub></i>) (&gt; 0).  Typical value = 1. Default: 0
	:kh: Exciter field current limiter gain (<i>K</i><i><sub>H</sub></i>) (&gt;= 0).  Typical value = 92. Default: 0.0
	:tj: Exciter field current limiter time constant (<i>T</i><i><sub>J</sub></i>) (&gt;= 0).  Typical value = 0,02. Default: 0
	:th: Exciter field current limiter time constant (<i>T</i><i><sub>H</sub></i>) (&gt; 0).  Typical value = 0,08. Default: 0
	:vfelim: Exciter field current limit reference (<i>V</i><i><sub>FELIM</sub></i>) (&gt; 0).  Typical value = 19. Default: 0.0
	:vhmax: Maximum field current limiter signal reference (<i>V</i><i><sub>HMAX</sub></i>) (&gt; 0).  Typical value = 75. Default: 0.0
	:kc: Rectifier loading factor proportional to commutating reactance (<i>K</i><i><sub>C</sub></i>) (&gt;= 0). Typical value = 0,173. Default: 0.0
	:kd: Demagnetizing factor, a function of exciter alternator reactances (<i>K</i><i><sub>D</sub></i>) (&gt;= 0).  Typical value = 1,91. Default: 0.0
	:ke: Exciter constant related to self-excited field (<i>K</i><i><sub>E</sub></i>).  Typical value = 1,6. Default: 0.0
	:ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (<i>V</i><i><sub>E1</sub></i>) (&gt; 0).  Typical value = 7,4. Default: 0.0
	:seve1: Exciter saturation function value at the corresponding exciter voltage, <i>V</i><i><sub>E1</sub></i>, back of commutating reactance (<i>S</i><i><sub>E</sub></i><i>[V</i><i><sub>E1</sub></i><i>])</i> (&gt;= 0).  Typical value = 0,214. Default: 0.0
	:ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (<i>V</i><i><sub>E2</sub></i>) (&gt; 0).  Typical value = 5,55. Default: 0.0
	:seve2: Exciter saturation function value at the corresponding exciter voltage, <i>V</i><i><sub>E2</sub></i>, back of commutating reactance (<i>S</i><i><sub>E</sub></i><i>[V</i><i><sub>E2</sub></i><i>]</i>) (&gt;= 0).  Typical value = 0,044. Default: 0.0
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'tk': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						'vamax': [cgmesProfile.DY.value, ],
						'vamin': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'kh': [cgmesProfile.DY.value, ],
						'tj': [cgmesProfile.DY.value, ],
						'th': [cgmesProfile.DY.value, ],
						'vfelim': [cgmesProfile.DY.value, ],
						'vhmax': [cgmesProfile.DY.value, ],
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

	def __init__(self, ka = 0.0, ta = 0, tk = 0, tb = 0, tc = 0, vamax = 0.0, vamin = 0.0, vrmax = 0.0, vrmin = 0.0, te = 0, kh = 0.0, tj = 0, th = 0, vfelim = 0.0, vhmax = 0.0, kc = 0.0, kd = 0.0, ke = 0.0, ve1 = 0.0, seve1 = 0.0, ve2 = 0.0, seve2 = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ka = ka
		self.ta = ta
		self.tk = tk
		self.tb = tb
		self.tc = tc
		self.vamax = vamax
		self.vamin = vamin
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.te = te
		self.kh = kh
		self.tj = tj
		self.th = th
		self.vfelim = vfelim
		self.vhmax = vhmax
		self.kc = kc
		self.kd = kd
		self.ke = ke
		self.ve1 = ve1
		self.seve1 = seve1
		self.ve2 = ve2
		self.seve2 = seve2
		
	def __str__(self):
		str = 'class=ExcIEEEAC6A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
