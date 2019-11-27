from cimpy.cgmes_v2_4_15.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcPIC(ExcitationSystemDynamics):
	'''
	Proportional/Integral Regulator Excitation System Model.  This model can be used to represent excitation systems with a proportional-integral (PI) voltage regulator controller.

	:ka: PI controller gain (Ka).  Typical Value = 3.15. Default: 0.0
	:ta1: PI controller time constant (Ta1).  Typical Value = 1. Default: 0.0
	:vr1: PI maximum limit (Vr1).  Typical Value = 1. Default: 0.0
	:vr2: PI minimum limit (Vr2).  Typical Value = -0.87. Default: 0.0
	:ta2: Voltage regulator time constant (Ta2).  Typical Value = 0.01. Default: 0.0
	:ta3: Lead time constant (Ta3).  Typical Value = 0. Default: 0.0
	:ta4: Lag time constant (Ta4).  Typical Value = 0. Default: 0.0
	:vrmax: Voltage regulator maximum limit (Vrmax).  Typical Value = 1. Default: 0.0
	:vrmin: Voltage regulator minimum limit (Vrmin).  Typical Value = -0.87. Default: 0.0
	:kf: Rate feedback gain (Kf).  Typical Value = 0. Default: 0.0
	:tf1: Rate feedback time constant (Tf1).  Typical Value = 0. Default: 0.0
	:tf2: Rate feedback lag time constant (Tf2).  Typical Value = 0. Default: 0.0
	:efdmax: Exciter maximum limit (Efdmax).  Typical Value = 8. Default: 0.0
	:efdmin: Exciter minimum limit (Efdmin).  Typical Value = -0.87. Default: 0.0
	:ke: Exciter constant (Ke).  Typical Value = 0. Default: 0.0
	:te: Exciter time constant (Te).  Typical Value = 0. Default: 0.0
	:e1: Field voltage value 1 (E1).  Typical Value = 0. Default: 0.0
	:se1: Saturation factor at E1 (Se1).  Typical Value = 0. Default: 0.0
	:e2: Field voltage value 2 (E2).  Typical Value = 0. Default: 0.0
	:se2: Saturation factor at E2 (Se2).  Typical Value = 0. Default: 0.0
	:kp: Potential source gain (Kp).  Typical Value = 6.5. Default: 0.0
	:ki: Current source gain (Ki).  Typical Value = 0. Default: 0.0
	:kc: Exciter regulation factor (Kc).  Typical Value = 0.08. Default: 0.0
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

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ka = 0.0, ta1 = 0.0, vr1 = 0.0, vr2 = 0.0, ta2 = 0.0, ta3 = 0.0, ta4 = 0.0, vrmax = 0.0, vrmin = 0.0, kf = 0.0, tf1 = 0.0, tf2 = 0.0, efdmax = 0.0, efdmin = 0.0, ke = 0.0, te = 0.0, e1 = 0.0, se1 = 0.0, e2 = 0.0, se2 = 0.0, kp = 0.0, ki = 0.0, kc = 0.0,  *args, **kw_args):
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
