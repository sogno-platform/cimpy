from cimpy.cgmes_v2_4_15.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAC5A(ExcitationSystemDynamics):
	'''
	Modified IEEE AC5A alternator-supplied rectifier excitation system with different minimum controller output.

	:ka: Voltage regulator gain (Ka).  Typical Value = 400. Default: 
	:ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0. Default: 
	:tb: Voltage regulator time constant (Tb).  Typical Value = 0. Default: 
	:tc: Voltage regulator time constant (Tc).  Typical Value = 0. Default: 
	:ta: Voltage regulator time constant (Ta).  Typical Value = 0.02. Default: 
	:vrmax: Maximum voltage regulator output (Vrmax).  Typical Value = 7.3. Default: 
	:vrmin: Minimum voltage regulator output (Vrmin).  Typical Value =-7.3. Default: 
	:ke: Exciter constant related to self-excited field (Ke).  Typical Value = 1. Default: 
	:te: Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 0.8. Default: 
	:kf: Excitation control system stabilizer gains (Kf).  Typical Value = 0.03. Default: 
	:tf1: Excitation control system stabilizer time constant (Tf1).  Typical Value  = 1. Default: 
	:tf2: Excitation control system stabilizer time constant (Tf2).  Typical Value = 0.8. Default: 
	:tf3: Excitation control system stabilizer time constant (Tf3).  Typical Value = 0. Default: 
	:efd1: Exciter voltage at which exciter saturation is defined (Efd1).  Typical Value = 5.6. Default: 
	:seefd1: Exciter saturation function value at the corresponding exciter voltage, Efd1 (S[Efd1]).  Typical Value = 0.86. Default: 
	:efd2: Exciter voltage at which exciter saturation is defined (Efd2).  Typical Value = 4.2. Default: 
	:seefd2: Exciter saturation function value at the corresponding exciter voltage, Efd2 (S[Efd2]).  Typical Value = 0.5. Default: 
	:a: Coefficient to allow different usage of the model (a).  Typical Value = 1. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'ks': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'ke': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'kf': [cgmesProfile.DY.value, ],
						'tf1': [cgmesProfile.DY.value, ],
						'tf2': [cgmesProfile.DY.value, ],
						'tf3': [cgmesProfile.DY.value, ],
						'efd1': [cgmesProfile.DY.value, ],
						'seefd1': [cgmesProfile.DY.value, ],
						'efd2': [cgmesProfile.DY.value, ],
						'seefd2': [cgmesProfile.DY.value, ],
						'a': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ka = , ks = , tb = , tc = , ta = , vrmax = , vrmin = , ke = , te = , kf = , tf1 = , tf2 = , tf3 = , efd1 = , seefd1 = , efd2 = , seefd2 = , a = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ka = ka
		self.ks = ks
		self.tb = tb
		self.tc = tc
		self.ta = ta
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.ke = ke
		self.te = te
		self.kf = kf
		self.tf1 = tf1
		self.tf2 = tf2
		self.tf3 = tf3
		self.efd1 = efd1
		self.seefd1 = seefd1
		self.efd2 = efd2
		self.seefd2 = seefd2
		self.a = a
		
	def __str__(self):
		str = 'class=ExcAC5A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
