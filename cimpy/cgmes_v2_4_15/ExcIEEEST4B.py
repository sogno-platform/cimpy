from cimpy.cgmes_v2_4_15.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEST4B(ExcitationSystemDynamics):
	'''
	The class represents IEEE Std 421.5-2005 type ST4B model. This model is a variation of the Type ST3A model, with a proportional plus integral (PI) regulator block replacing the lag-lead regulator characteristic that is in the ST3A model. Both potential and compound source rectifier excitation systems are modeled.  The PI regulator blocks have non-windup limits that are represented. The voltage regulator of this model is typically implemented digitally.  Reference: IEEE Standard 421.5-2005 Section 7.4.

	:kpr: Voltage regulator proportional gain (K).  Typical Value = 10.75. Default: 
	:kir: Voltage regulator integral gain (K).  Typical Value = 10.75. Default: 
	:ta: Voltage regulator time constant (T).  Typical Value = 0.02. Default: 
	:vrmax: Maximum voltage regulator output (V).  Typical Value = 1. Default: 
	:vrmin: Minimum voltage regulator output (V).  Typical Value = -0.87. Default: 
	:kpm: Voltage regulator proportional gain output (K).  Typical Value = 1. Default: 
	:kim: Voltage regulator integral gain output (K).  Typical Value = 0. Default: 
	:vmmax: Maximum inner loop output (V).  Typical Value = 99. Default: 
	:vmmin: Minimum inner loop output (V).  Typical Value = -99. Default: 
	:kg: Feedback gain constant of the inner loop field regulator (K).  Typical Value = 0. Default: 
	:kp: Potential circuit gain coefficient (K).  Typical Value = 9.3. Default: 
	:thetap: Potential circuit phase angle (thetap).  Typical Value = 0. Default: 
	:ki: Potential circuit gain coefficient (K).  Typical Value = 0. Default: 
	:kc: Rectifier loading factor proportional to commutating reactance (K). Typical Value = 0.113. Default: 
	:xl: Reactance associated with potential source (X).  Typical Value = 0.124. Default: 
	:vbmax: Maximum excitation voltage (V).  Typical Value = 11.63. Default: 
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
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, kpr = , kir = , ta = , vrmax = , vrmin = , kpm = , kim = , vmmax = , vmmin = , kg = , kp = , thetap = , ki = , kc = , xl = , vbmax = ,  *args, **kw_args):
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
		
	def __str__(self):
		str = 'class=ExcIEEEST4B\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
