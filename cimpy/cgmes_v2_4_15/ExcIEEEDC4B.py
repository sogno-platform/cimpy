from cimpy.output.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEDC4B(ExcitationSystemDynamics):
	'''
	The class represents IEEE Std 421.5-2005 type DC4B model. These excitation systems utilize a field-controlled dc commutator exciter with a continuously acting voltage regulator having supplies obtained from the generator or auxiliary bus.  Reference: IEEE Standard 421.5-2005 Section 5.4.

	:ka: Voltage regulator gain (K).  Typical Value = 1. Default: 
	:ta: Voltage regulator time constant (T).  Typical Value = 0.2. Default: 
	:kp: Regulator proportional gain (K).  Typical Value = 20. Default: 
	:ki: Regulator integral gain (K).  Typical Value = 20. Default: 
	:kd: Regulator derivative gain (K).  Typical Value = 20. Default: 
	:td: Regulator derivative filter time constant(T).  Typical Value = 0.01. Default: 
	:vrmax: Maximum voltage regulator output (V).  Typical Value = 2.7. Default: 
	:vrmin: Minimum voltage regulator output (V).  Typical Value = -0.9. Default: 
	:ke: Exciter constant related to self-excited field (K).  Typical Value = 1. Default: 
	:te: Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 0.8. Default: 
	:kf: Excitation control system stabilizer gain (K).  Typical Value = 0. Default: 
	:tf: Excitation control system stabilizer time constant (T).  Typical Value = 1. Default: 
	:efd1: Exciter voltage at which exciter saturation is defined (E).  Typical Value = 1.75. Default: 
	:seefd1: Exciter saturation function value at the corresponding exciter voltage, E (S[E]).  Typical Value = 0.08. Default: 
	:efd2: Exciter voltage at which exciter saturation is defined (E).  Typical Value = 2.33. Default: 
	:seefd2: Exciter saturation function value at the corresponding exciter voltage, E (S[E]).  Typical Value = 0.27. Default: 
	:vemin: Minimum exciter voltage output(V).  Typical Value = 0. Default: 
	:oelin: OEL input (OELin). true = LV gate false = subtract from error signal. Typical Value = true. Default: 
	:uelin: UEL input (UELin). true = HV gate false = add to error signal. Typical Value = true. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ka': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ta': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kp': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ki': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kd': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'td': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ke': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'te': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kf': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tf': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'efd1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'seefd1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'efd2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'seefd2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vemin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'oelin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'uelin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ka = , ta = , kp = , ki = , kd = , td = , vrmax = , vrmin = , ke = , te = , kf = , tf = , efd1 = , seefd1 = , efd2 = , seefd2 = , vemin = , oelin = , uelin = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ka = ka
		self.ta = ta
		self.kp = kp
		self.ki = ki
		self.kd = kd
		self.td = td
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
		self.vemin = vemin
		self.oelin = oelin
		self.uelin = uelin
		
	def __str__(self):
		str = 'class=ExcIEEEDC4B\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
