from cimpy.cgmes_v2_4_15.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcELIN2(ExcitationSystemDynamics):
	'''
	Detailed Excitation System Model - ELIN (VATECH).  This model represents an all-static excitation system. A PI voltage controller establishes a desired field current set point for a proportional current controller. The integrator of the PI controller has a follow-up input to match its signal to the present field current.  Power system stabilizer models used in conjunction with this excitation system model: PssELIN2, PssIEEE2B, Pss2B.

	:k1: Voltage regulator input gain (K1).  Typical Value = 0. Default: 0.0
	:k1ec: Voltage regulator input limit (K1ec).  Typical Value = 2. Default: 0.0
	:kd1: Voltage controller derivative gain (Kd1).  Typical Value = 34.5. Default: 0.0
	:tb1: Voltage controller derivative washout time constant (Tb1).  Typical Value = 12.45. Default: 0.0
	:pid1max: Controller follow up gain (PID1max).  Typical Value = 2. Default: 0.0
	:ti1: Controller follow up dead band (Ti1).  Typical Value = 0. Default: 0.0
	:iefmax2: Minimum open circuit excitation voltage (Iefmax2).  Typical Value = -5. Default: 0.0
	:k2: Gain (K2).  Typical Value = 5. Default: 0.0
	:ketb: Gain (Ketb).  Typical Value = 0.06. Default: 0.0
	:upmax: Limiter (Upmax).  Typical Value = 3. Default: 0.0
	:upmin: Limiter (Upmin).  Typical Value = 0. Default: 0.0
	:te: Time constant (Te).  Typical Value = 0. Default: 0.0
	:xp: Excitation transformer effective reactance (Xp).  Typical Value = 1. Default: 0.0
	:te2: Time Constant (Te2).  Typical Value = 1. Default: 0.0
	:ke2: Gain (Ke2).  Typical Value = 0.1. Default: 0.0
	:ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1).  Typical Value = 3. Default: 0.0
	:seve1: Exciter saturation function value at the corresponding exciter voltage, Ve1, back of commutating reactance (Se[Ve1]).  Typical Value = 0. Default: 0.0
	:ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve2).  Typical Value = 0. Default: 0.0
	:seve2: Exciter saturation function value at the corresponding exciter voltage, Ve2, back of commutating reactance (Se[Ve2]).  Typical Value = 1. Default: 0.0
	:tr4: Time constant (Tr4).  Typical Value = 1. Default: 0.0
	:k3: Gain (K3).  Typical Value = 0.1. Default: 0.0
	:ti3: Time constant (Ti3).  Typical Value = 3. Default: 0.0
	:k4: Gain (K4).  Typical Value = 0. Default: 0.0
	:ti4: Time constant (Ti4).  Typical Value = 0. Default: 0.0
	:iefmax: Limiter (Iefmax).  Typical Value = 1. Default: 0.0
	:iefmin: Limiter (Iefmin).  Typical Value = 1. Default: 0.0
	:efdbas: Gain (Efdbas).  Typical Value = 0.1. Default: 0.0
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'k1': [cgmesProfile.DY.value, ],
						'k1ec': [cgmesProfile.DY.value, ],
						'kd1': [cgmesProfile.DY.value, ],
						'tb1': [cgmesProfile.DY.value, ],
						'pid1max': [cgmesProfile.DY.value, ],
						'ti1': [cgmesProfile.DY.value, ],
						'iefmax2': [cgmesProfile.DY.value, ],
						'k2': [cgmesProfile.DY.value, ],
						'ketb': [cgmesProfile.DY.value, ],
						'upmax': [cgmesProfile.DY.value, ],
						'upmin': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'xp': [cgmesProfile.DY.value, ],
						'te2': [cgmesProfile.DY.value, ],
						'ke2': [cgmesProfile.DY.value, ],
						've1': [cgmesProfile.DY.value, ],
						'seve1': [cgmesProfile.DY.value, ],
						've2': [cgmesProfile.DY.value, ],
						'seve2': [cgmesProfile.DY.value, ],
						'tr4': [cgmesProfile.DY.value, ],
						'k3': [cgmesProfile.DY.value, ],
						'ti3': [cgmesProfile.DY.value, ],
						'k4': [cgmesProfile.DY.value, ],
						'ti4': [cgmesProfile.DY.value, ],
						'iefmax': [cgmesProfile.DY.value, ],
						'iefmin': [cgmesProfile.DY.value, ],
						'efdbas': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, k1 = 0.0, k1ec = 0.0, kd1 = 0.0, tb1 = 0.0, pid1max = 0.0, ti1 = 0.0, iefmax2 = 0.0, k2 = 0.0, ketb = 0.0, upmax = 0.0, upmin = 0.0, te = 0.0, xp = 0.0, te2 = 0.0, ke2 = 0.0, ve1 = 0.0, seve1 = 0.0, ve2 = 0.0, seve2 = 0.0, tr4 = 0.0, k3 = 0.0, ti3 = 0.0, k4 = 0.0, ti4 = 0.0, iefmax = 0.0, iefmin = 0.0, efdbas = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.k1 = k1
		self.k1ec = k1ec
		self.kd1 = kd1
		self.tb1 = tb1
		self.pid1max = pid1max
		self.ti1 = ti1
		self.iefmax2 = iefmax2
		self.k2 = k2
		self.ketb = ketb
		self.upmax = upmax
		self.upmin = upmin
		self.te = te
		self.xp = xp
		self.te2 = te2
		self.ke2 = ke2
		self.ve1 = ve1
		self.seve1 = seve1
		self.ve2 = ve2
		self.seve2 = seve2
		self.tr4 = tr4
		self.k3 = k3
		self.ti3 = ti3
		self.k4 = k4
		self.ti4 = ti4
		self.iefmax = iefmax
		self.iefmin = iefmin
		self.efdbas = efdbas
		
	def __str__(self):
		str = 'class=ExcELIN2\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
