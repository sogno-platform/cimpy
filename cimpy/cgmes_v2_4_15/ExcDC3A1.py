from cimpy.cgmes_v2_4_15.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcDC3A1(ExcitationSystemDynamics):
	'''
	This is modified old IEEE type 3 excitation system.

	:ka: Voltage regulator gain (Ka).  Typical Value = 300. Default: 0.0
	:ta: Voltage regulator time constant (Ta).  Typical Value = 0.01. Default: 0.0
	:vrmax: Maximum voltage regulator output (Vrmax).  Typical Value = 5. Default: 0.0
	:vrmin: Minimum voltage regulator output (Vrmin).  Typical Value = 0. Default: 0.0
	:te: Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 1.83. Default: 0.0
	:kf: Excitation control system stabilizer gain (Kf).  Typical Value = 0.1. Default: 0.0
	:tf: Excitation control system stabilizer time constant (Tf).  Typical Value = 0.675. Default: 0.0
	:kp: Potential circuit gain coefficient (Kp).  Typical Value = 4.37. Default: 0.0
	:ki: Potential circuit gain coefficient (Ki).  Typical Value = 4.83. Default: 0.0
	:vbmax: Available exciter voltage limiter (Vbmax).  Typical Value = 11.63. Default: 0.0
	:exclim: (exclim). true = lower limit of zero is applied to integrator output false = lower limit of zero not applied to integrator output. Typical Value = true. Default: False
	:ke: Exciter constant related to self-excited field (Ke).  Typical Value = 1. Default: 0.0
	:vb1max: Available exciter voltage limiter (Vb1max).  Typical Value = 11.63. Default: 0.0
	:vblim: Vb limiter indicator. true = exciter Vbmax limiter is active false = Vb1max is active.  Typical Value = true. Default: False
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'kf': [cgmesProfile.DY.value, ],
						'tf': [cgmesProfile.DY.value, ],
						'kp': [cgmesProfile.DY.value, ],
						'ki': [cgmesProfile.DY.value, ],
						'vbmax': [cgmesProfile.DY.value, ],
						'exclim': [cgmesProfile.DY.value, ],
						'ke': [cgmesProfile.DY.value, ],
						'vb1max': [cgmesProfile.DY.value, ],
						'vblim': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ka = 0.0, ta = 0.0, vrmax = 0.0, vrmin = 0.0, te = 0.0, kf = 0.0, tf = 0.0, kp = 0.0, ki = 0.0, vbmax = 0.0, exclim = False, ke = 0.0, vb1max = 0.0, vblim = False,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ka = ka
		self.ta = ta
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.te = te
		self.kf = kf
		self.tf = tf
		self.kp = kp
		self.ki = ki
		self.vbmax = vbmax
		self.exclim = exclim
		self.ke = ke
		self.vb1max = vb1max
		self.vblim = vblim
		
	def __str__(self):
		str = 'class=ExcDC3A1\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
