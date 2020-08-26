from cimpy.cgmes_v2_4_15.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcREXS(ExcitationSystemDynamics):
	'''
	General Purpose Rotating Excitation System Model.  This model can be used to represent a wide range of excitation systems whose DC power source is an AC or DC generator. It encompasses IEEE type AC1, AC2, DC1, and DC2 excitation system models.

	:e1: Field voltage value 1 (E1).  Typical Value = 3. Default: 
	:e2: Field voltage value 2 (E2).  Typical Value = 4. Default: 
	:fbf: Rate feedback signal flag (Fbf). Typical Value = fieldCurrent. Default: 
	:flimf: Limit type flag (Flimf).  Typical Value = 0. Default: 
	:kc: Rectifier regulation factor (Kc).  Typical Value = 0.05. Default: 
	:kd: Exciter regulation factor (Kd).  Typical Value = 2. Default: 
	:ke: Exciter field proportional constant (Ke).  Typical Value = 1. Default: 
	:kefd: Field voltage feedback gain (Kefd).  Typical Value = 0. Default: 
	:kf: Rate feedback gain (Kf).  Typical Value = 0.05. Default: 
	:kh: Field voltage controller feedback gain (Kh).  Typical Value = 0. Default: 
	:kii: Field Current Regulator Integral Gain (Kii).  Typical Value = 0. Default: 
	:kip: Field Current Regulator Proportional Gain (Kip).  Typical Value = 1. Default: 
	:ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0. Default: 
	:kvi: Voltage Regulator Integral Gain (Kvi).  Typical Value = 0. Default: 
	:kvp: Voltage Regulator Proportional Gain (Kvp).  Typical Value = 2800. Default: 
	:kvphz: V/Hz limiter gain (Kvphz).  Typical Value = 0. Default: 
	:nvphz: Pickup speed of V/Hz limiter (Nvphz).  Typical Value = 0. Default: 
	:se1: Saturation factor at E1 (Se1).  Typical Value = 0.0001. Default: 
	:se2: Saturation factor at E2 (Se2).  Typical Value = 0.001. Default: 
	:ta: Voltage Regulator time constant (Ta).  Typical Value = 0.01. Default: 
	:tb1: Lag time constant (Tb1).  Typical Value = 0. Default: 
	:tb2: Lag time constant (Tb2).  Typical Value = 0. Default: 
	:tc1: Lead time constant (Tc1).  Typical Value = 0. Default: 
	:tc2: Lead time constant (Tc2).  Typical Value = 0. Default: 
	:te: Exciter field time constant (Te).  Typical Value = 1.2. Default: 
	:tf: Rate feedback time constant (Tf).  Typical Value = 1. Default: 
	:tf1: Feedback lead time constant (Tf1).  Typical Value = 0. Default: 
	:tf2: Feedback lag time constant (Tf2).  Typical Value = 0. Default: 
	:tp: Field current Bridge time constant (Tp).  Typical Value = 0. Default: 
	:vcmax: Maximum compounding voltage (Vcmax).  Typical Value = 0. Default: 
	:vfmax: Maximum Exciter Field Current (Vfmax).  Typical Value = 47. Default: 
	:vfmin: Minimum Exciter Field Current (Vfmin).  Typical Value = -20. Default: 
	:vimax: Voltage Regulator Input Limit (Vimax).  Typical Value = 0.1. Default: 
	:vrmax: Maximum controller output (Vrmax).  Typical Value = 47. Default: 
	:vrmin: Minimum controller output (Vrmin).  Typical Value = -20. Default: 
	:xc: Exciter compounding reactance (Xc).  Typical Value = 0. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'e1': [cgmesProfile.DY.value, ],
						'e2': [cgmesProfile.DY.value, ],
						'fbf': [cgmesProfile.DY.value, ],
						'flimf': [cgmesProfile.DY.value, ],
						'kc': [cgmesProfile.DY.value, ],
						'kd': [cgmesProfile.DY.value, ],
						'ke': [cgmesProfile.DY.value, ],
						'kefd': [cgmesProfile.DY.value, ],
						'kf': [cgmesProfile.DY.value, ],
						'kh': [cgmesProfile.DY.value, ],
						'kii': [cgmesProfile.DY.value, ],
						'kip': [cgmesProfile.DY.value, ],
						'ks': [cgmesProfile.DY.value, ],
						'kvi': [cgmesProfile.DY.value, ],
						'kvp': [cgmesProfile.DY.value, ],
						'kvphz': [cgmesProfile.DY.value, ],
						'nvphz': [cgmesProfile.DY.value, ],
						'se1': [cgmesProfile.DY.value, ],
						'se2': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'tb1': [cgmesProfile.DY.value, ],
						'tb2': [cgmesProfile.DY.value, ],
						'tc1': [cgmesProfile.DY.value, ],
						'tc2': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'tf': [cgmesProfile.DY.value, ],
						'tf1': [cgmesProfile.DY.value, ],
						'tf2': [cgmesProfile.DY.value, ],
						'tp': [cgmesProfile.DY.value, ],
						'vcmax': [cgmesProfile.DY.value, ],
						'vfmax': [cgmesProfile.DY.value, ],
						'vfmin': [cgmesProfile.DY.value, ],
						'vimax': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'xc': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, e1 = , e2 = , fbf = , flimf = , kc = , kd = , ke = , kefd = , kf = , kh = , kii = , kip = , ks = , kvi = , kvp = , kvphz = , nvphz = , se1 = , se2 = , ta = , tb1 = , tb2 = , tc1 = , tc2 = , te = , tf = , tf1 = , tf2 = , tp = , vcmax = , vfmax = , vfmin = , vimax = , vrmax = , vrmin = , xc = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.e1 = e1
		self.e2 = e2
		self.fbf = fbf
		self.flimf = flimf
		self.kc = kc
		self.kd = kd
		self.ke = ke
		self.kefd = kefd
		self.kf = kf
		self.kh = kh
		self.kii = kii
		self.kip = kip
		self.ks = ks
		self.kvi = kvi
		self.kvp = kvp
		self.kvphz = kvphz
		self.nvphz = nvphz
		self.se1 = se1
		self.se2 = se2
		self.ta = ta
		self.tb1 = tb1
		self.tb2 = tb2
		self.tc1 = tc1
		self.tc2 = tc2
		self.te = te
		self.tf = tf
		self.tf1 = tf1
		self.tf2 = tf2
		self.tp = tp
		self.vcmax = vcmax
		self.vfmax = vfmax
		self.vfmin = vfmin
		self.vimax = vimax
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.xc = xc
		
	def __str__(self):
		str = 'class=ExcREXS\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
