from cimpy.cgmes_v2_4_15.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcST2A(ExcitationSystemDynamics):
	'''
	Modified IEEE ST2A static excitation system - another lead-lag block added to match  the model defined by WECC.

	:ka: Voltage regulator gain (Ka).  Typical Value = 120. Default: 0.0
	:ta: Voltage regulator time constant (Ta).  Typical Value = 0.15. Default: 0.0
	:vrmax: Maximum voltage regulator outputs (Vrmax).  Typical Value = 1. Default: 0.0
	:vrmin: Minimum voltage regulator outputs (Vrmin).  Typical Value = -1. Default: 0.0
	:ke: Exciter constant related to self-excited field (Ke).  Typical Value = 1. Default: 0.0
	:te: Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 0.5. Default: 0.0
	:kf: Excitation control system stabilizer gains (Kf).  Typical Value = 0.05. Default: 0.0
	:tf: Excitation control system stabilizer time constant (Tf).  Typical Value = 0.7. Default: 0.0
	:kp: Potential circuit gain coefficient (Kp).  Typical Value = 4.88. Default: 0.0
	:ki: Potential circuit gain coefficient (Ki).  Typical Value = 8. Default: 0.0
	:kc: Rectifier loading factor proportional to commutating reactance (Kc).  Typical Value = 1.82. Default: 0.0
	:efdmax: Maximum field voltage (Efdmax).  Typical Value = 99. Default: 0.0
	:uelin: UEL input (UELin). true = HV gate false = add to error signal. Typical Value = false. Default: False
	:tb: Voltage regulator time constant (Tb).  Typical Value = 0. Default: 0.0
	:tc: Voltage regulator time constant (Tc).  Typical Value = 0. Default: 0.0
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

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
						'tb': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ka = 0.0, ta = 0.0, vrmax = 0.0, vrmin = 0.0, ke = 0.0, te = 0.0, kf = 0.0, tf = 0.0, kp = 0.0, ki = 0.0, kc = 0.0, efdmax = 0.0, uelin = False, tb = 0.0, tc = 0.0,  *args, **kw_args):
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
		self.tb = tb
		self.tc = tc
		
	def __str__(self):
		str = 'class=ExcST2A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
