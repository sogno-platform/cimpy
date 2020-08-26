from cimpy.output.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEDC2A(ExcitationSystemDynamics):
	'''
	The class represents IEEE Std 421.5-2005 type DC2A model. This model represents represent field-controlled dc commutator exciters with continuously acting voltage regulators having supplies obtained from the generator or auxiliary bus.  It differs from the Type DC1A model only in the voltage regulator output limits, which are now proportional to terminal voltage . It is representative of solid-state replacements for various forms of older mechanical and rotating amplifier regulating equipment connected to dc commutator exciters.  Reference: IEEE Standard 421.5-2005 Section 5.2.

	:efd1: Exciter voltage at which exciter saturation is defined (E).  Typical Value = 3.05. Default: 
	:efd2: Exciter voltage at which exciter saturation is defined (E).  Typical Value = 2.29. Default: 
	:exclim: (exclim).  IEEE standard is ambiguous about lower limit on exciter output. Typical Value = - 999  which means that there is no limit applied. Default: 
	:ka: Voltage regulator gain (K).  Typical Value = 300. Default: 
	:ke: Exciter constant related to self-excited field (K).  Typical Value = 1. Default: 
	:kf: Excitation control system stabilizer gain (K).  Typical Value = 0.1. Default: 
	:seefd1: Exciter saturation function value at the corresponding exciter voltage, E (S[E]).  Typical Value = 0.279. Default: 
	:seefd2: Exciter saturation function value at the corresponding exciter voltage, E (S[E]).  Typical Value = 0.117. Default: 
	:ta: Voltage regulator time constant (T).  Typical Value = 0.01. Default: 
	:tb: Voltage regulator time constant (T).  Typical Value = 0. Default: 
	:tc: Voltage regulator time constant (T).  Typical Value = 0. Default: 
	:te: Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 1.33. Default: 
	:tf: Excitation control system stabilizer time constant (T).  Typical Value = 0.675. Default: 
	:uelin: UEL input (uelin). true = input is connected to the HV gate false = input connects to the error signal. Typical Value = true. Default: 
	:vrmax: Maximum voltage regulator output (V).  Typical Value = 4.95. Default: 
	:vrmin: Minimum voltage regulator output (V).  Typical Value = -4.9. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'efd1': [cgmesProfile.DY.value, ],
						'efd2': [cgmesProfile.DY.value, ],
						'exclim': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'ke': [cgmesProfile.DY.value, ],
						'kf': [cgmesProfile.DY.value, ],
						'seefd1': [cgmesProfile.DY.value, ],
						'seefd2': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'tf': [cgmesProfile.DY.value, ],
						'uelin': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, efd1 = , efd2 = , exclim = , ka = , ke = , kf = , seefd1 = , seefd2 = , ta = , tb = , tc = , te = , tf = , uelin = , vrmax = , vrmin = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.efd1 = efd1
		self.efd2 = efd2
		self.exclim = exclim
		self.ka = ka
		self.ke = ke
		self.kf = kf
		self.seefd1 = seefd1
		self.seefd2 = seefd2
		self.ta = ta
		self.tb = tb
		self.tc = tc
		self.te = te
		self.tf = tf
		self.uelin = uelin
		self.vrmax = vrmax
		self.vrmin = vrmin
		
	def __str__(self):
		str = 'class=ExcIEEEDC2A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
