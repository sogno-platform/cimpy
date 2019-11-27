from cimpy.cgmes_v2_4_15.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEDC1A(ExcitationSystemDynamics):
	'''
	The class represents IEEE Std 421.5-2005 type DC1A model. This model represents field-controlled dc commutator exciters with continuously acting voltage regulators (especially the direct-acting rheostatic, rotating amplifier, and magnetic amplifier types).  Because this model has been widely implemented by the industry, it is sometimes used to represent other types of systems when detailed data for them are not available or when a simplified model is required.   Reference: IEEE Standard 421.5-2005 Section 5.1.

	:ka: Voltage regulator gain (K).  Typical Value = 46. Default: 0.0
	:ta: Voltage regulator time constant (T).  Typical Value = 0.06. Default: 0.0
	:tb: Voltage regulator time constant (T).  Typical Value = 0. Default: 0.0
	:tc: Voltage regulator time constant (T).  Typical Value = 0. Default: 0.0
	:vrmax: Maximum voltage regulator output (V).  Typical Value = 1. Default: 0.0
	:vrmin: Minimum voltage regulator output (V).  Typical Value = -0.9. Default: 0.0
	:ke: Exciter constant related to self-excited field (K).  Typical Value = 0. Default: 0.0
	:te: Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 0.46. Default: 0.0
	:kf: Excitation control system stabilizer gain (K).  Typical Value = 0.1. Default: 0.0
	:tf: Excitation control system stabilizer time constant (T).  Typical Value = 1. Default: 0.0
	:efd1: Exciter voltage at which exciter saturation is defined (E).  Typical Value = 3.1. Default: 0.0
	:seefd1: Exciter saturation function value at the corresponding exciter voltage, E (S[E]).  Typical Value = 0.33. Default: 0.0
	:efd2: Exciter voltage at which exciter saturation is defined (E).  Typical Value = 2.3. Default: 0.0
	:seefd2: Exciter saturation function value at the corresponding exciter voltage, E (S[E]).  Typical Value = 0.1. Default: 0.0
	:uelin: UEL input (uelin). true = input is connected to the HV gate false = input connects to the error signal. Typical Value = true. Default: False
	:exclim: (exclim).  IEEE standard is ambiguous about lower limit on exciter output. true = a lower limit of zero is applied to integrator output false = a lower limit of zero is not applied to integrator output. Typical Value = true. Default: False
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'tb': [cgmesProfile.DY.value, ],
						'tc': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'ke': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'kf': [cgmesProfile.DY.value, ],
						'tf': [cgmesProfile.DY.value, ],
						'efd1': [cgmesProfile.DY.value, ],
						'seefd1': [cgmesProfile.DY.value, ],
						'efd2': [cgmesProfile.DY.value, ],
						'seefd2': [cgmesProfile.DY.value, ],
						'uelin': [cgmesProfile.DY.value, ],
						'exclim': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ka = 0.0, ta = 0.0, tb = 0.0, tc = 0.0, vrmax = 0.0, vrmin = 0.0, ke = 0.0, te = 0.0, kf = 0.0, tf = 0.0, efd1 = 0.0, seefd1 = 0.0, efd2 = 0.0, seefd2 = 0.0, uelin = False, exclim = False,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ka = ka
		self.ta = ta
		self.tb = tb
		self.tc = tc
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.ke = ke
		self.te = te
		self.kf = kf
		self.tf = tf
		self.efd1 = efd1
		self.seefd1 = seefd1
		self.efd2 = efd2
		self.seefd2 = seefd2
		self.uelin = uelin
		self.exclim = exclim
		
	def __str__(self):
		str = 'class=ExcIEEEDC1A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
