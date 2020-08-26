from cimpy.cgmes_v2_4_15.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcST4B(ExcitationSystemDynamics):
	'''
	Modified IEEE ST4B static excitation system with maximum inner loop feedback gain .

	:kpr: Voltage regulator proportional gain (Kpr).  Typical Value = 10.75. Default: 
	:kir: Voltage regulator integral gain (Kir).  Typical Value = 10.75. Default: 
	:ta: Voltage regulator time constant (Ta).  Typical Value = 0.02. Default: 
	:vrmax: Maximum voltage regulator output (Vrmax).  Typical Value = 1. Default: 
	:vrmin: Minimum voltage regulator output (Vrmin).  Typical Value = -0.87. Default: 
	:kpm: Voltage regulator proportional gain output (Kpm).  Typical Value = 1. Default: 
	:kim: Voltage regulator integral gain output (Kim).  Typical Value = 0. Default: 
	:vmmax: Maximum inner loop output (Vmmax).  Typical Value = 99. Default: 
	:vmmin: Minimum inner loop output (Vmmin).  Typical Value = -99. Default: 
	:kg: Feedback gain constant of the inner loop field regulator (Kg). Typical Value = 0. Default: 
	:kp: Potential circuit gain coefficient (Kp).  Typical Value = 9.3. Default: 
	:thetap: Potential circuit phase angle (thetap).  Typical Value = 0. Default: 
	:ki: Potential circuit gain coefficient (Ki).  Typical Value = 0. Default: 
	:kc: Rectifier loading factor proportional to commutating reactance (Kc). Typical Value = 0.113. Default: 
	:xl: Reactance associated with potential source (Xl).  Typical Value = 0.124. Default: 
	:vbmax: Maximum excitation voltage (Vbmax).  Typical Value = 11.63. Default: 
	:vgmax: Maximum inner loop feedback voltage (Vgmax).  Typical Value = 5.8. Default: 
	:uel: Selector (Uel). true = UEL is part of block diagram false = UEL is not part of block diagram.  Typical Value = false. Default: 
	:lvgate: Selector (LVgate). true = LVgate is part of the block diagram false = LVgate is not part of the block diagram.  Typical Value = false. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'kpr': [cgmesProfile.DY.value, ],
						'kir': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'kpm': [cgmesProfile.DY.value, ],
						'kim': [cgmesProfile.DY.value, ],
						'vmmax': [cgmesProfile.DY.value, ],
						'vmmin': [cgmesProfile.DY.value, ],
						'kg': [cgmesProfile.DY.value, ],
						'kp': [cgmesProfile.DY.value, ],
						'thetap': [cgmesProfile.DY.value, ],
						'ki': [cgmesProfile.DY.value, ],
						'kc': [cgmesProfile.DY.value, ],
						'xl': [cgmesProfile.DY.value, ],
						'vbmax': [cgmesProfile.DY.value, ],
						'vgmax': [cgmesProfile.DY.value, ],
						'uel': [cgmesProfile.DY.value, ],
						'lvgate': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, kpr = , kir = , ta = , vrmax = , vrmin = , kpm = , kim = , vmmax = , vmmin = , kg = , kp = , thetap = , ki = , kc = , xl = , vbmax = , vgmax = , uel = , lvgate = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.kpr = kpr
		self.kir = kir
		self.ta = ta
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.kpm = kpm
		self.kim = kim
		self.vmmax = vmmax
		self.vmmin = vmmin
		self.kg = kg
		self.kp = kp
		self.thetap = thetap
		self.ki = ki
		self.kc = kc
		self.xl = xl
		self.vbmax = vbmax
		self.vgmax = vgmax
		self.uel = uel
		self.lvgate = lvgate
		
	def __str__(self):
		str = 'class=ExcST4B\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
