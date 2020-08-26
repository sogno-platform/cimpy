from cimpy.output.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcPIC(ExcitationSystemDynamics):
	'''
	Proportional/Integral Regulator Excitation System Model.  This model can be used to represent excitation systems with a proportional-integral (PI) voltage regulator controller.

	:ka: PI controller gain (Ka).  Typical Value = 3.15. Default: 
	:ta1: PI controller time constant (Ta1).  Typical Value = 1. Default: 
	:vr1: PI maximum limit (Vr1).  Typical Value = 1. Default: 
	:vr2: PI minimum limit (Vr2).  Typical Value = -0.87. Default: 
	:ta2: Voltage regulator time constant (Ta2).  Typical Value = 0.01. Default: 
	:ta3: Lead time constant (Ta3).  Typical Value = 0. Default: 
	:ta4: Lag time constant (Ta4).  Typical Value = 0. Default: 
	:vrmax: Voltage regulator maximum limit (Vrmax).  Typical Value = 1. Default: 
	:vrmin: Voltage regulator minimum limit (Vrmin).  Typical Value = -0.87. Default: 
	:kf: Rate feedback gain (Kf).  Typical Value = 0. Default: 
	:tf1: Rate feedback time constant (Tf1).  Typical Value = 0. Default: 
	:tf2: Rate feedback lag time constant (Tf2).  Typical Value = 0. Default: 
	:efdmax: Exciter maximum limit (Efdmax).  Typical Value = 8. Default: 
	:efdmin: Exciter minimum limit (Efdmin).  Typical Value = -0.87. Default: 
	:ke: Exciter constant (Ke).  Typical Value = 0. Default: 
	:te: Exciter time constant (Te).  Typical Value = 0. Default: 
	:e1: Field voltage value 1 (E1).  Typical Value = 0. Default: 
	:se1: Saturation factor at E1 (Se1).  Typical Value = 0. Default: 
	:e2: Field voltage value 2 (E2).  Typical Value = 0. Default: 
	:se2: Saturation factor at E2 (Se2).  Typical Value = 0. Default: 
	:kp: Potential source gain (Kp).  Typical Value = 6.5. Default: 
	:ki: Current source gain (Ki).  Typical Value = 0. Default: 
	:kc: Exciter regulation factor (Kc).  Typical Value = 0.08. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'ta1': [cgmesProfile.DY.value, ],
						'vr1': [cgmesProfile.DY.value, ],
						'vr2': [cgmesProfile.DY.value, ],
						'ta2': [cgmesProfile.DY.value, ],
						'ta3': [cgmesProfile.DY.value, ],
						'ta4': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'kf': [cgmesProfile.DY.value, ],
						'tf1': [cgmesProfile.DY.value, ],
						'tf2': [cgmesProfile.DY.value, ],
						'efdmax': [cgmesProfile.DY.value, ],
						'efdmin': [cgmesProfile.DY.value, ],
						'ke': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'e1': [cgmesProfile.DY.value, ],
						'se1': [cgmesProfile.DY.value, ],
						'e2': [cgmesProfile.DY.value, ],
						'se2': [cgmesProfile.DY.value, ],
						'kp': [cgmesProfile.DY.value, ],
						'ki': [cgmesProfile.DY.value, ],
						'kc': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ka = , ta1 = , vr1 = , vr2 = , ta2 = , ta3 = , ta4 = , vrmax = , vrmin = , kf = , tf1 = , tf2 = , efdmax = , efdmin = , ke = , te = , e1 = , se1 = , e2 = , se2 = , kp = , ki = , kc = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ka = ka
		self.ta1 = ta1
		self.vr1 = vr1
		self.vr2 = vr2
		self.ta2 = ta2
		self.ta3 = ta3
		self.ta4 = ta4
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.kf = kf
		self.tf1 = tf1
		self.tf2 = tf2
		self.efdmax = efdmax
		self.efdmin = efdmin
		self.ke = ke
		self.te = te
		self.e1 = e1
		self.se1 = se1
		self.e2 = e2
		self.se2 = se2
		self.kp = kp
		self.ki = ki
		self.kc = kc
		
	def __str__(self):
		str = 'class=ExcPIC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
