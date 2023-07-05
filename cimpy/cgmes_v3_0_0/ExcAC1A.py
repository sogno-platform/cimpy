from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAC1A(ExcitationSystemDynamics):
	'''
	Modified IEEE AC1A alternator-supplied rectifier excitation system with different rate feedback source.

	:tb: Voltage regulator time constant (<i>Tb</i>) (&gt;= 0).  Typical value = 0. Default: 0
	:tc: Voltage regulator time constant (<i>T</i><i><sub>c</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
	:ka: Voltage regulator gain (<i>Ka</i>) (&gt; 0).  Typical value = 400. Default: 0.0
	:ta: Voltage regulator time constant (<i>Ta</i>) (&gt; 0).  Typical value = 0,02. Default: 0
	:vamax: Maximum voltage regulator output (<i>V</i><i><sub>amax</sub></i>) (&gt; 0).  Typical value = 14,5. Default: 0.0
	:vamin: Minimum voltage regulator output (<i>V</i><i><sub>amin</sub></i>) (&lt; 0).  Typical value = -14,5. Default: 0.0
	:te: Exciter time constant, integration rate associated with exciter control (<i>Te</i>) (&gt; 0).  Typical value = 0,8. Default: 0
	:kf: Excitation control system stabilizer gains (<i>Kf</i>) (&gt;= 0).  Typical value = 0,03. Default: 0.0
	:kf1: Coefficient to allow different usage of the model (<i>Kf1</i>) (&gt;= 0).  Typical value = 0. Default: 0.0
	:kf2: Coefficient to allow different usage of the model (<i>Kf2</i>) (&gt;= 0).  Typical value = 1. Default: 0.0
	:ks: Coefficient to allow different usage of the model-speed coefficient (<i>Ks</i>) (&gt;= 0).  Typical value = 0. Default: 0.0
	:tf: Excitation control system stabilizer time constant (<i>Tf</i>) (&gt; 0).  Typical value = 1. Default: 0
	:kc: Rectifier loading factor proportional to commutating reactance (<i>Kc</i>) (&gt;= 0). Typical value = 0,2. Default: 0.0
	:kd: Demagnetizing factor, a function of exciter alternator reactances (<i>Kd</i>) (&gt;= 0).  Typical value = 0,38. Default: 0.0
	:ke: Exciter constant related to self-excited field (<i>Ke</i>).  Typical value = 1. Default: 0.0
	:ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (<i>Ve1</i>) (&gt; 0).  Typical value = 4,18. Default: 0.0
	:seve1: Exciter saturation function value at the corresponding exciter voltage, <i>Ve</i><i><sub>1</sub></i>, back of commutating reactance (<i>Se[Ve</i><i><sub>1</sub></i><i>]</i>) (&gt;= 0).  Typical value = 0,1. Default: 0.0
	:ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (<i>Ve2</i>) (&gt; 0).  Typical value = 3,14. Default: 0.0
	:seve2: Exciter saturation function value at the corresponding exciter voltage, <i>Ve</i><i><sub>2</sub></i>, back of commutating reactance (<i>Se[Ve</i><i><sub>2</sub></i><i>]</i>) (&gt;= 0).  Typical value = 0,03. Default: 0.0
	:vrmax: Maximum voltage regulator outputs (<i>Vrmax</i>) (&gt; 0).  Typical value = 6,03. Default: 0.0
	:vrmin: Minimum voltage regulator outputs (<i>Vrmin</i>) (&lt; 0).  Typical value = -5,43. Default: 0.0
	:hvlvgates: Indicates if both HV gate and LV gate are active (<i>HVLVgates</i>). true = gates are used false = gates are not used. Typical value = true. Default: False
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
						'kf': [cgmesProfile.DY.value, ],
						'kf1': [cgmesProfile.DY.value, ],
						'kf2': [cgmesProfile.DY.value, ],
						'ks': [cgmesProfile.DY.value, ],
						'tf': [cgmesProfile.DY.value, ],
						'kc': [cgmesProfile.DY.value, ],
						'kd': [cgmesProfile.DY.value, ],
						'ke': [cgmesProfile.DY.value, ],
						've1': [cgmesProfile.DY.value, ],
						'seve1': [cgmesProfile.DY.value, ],
						've2': [cgmesProfile.DY.value, ],
						'seve2': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'hvlvgates': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, tb = 0, tc = 0, ka = 0.0, ta = 0, vamax = 0.0, vamin = 0.0, te = 0, kf = 0.0, kf1 = 0.0, kf2 = 0.0, ks = 0.0, tf = 0, kc = 0.0, kd = 0.0, ke = 0.0, ve1 = 0.0, seve1 = 0.0, ve2 = 0.0, seve2 = 0.0, vrmax = 0.0, vrmin = 0.0, hvlvgates = False,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.tb = tb
		self.tc = tc
		self.ka = ka
		self.ta = ta
		self.vamax = vamax
		self.vamin = vamin
		self.te = te
		self.kf = kf
		self.kf1 = kf1
		self.kf2 = kf2
		self.ks = ks
		self.tf = tf
		self.kc = kc
		self.kd = kd
		self.ke = ke
		self.ve1 = ve1
		self.seve1 = seve1
		self.ve2 = ve2
		self.seve2 = seve2
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.hvlvgates = hvlvgates
		
	def __str__(self):
		str = 'class=ExcAC1A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
