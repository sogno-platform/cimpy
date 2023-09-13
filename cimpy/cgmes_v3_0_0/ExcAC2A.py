from .ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAC2A(ExcitationSystemDynamics):
	'''
	Modified IEEE AC2A alternator-supplied rectifier excitation system with different field current limit.

	:tb: Voltage regulator time constant (<i>Tb</i>) (&gt;= 0).  Typical value = 0. Default: 0
	:tc: Voltage regulator time constant (<i>Tc</i>) (&gt;= 0).  Typical value = 0. Default: 0
	:ka: Voltage regulator gain (<i>Ka</i>) (&gt; 0).  Typical value = 400. Default: 0.0
	:ta: Voltage regulator time constant (<i>Ta</i>) (&gt; 0).  Typical value = 0,02. Default: 0
	:vamax: Maximum voltage regulator output (<i>Vamax</i>) (&gt; 0).  Typical value = 8. Default: 0.0
	:vamin: Minimum voltage regulator output (<i>Vamin</i>) (&lt; 0).  Typical value = -8. Default: 0.0
	:kb: Second stage regulator gain (<i>Kb</i>) (&gt; 0).  Exciter field current controller gain.  Typical value = 25. Default: 0.0
	:kb1: Second stage regulator gain (<i>Kb1</i>). It is exciter field current controller gain used as alternative to <i>Kb</i> to represent a variant of the ExcAC2A model.  Typical value = 25. Default: 0.0
	:vrmax: Maximum voltage regulator outputs (<i>Vrmax</i>) (&gt; 0).  Typical value = 105. Default: 0.0
	:vrmin: Minimum voltage regulator outputs (<i>Vrmin</i>) (&lt; 0).  Typical value = -95. Default: 0.0
	:te: Exciter time constant, integration rate associated with exciter control (<i>Te</i>) (&gt; 0).  Typical value = 0,6. Default: 0
	:vfemax: Exciter field current limit reference (<i>Vfemax</i>) (&gt;= 0).  Typical value = 4,4. Default: 0.0
	:kh: Exciter field current feedback gain (<i>Kh</i>) (&gt;= 0).  Typical value = 1. Default: 0.0
	:kf: Excitation control system stabilizer gains (<i>Kf</i>) (&gt;= 0).  Typical value = 0,03. Default: 0.0
	:kl: Exciter field current limiter gain (<i>Kl</i>).  Typical value = 10. Default: 0.0
	:vlr: Maximum exciter field current (<i>Vlr</i>) (&gt; 0).  Typical value = 4,4. Default: 0.0
	:kl1: Coefficient to allow different usage of the model (<i>Kl1</i>).  Typical value = 1. Default: 0.0
	:ks: Coefficient to allow different usage of the model-speed coefficient (<i>Ks</i>) (&gt;= 0).  Typical value = 0. Default: 0.0
	:tf: Excitation control system stabilizer time constant (<i>Tf</i>) (&gt; 0).  Typical value = 1. Default: 0
	:kc: Rectifier loading factor proportional to commutating reactance (<i>Kc</i>) (&gt;= 0).  Typical value = 0,28. Default: 0.0
	:kd: Demagnetizing factor, a function of exciter alternator reactances (<i>Kd</i>) (&gt;= 0).  Typical value = 0,35. Default: 0.0
	:ke: Exciter constant related to self-excited field (<i>Ke</i>).  Typical value = 1. Default: 0.0
	:ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (<i>Ve</i><i><sub>1</sub></i>) (&gt; 0).  Typical value = 4,4. Default: 0.0
	:seve1: Exciter saturation function value at the corresponding exciter voltage, <i>Ve</i><i><sub>1</sub></i>, back of commutating reactance (<i>Se[Ve</i><i><sub>1</sub></i><i>]</i>) (&gt;= 0).  Typical value = 0,037. Default: 0.0
	:ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (<i>Ve</i><i><sub>2</sub></i>) (&gt; 0).  Typical value = 3,3. Default: 0.0
	:seve2: Exciter saturation function value at the corresponding exciter voltage, <i>Ve</i><i><sub>2</sub></i>, back of commutating reactance (<i>Se[Ve</i><i><sub>2</sub></i><i>]</i>) (&gt;= 0).  Typical value = 0,012. Default: 0.0
	:hvgate: Indicates if HV gate is active (<i>HVgate</i>). true = gate is used false = gate is not used. Typical value = true. Default: False
	:lvgate: Indicates if LV gate is active (<i>LVgate</i>). true = gate is used false = gate is not used. Typical value = true. Default: False
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
						'kb1': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'vfemax': [cgmesProfile.DY.value, ],
						'kh': [cgmesProfile.DY.value, ],
						'kf': [cgmesProfile.DY.value, ],
						'kl': [cgmesProfile.DY.value, ],
						'vlr': [cgmesProfile.DY.value, ],
						'kl1': [cgmesProfile.DY.value, ],
						'ks': [cgmesProfile.DY.value, ],
						'tf': [cgmesProfile.DY.value, ],
						'kc': [cgmesProfile.DY.value, ],
						'kd': [cgmesProfile.DY.value, ],
						'ke': [cgmesProfile.DY.value, ],
						've1': [cgmesProfile.DY.value, ],
						'seve1': [cgmesProfile.DY.value, ],
						've2': [cgmesProfile.DY.value, ],
						'seve2': [cgmesProfile.DY.value, ],
						'hvgate': [cgmesProfile.DY.value, ],
						'lvgate': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, tb = 0, tc = 0, ka = 0.0, ta = 0, vamax = 0.0, vamin = 0.0, kb = 0.0, kb1 = 0.0, vrmax = 0.0, vrmin = 0.0, te = 0, vfemax = 0.0, kh = 0.0, kf = 0.0, kl = 0.0, vlr = 0.0, kl1 = 0.0, ks = 0.0, tf = 0, kc = 0.0, kd = 0.0, ke = 0.0, ve1 = 0.0, seve1 = 0.0, ve2 = 0.0, seve2 = 0.0, hvgate = False, lvgate = False,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.tb = tb
		self.tc = tc
		self.ka = ka
		self.ta = ta
		self.vamax = vamax
		self.vamin = vamin
		self.kb = kb
		self.kb1 = kb1
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.te = te
		self.vfemax = vfemax
		self.kh = kh
		self.kf = kf
		self.kl = kl
		self.vlr = vlr
		self.kl1 = kl1
		self.ks = ks
		self.tf = tf
		self.kc = kc
		self.kd = kd
		self.ke = ke
		self.ve1 = ve1
		self.seve1 = seve1
		self.ve2 = ve2
		self.seve2 = seve2
		self.hvgate = hvgate
		self.lvgate = lvgate
		
	def __str__(self):
		str = 'class=ExcAC2A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
