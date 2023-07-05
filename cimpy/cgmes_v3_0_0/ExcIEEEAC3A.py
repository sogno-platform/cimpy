from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEAC3A(ExcitationSystemDynamics):
	'''
	IEEE 421.5-2005 type AC3A model. The model represents the field-controlled alternator-rectifier excitation systems designated type AC3A. These excitation systems include an alternator main exciter with non-controlled rectifiers. The exciter employs self-excitation, and the voltage regulator power is derived from the exciter output voltage.  Therefore, this system has an additional nonlinearity, simulated by the use of a multiplier whose inputs are the voltage regulator command signal, <i>Va</i>, and the exciter output voltage, <i>Efd</i>, times <i>K</i><i><sub>R</sub></i>.  This model is applicable to excitation systems employing static voltage regulators. Reference: IEEE 421.5-2005, 6.3.

	:tb: Voltage regulator time constant (<i>T</i><i><sub>B</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
	:tc: Voltage regulator time constant (<i>T</i><i><sub>C</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
	:ka: Voltage regulator gain (<i>K</i><i><sub>A</sub></i>) (&gt; 0).  Typical value = 45,62. Default: 0.0
	:ta: Voltage regulator time constant (<i>T</i><i><sub>A</sub></i>) (&gt; 0).  Typical value = 0,013. Default: 0
	:vamax: Maximum voltage regulator output (<i>V</i><i><sub>AMAX</sub></i>) (&gt; 0).  Typical value = 1. Default: 0.0
	:vamin: Minimum voltage regulator output (<i>V</i><i><sub>AMIN</sub></i>) (&lt; 0).  Typical value = -0,95. Default: 0.0
	:te: Exciter time constant, integration rate associated with exciter control (<i>T</i><i><sub>E</sub></i>) (&gt; 0).  Typical value = 1,17. Default: 0
	:vemin: Minimum exciter voltage output (<i>V</i><i><sub>EMIN</sub></i>) (&lt;= 0).  Typical value = 0. Default: 0.0
	:kr: Constant associated with regulator and alternator field power supply (<i>K</i><i><sub>R</sub></i>) (&gt; 0).  Typical value = 3,77. Default: 0.0
	:kf: Excitation control system stabilizer gains (<i>K</i><i><sub>F</sub></i>) (&gt;= 0).  Typical value = 0,143. Default: 0.0
	:tf: Excitation control system stabilizer time constant (<i>T</i><i><sub>F</sub></i>) (&gt; 0).  Typical value = 1. Default: 0
	:kn: Excitation control system stabilizer gain (<i>K</i><i><sub>N</sub></i>) (&gt;= 0).  Typical value = 0,05. Default: 0.0
	:efdn: Value of <i>Efd </i>at which feedback gain changes (<i>E</i><i><sub>FDN</sub></i>) (&gt; 0).  Typical value = 2,36. Default: 0.0
	:kc: Rectifier loading factor proportional to commutating reactance (<i>K</i><i><sub>C</sub></i>) (&gt;= 0).  Typical value = 0,104. Default: 0.0
	:kd: Demagnetizing factor, a function of exciter alternator reactances (<i>K</i><i><sub>D</sub></i>) (&gt;= 0).  Typical value = 0,499. Default: 0.0
	:ke: Exciter constant related to self-excited field (<i>K</i><i><sub>E</sub></i>).  Typical value = 1. Default: 0.0
	:vfemax: Exciter field current limit reference (<i>V</i><i><sub>FEMAX</sub></i>) (&gt;= 0).  Typical value = 16. Default: 0.0
	:ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (<i>V</i><i><sub>E1</sub></i>) (&gt; 0).  Typical value = 6,24. Default: 0.0
	:seve1: Exciter saturation function value at the corresponding exciter voltage, <i>V</i><i><sub>E1</sub></i>, back of commutating reactance (<i>S</i><i><sub>E</sub></i><i>[V</i><i><sub>E1</sub></i><i>]</i>) (&gt;= 0).  Typical value = 1,143. Default: 0.0
	:ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (<i>V</i><i><sub>E2</sub></i>) (&gt; 0).  Typical value = 4,68. Default: 0.0
	:seve2: Exciter saturation function value at the corresponding exciter voltage, <i>V</i><i><sub>E2</sub></i>, back of commutating reactance (<i>S</i><i><sub>E</sub></i><i>[V</i><i><sub>E2</sub></i><i>]</i>) (&gt;= 0).  Typical value = 0,1. Default: 0.0
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'vamax': [cgmesProfile.DY.value, ],
						'vamin': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'vemin': [cgmesProfile.DY.value, ],
						'kr': [cgmesProfile.DY.value, ],
						'kf': [cgmesProfile.DY.value, ],
						'tf': [cgmesProfile.DY.value, ],
						'kn': [cgmesProfile.DY.value, ],
						'efdn': [cgmesProfile.DY.value, ],
						'kc': [cgmesProfile.DY.value, ],
						'kd': [cgmesProfile.DY.value, ],
						'ke': [cgmesProfile.DY.value, ],
						'vfemax': [cgmesProfile.DY.value, ],
						've1': [cgmesProfile.DY.value, ],
						'seve1': [cgmesProfile.DY.value, ],
						've2': [cgmesProfile.DY.value, ],
						'seve2': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, tb = 0, tc = 0, ka = 0.0, ta = 0, vamax = 0.0, vamin = 0.0, te = 0, vemin = 0.0, kr = 0.0, kf = 0.0, tf = 0, kn = 0.0, efdn = 0.0, kc = 0.0, kd = 0.0, ke = 0.0, vfemax = 0.0, ve1 = 0.0, seve1 = 0.0, ve2 = 0.0, seve2 = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.tb = tb
		self.tc = tc
		self.ka = ka
		self.ta = ta
		self.vamax = vamax
		self.vamin = vamin
		self.te = te
		self.vemin = vemin
		self.kr = kr
		self.kf = kf
		self.tf = tf
		self.kn = kn
		self.efdn = efdn
		self.kc = kc
		self.kd = kd
		self.ke = ke
		self.vfemax = vfemax
		self.ve1 = ve1
		self.seve1 = seve1
		self.ve2 = ve2
		self.seve2 = seve2
		
	def __str__(self):
		str = 'class=ExcIEEEAC3A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
