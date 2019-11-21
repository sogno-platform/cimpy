from cimpy.cgmes_v2_4_15_flat.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEST2A(ExcitationSystemDynamics):
	'''
	The class represents IEEE Std 421.5-2005 type ST2A model. Some static systems utilize both current and voltage sources (generator terminal quantities) to comprise the power source.  The regulator controls the exciter output through controlled saturation of the power transformer components.  These compound-source rectifier excitation systems are designated Type ST2A and are represented by ExcIEEEST2A.  Reference: IEEE Standard 421.5-2005 Section 7.2.

	:ka: Voltage regulator gain (K).  Typical Value = 120. Default: 0.0
	:ta: Voltage regulator time constant (T).  Typical Value = 0.15. Default: 0.0
	:vrmax: Maximum voltage regulator outputs (V).  Typical Value = 1. Default: 0.0
	:vrmin: Minimum voltage regulator outputs (V).  Typical Value = 0. Default: 0.0
	:ke: Exciter constant related to self-excited field (K).  Typical Value = 1. Default: 0.0
	:te: Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 0.5. Default: 0.0
	:kf: Excitation control system stabilizer gains (K).  Typical Value = 0.05. Default: 0.0
	:tf: Excitation control system stabilizer time constant (T).  Typical Value = 1. Default: 0.0
	:kp: Potential circuit gain coefficient (K).  Typical Value = 4.88. Default: 0.0
	:ki: Potential circuit gain coefficient (K).  Typical Value = 8. Default: 0.0
	:kc: Rectifier loading factor proportional to commutating reactance (K). Typical Value = 1.82. Default: 0.0
	:efdmax: Maximum field voltage (E).  Typical Value = 99. Default: 0.0
	:uelin: UEL input (UELin). true = HV gate false = add to error signal. Typical Value = true. Default: False
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'ke': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'kf': [cgmesProfile.DY.value, ],
						'tf': [cgmesProfile.DY.value, ],
						'kp': [cgmesProfile.DY.value, ],
						'ki': [cgmesProfile.DY.value, ],
						'kc': [cgmesProfile.DY.value, ],
						'efdmax': [cgmesProfile.DY.value, ],
						'uelin': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ka = 0.0, ta = 0.0, vrmax = 0.0, vrmin = 0.0, ke = 0.0, te = 0.0, kf = 0.0, tf = 0.0, kp = 0.0, ki = 0.0, kc = 0.0, efdmax = 0.0, uelin = False,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ka = ka
		self.ta = ta
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.ke = ke
		self.te = te
		self.kf = kf
		self.tf = tf
		self.kp = kp
		self.ki = ki
		self.kc = kc
		self.efdmax = efdmax
		self.uelin = uelin
		
	def __str__(self):
		str = 'class=ExcIEEEST2A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
