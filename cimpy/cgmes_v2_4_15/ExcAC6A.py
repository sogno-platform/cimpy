from cimpy.output.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAC6A(ExcitationSystemDynamics):
	'''
	Modified IEEE AC6A alternator-supplied rectifier excitation system with speed input.

	:ka: Voltage regulator gain (Ka).  Typical Value = 536. Default: 
	:ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0. Default: 
	:ta: Voltage regulator time constant (Ta).  Typical Value = 0.086. Default: 
	:tk: Voltage regulator time constant (Tk).  Typical Value = 0.18. Default: 
	:tb: Voltage regulator time constant (Tb).  Typical Value = 9. Default: 
	:tc: Voltage regulator time constant (Tc).  Typical Value = 3. Default: 
	:vamax: Maximum voltage regulator output (Vamax).  Typical Value = 75. Default: 
	:vamin: Minimum voltage regulator output (Vamin).  Typical Value = -75. Default: 
	:vrmax: Maximum voltage regulator output (Vrmax).  Typical Value = 44. Default: 
	:vrmin: Minimum voltage regulator output (Vrmin).  Typical Value = -36. Default: 
	:te: Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 1. Default: 
	:kh: Exciter field current limiter gain (Kh).  Typical Value = 92. Default: 
	:tj: Exciter field current limiter time constant (Tj).  Typical Value = 0.02. Default: 
	:th: Exciter field current limiter time constant (Th).  Typical Value = 0.08. Default: 
	:vfelim: Exciter field current limit reference (Vfelim).  Typical Value = 19. Default: 
	:vhmax: Maximum field current limiter signal reference (Vhmax).  Typical Value = 75. Default: 
	:kc: Rectifier loading factor proportional to commutating reactance (Kc).  Typical Value = 0.173. Default: 
	:kd: Demagnetizing factor, a function of exciter alternator reactances (Kd).  Typical Value = 1.91. Default: 
	:ke: Exciter constant related to self-excited field (Ke).  Typical Value = 1.6. Default: 
	:ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve).  Typical Value = 7.4. Default: 
	:seve1: Exciter saturation function value at the corresponding exciter voltage, Ve1, back of commutating reactance (Se[Ve1]).  Typical Value = 0.214. Default: 
	:ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve2).  Typical Value = 5.55. Default: 
	:seve2: Exciter saturation function value at the corresponding exciter voltage, Ve2, back of commutating reactance (Se[Ve2]).  Typical Value = 0.044. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'ks': [cgmesProfile.DY.value, ],
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

	def __init__(self, ka = , ks = , ta = , tk = , tb = , tc = , vamax = , vamin = , vrmax = , vrmin = , te = , kh = , tj = , th = , vfelim = , vhmax = , kc = , kd = , ke = , ve1 = , seve1 = , ve2 = , seve2 = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ka = ka
		self.ks = ks
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
		str = 'class=ExcAC6A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
