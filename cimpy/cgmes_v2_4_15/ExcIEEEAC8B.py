from cimpy.cgmes_v2_4_15.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEAC8B(ExcitationSystemDynamics):
	'''
	The class represents IEEE Std 421.5-2005 type AC8B model. This model represents a PID voltage regulator with either a brushless exciter or dc exciter. The AVR in this model consists of PID control, with separate constants for the proportional (), integral (), and derivative () gains. The representation of the brushless exciter (, , , , ) is similar to the model Type AC2A. The Type AC8B model can be used to represent static voltage regulators applied to brushless excitation systems. Digitally based voltage regulators feeding dc rotating main exciters can be represented with the AC Type AC8B model with the parameters  and  set to 0.  For thyristor power stages fed from the generator terminals, the limits  and  should be a function of terminal voltage:  * and  * .     Reference: IEEE Standard 421.5-2005 Section 6.8.

	:kpr: Voltage regulator proportional gain (K).  Typical Value = 80. Default: 0.0
	:kir: Voltage regulator integral gain (K).  Typical Value = 5. Default: 0.0
	:kdr: Voltage regulator derivative gain (K).  Typical Value = 10. Default: 0.0
	:tdr: Lag time constant (T).  Typical Value = 0.1. Default: 0.0
	:vrmax: Maximum voltage regulator output (V).  Typical Value = 35. Default: 0.0
	:vrmin: Minimum voltage regulator output (V).  Typical Value = 0. Default: 0.0
	:ka: Voltage regulator gain (K).  Typical Value = 1. Default: 0.0
	:ta: Voltage regulator time constant (T).  Typical Value = 0. Default: 0.0
	:te: Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 1.2. Default: 0.0
	:vfemax: Exciter field current limit reference (V).  Typical Value = 6. Default: 0.0
	:vemin: Minimum exciter voltage output (V).  Typical Value = 0. Default: 0.0
	:ke: Exciter constant related to self-excited field (K).  Typical Value = 1. Default: 0.0
	:kc: Rectifier loading factor proportional to commutating reactance (K). Typical Value = 0.55. Default: 0.0
	:kd: Demagnetizing factor, a function of exciter alternator reactances (K).    Typical Value = 1.1. Default: 0.0
	:ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (V) equals V (V).  Typical Value = 6.5. Default: 0.0
	:seve1: Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 0.3. Default: 0.0
	:ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (V).  Typical Value = 9. Default: 0.0
	:seve2: Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance (S[V]).  Typical Value = 3. Default: 0.0
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

	readInProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, kpr = 0.0, kir = 0.0, kdr = 0.0, tdr = 0.0, vrmax = 0.0, vrmin = 0.0, ka = 0.0, ta = 0.0, te = 0.0, vfemax = 0.0, vemin = 0.0, ke = 0.0, kc = 0.0, kd = 0.0, ve1 = 0.0, seve1 = 0.0, ve2 = 0.0, seve2 = 0.0,  *args, **kw_args):
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
