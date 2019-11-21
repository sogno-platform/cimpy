from cimpy.cgmes_v2_4_15_flat.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAC8B(ExcitationSystemDynamics):
	'''
	Modified IEEE AC8B alternator-supplied rectifier excitation system with speed input and input limiter.

	:inlim: Input limiter indicator. true = input limiter Vimax and Vimin is considered false = input limiter Vimax and Vimin is not considered. Typical Value = true. Default: False
	:ka: Voltage regulator gain (Ka).  Typical Value = 1. Default: 0.0
	:kc: Rectifier loading factor proportional to commutating reactance (Kc). Typical Value = 0.55. Default: 0.0
	:kd: Demagnetizing factor, a function of exciter alternator reactances (Kd).  Typical Value = 1.1. Default: 0.0
	:kdr: Voltage regulator derivative gain (Kdr).  Typical Value = 10. Default: 0.0
	:ke: Exciter constant related to self-excited field (Ke).  Typical Value = 1. Default: 0.0
	:kir: Voltage regulator integral gain (Kir).  Typical Value = 5. Default: 0.0
	:kpr: Voltage regulator proportional gain (Kpr).  Typical Value = 80. Default: 0.0
	:ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0. Default: 0.0
	:pidlim: PID limiter indicator. true = input limiter Vpidmax and Vpidmin is considered false = input limiter Vpidmax and Vpidmin is not considered. Typical Value = true. Default: False
	:seve1: Exciter saturation function value at the corresponding exciter voltage, Ve, back of commutating reactance (Se[Ve1]).  Typical Value = 0.3. Default: 0.0
	:seve2: Exciter saturation function value at the corresponding exciter voltage, Ve, back of commutating reactance (Se[Ve2]).  Typical Value = 3. Default: 0.0
	:ta: Voltage regulator time constant (Ta).  Typical Value = 0. Default: 0.0
	:tdr: Lag time constant (Tdr).  Typical Value = 0.1. Default: 0.0
	:te: Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 1.2. Default: 0.0
	:telim: Selector for the limiter on the block [1/sTe].  See diagram for meaning of true and false. Typical Value = false. Default: False
	:ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve) equals V (Ve1).  Typical Value = 6.5. Default: 0.0
	:ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve).  Typical Value = 9. Default: 0.0
	:vemin: Minimum exciter voltage output (Vemin).  Typical Value = 0. Default: 0.0
	:vfemax: Exciter field current limit reference (Vfemax).  Typical Value = 6. Default: 0.0
	:vimax: Input signal maximum (Vimax).  Typical Value = 35. Default: 0.0
	:vimin: Input signal minimum (Vimin).  Typical Value = -10. Default: 0.0
	:vpidmax: PID maximum controller output (Vpidmax).  Typical Value = 35. Default: 0.0
	:vpidmin: PID minimum controller output (Vpidmin).  Typical Value = -10. Default: 0.0
	:vrmax: Maximum voltage regulator output (Vrmax). Typical Value = 35. Default: 0.0
	:vrmin: Minimum voltage regulator output (Vrmin).  Typical Value = 0. Default: 0.0
	:vtmult: Multiply by generator's terminal voltage indicator. true =the limits Vrmax and Vrmin are multiplied by the generator's terminal voltage to represent a thyristor power stage fed from the generator terminals false = limits are not multiplied by generator's terminal voltage.  Typical Value = false. Default: False
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'inlim': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'kc': [cgmesProfile.DY.value, ],
						'kd': [cgmesProfile.DY.value, ],
						'kdr': [cgmesProfile.DY.value, ],
						'ke': [cgmesProfile.DY.value, ],
						'kir': [cgmesProfile.DY.value, ],
						'kpr': [cgmesProfile.DY.value, ],
						'ks': [cgmesProfile.DY.value, ],
						'pidlim': [cgmesProfile.DY.value, ],
						'seve1': [cgmesProfile.DY.value, ],
						'seve2': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'tdr': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'telim': [cgmesProfile.DY.value, ],
						've1': [cgmesProfile.DY.value, ],
						've2': [cgmesProfile.DY.value, ],
						'vemin': [cgmesProfile.DY.value, ],
						'vfemax': [cgmesProfile.DY.value, ],
						'vimax': [cgmesProfile.DY.value, ],
						'vimin': [cgmesProfile.DY.value, ],
						'vpidmax': [cgmesProfile.DY.value, ],
						'vpidmin': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'vtmult': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, inlim = False, ka = 0.0, kc = 0.0, kd = 0.0, kdr = 0.0, ke = 0.0, kir = 0.0, kpr = 0.0, ks = 0.0, pidlim = False, seve1 = 0.0, seve2 = 0.0, ta = 0.0, tdr = 0.0, te = 0.0, telim = False, ve1 = 0.0, ve2 = 0.0, vemin = 0.0, vfemax = 0.0, vimax = 0.0, vimin = 0.0, vpidmax = 0.0, vpidmin = 0.0, vrmax = 0.0, vrmin = 0.0, vtmult = False,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.inlim = inlim
		self.ka = ka
		self.kc = kc
		self.kd = kd
		self.kdr = kdr
		self.ke = ke
		self.kir = kir
		self.kpr = kpr
		self.ks = ks
		self.pidlim = pidlim
		self.seve1 = seve1
		self.seve2 = seve2
		self.ta = ta
		self.tdr = tdr
		self.te = te
		self.telim = telim
		self.ve1 = ve1
		self.ve2 = ve2
		self.vemin = vemin
		self.vfemax = vfemax
		self.vimax = vimax
		self.vimin = vimin
		self.vpidmax = vpidmax
		self.vpidmin = vpidmin
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.vtmult = vtmult
		
	def __str__(self):
		str = 'class=ExcAC8B\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
