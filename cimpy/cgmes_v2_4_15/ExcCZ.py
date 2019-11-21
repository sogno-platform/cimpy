from cimpy.cgmes_v2_4_15_flat.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcCZ(ExcitationSystemDynamics):
	'''
	Czech Proportion/Integral Exciter.

	:kp: Regulator proportional gain (Kp). Default: 0.0
	:tc: Regulator integral time constant (Tc). Default: 0.0
	:vrmax: Voltage regulator maximum limit (Vrmax). Default: 0.0
	:vrmin: Voltage regulator minimum limit (Vrmin). Default: 0.0
	:ka: Regulator gain (Ka). Default: 0.0
	:ta: Regulator time constant (Ta). Default: 0.0
	:ke: Exciter constant related to self-excited field (Ke). Default: 0.0
	:te: Exciter time constant, integration rate associated with exciter control (Te). Default: 0.0
	:efdmax: Exciter output maximum limit (Efdmax). Default: 0.0
	:efdmin: Exciter output minimum limit (Efdmin). Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'kp': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'ke': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'efdmax': [cgmesProfile.DY.value, ],
						'efdmin': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, kp = 0.0, tc = 0.0, vrmax = 0.0, vrmin = 0.0, ka = 0.0, ta = 0.0, ke = 0.0, te = 0.0, efdmax = 0.0, efdmin = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.kp = kp
		self.tc = tc
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.ka = ka
		self.ta = ta
		self.ke = ke
		self.te = te
		self.efdmax = efdmax
		self.efdmin = efdmin
		
	def __str__(self):
		str = 'class=ExcCZ\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
