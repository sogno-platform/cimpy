from cimpy.output.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEAC8B(ExcitationSystemDynamics):
	'''
	The class represents IEEE Std 421.5-2005 type AC8B model. This model represents a PID voltage regulator with either a brushless exciter or dc exciter. The AVR in this model consists of PID control, with separate constants for the proportional (), integral (), and derivative () gains. The representation of the brushless exciter (, , , , ) is similar to the model Type AC2A. The Type AC8B model can be used to represent static voltage regulators applied to brushless excitation systems. Digitally based voltage regulators feeding dc rotating main exciters can be represented with the AC Type AC8B model with the parameters  and  set to 0.  For thyristor power stages fed from the generator terminals, the limits  and  should be a function of terminal voltage:  * and  * .     Reference: IEEE Standard 421.5-2005 Section 6.8.

	:kpr: Voltage regulator proportional gain (K).  Typical Value = 80. Default: 
	:kir: Voltage regulator integral gain (K).  Typical Value = 5. Default: 
	:kdr: Voltage regulator derivative gain (K).  Typical Value = 10. Default: 
	:tdr: Lag time constant (T).  Typical Value = 0.1. Default: 
	:vrmax: Maximum voltage regulator output (V).  Typical Value = 35. Default: 
	:vrmin: Minimum voltage regulator output (V).  Typical Value = 0. Default: 
	:ka: Voltage regulator gain (K).  Typical Value = 1. Default: 
	:ta: Voltage regulator time constant (T).  Typical Value = 0. Default: 
	:te: Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 1.2. Default: 
	:vfemax: Exciter field current limit reference (V).  Typical Value = 6. Default: 
	:vemin: Minimum exciter voltage output (V).  Typical Value = 0. Default: 
	:ke: Exciter constant related to self-excited field (K).  Typical Value = 1. Default: 
	:kc: Rectifier loading factor proportional to commutating reactance (K). Typical Value = 0.55. Default: 
	:kd: Demagnetizing factor, a function of exciter alternator reactances (K).    Typical Value = 1.1. Default: 
	:ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (V) equals V (V).  Typical Value = 6.5. Default: 
	:seve1: Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 0.3. Default: 
	:ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (V).  Typical Value = 9. Default: 
	:seve2: Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 3. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'kpr': [cgmesProfile.DY.value, ],
						'kir': [cgmesProfile.DY.value, ],
						'kdr': [cgmesProfile.DY.value, ],
						'tdr': [cgmesProfile.DY.value, ],
						'vrmax': [cgmesProfile.DY.value, ],
						'vrmin': [cgmesProfile.DY.value, ],
						'ka': [cgmesProfile.DY.value, ],
						'ta': [cgmesProfile.DY.value, ],
						'te': [cgmesProfile.DY.value, ],
						'vfemax': [cgmesProfile.DY.value, ],
						'vemin': [cgmesProfile.DY.value, ],
						'ke': [cgmesProfile.DY.value, ],
						'kc': [cgmesProfile.DY.value, ],
						'kd': [cgmesProfile.DY.value, ],
						've1': [cgmesProfile.DY.value, ],
						'seve1': [cgmesProfile.DY.value, ],
						've2': [cgmesProfile.DY.value, ],
						'seve2': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, kpr = , kir = , kdr = , tdr = , vrmax = , vrmin = , ka = , ta = , te = , vfemax = , vemin = , ke = , kc = , kd = , ve1 = , seve1 = , ve2 = , seve2 = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.kpr = kpr
		self.kir = kir
		self.kdr = kdr
		self.tdr = tdr
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.ka = ka
		self.ta = ta
		self.te = te
		self.vfemax = vfemax
		self.vemin = vemin
		self.ke = ke
		self.kc = kc
		self.kd = kd
		self.ve1 = ve1
		self.seve1 = seve1
		self.ve2 = ve2
		self.seve2 = seve2
		
	def __str__(self):
		str = 'class=ExcIEEEAC8B\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
