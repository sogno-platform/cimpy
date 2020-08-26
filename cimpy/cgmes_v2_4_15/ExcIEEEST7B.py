from cimpy.output.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEST7B(ExcitationSystemDynamics):
	'''
	The class represents IEEE Std 421.5-2005 type ST7B model. This model is representative of static potential-source excitation systems. In this system, the AVR consists of a PI voltage regulator. A phase lead-lag filter in series allows introduction of a derivative function, typically used with brushless excitation systems. In that case, the regulator is of the PID type. In addition, the terminal voltage channel includes a phase lead-lag filter.  The AVR includes the appropriate inputs on its reference for overexcitation limiter (OEL1), underexcitation limiter (UEL), stator current limiter (SCL), and current compensator (DROOP). All these limitations, when they work at voltage reference level, keep the PSS (VS signal from Type PSS1A, PSS2A, or PSS2B) in operation. However, the UEL limitation can also be transferred to the high value (HV) gate acting on the output signal. In addition, the output signal passes through a low value (LV) gate for a ceiling overexcitation limiter (OEL2).  Reference: IEEE Standard 421.5-2005 Section 7.7.

	:kh: High-value gate feedback gain (K).  Typical Value 1. Default: 
	:kia: Voltage regulator integral gain (K).  Typical Value = 1. Default: 
	:kl: Low-value gate feedback gain (K).  Typical Value 1. Default: 
	:kpa: Voltage regulator proportional gain (K).  Typical Value = 40. Default: 
	:oelin: OEL input selector (OELin). Typical Value = noOELinput. Default: 
	:tb: Regulator lag time constant (T).  Typical Value 1. Default: 
	:tc: Regulator lead time constant (T).  Typical Value 1. Default: 
	:tf: Excitation control system stabilizer time constant (T).  Typical Value 1. Default: 
	:tg: Feedback time constant of inner loop field voltage regulator (T). Typical Value 1. Default: 
	:tia: Feedback time constant (T).  Typical Value = 3. Default: 
	:uelin: UEL input selector (UELin). Typical Value = noUELinput. Default: 
	:vmax: Maximum voltage reference signal (V).  Typical Value = 1.1. Default: 
	:vmin: Minimum voltage reference signal (V).  Typical Value = 0.9. Default: 
	:vrmax: Maximum voltage regulator output (V).  Typical Value = 5. Default: 
	:vrmin: Minimum voltage regulator output (V).  Typical Value = -4.5. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kh': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kia': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kl': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kpa': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'oelin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tb': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tf': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tg': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tia': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'uelin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, kh = , kia = , kl = , kpa = , oelin = , tb = , tc = , tf = , tg = , tia = , uelin = , vmax = , vmin = , vrmax = , vrmin = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.kh = kh
		self.kia = kia
		self.kl = kl
		self.kpa = kpa
		self.oelin = oelin
		self.tb = tb
		self.tc = tc
		self.tf = tf
		self.tg = tg
		self.tia = tia
		self.uelin = uelin
		self.vmax = vmax
		self.vmin = vmin
		self.vrmax = vrmax
		self.vrmin = vrmin
		
	def __str__(self):
		str = 'class=ExcIEEEST7B\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
