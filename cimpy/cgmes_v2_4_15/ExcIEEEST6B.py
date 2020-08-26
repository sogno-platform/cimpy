from cimpy.output.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIEEEST6B(ExcitationSystemDynamics):
	'''
	The class represents IEEE Std 421.5-2005 type ST6B model. This model consists of a PI voltage regulator with an inner loop field voltage regulator and pre-control. The field voltage regulator implements a proportional control. The pre-control and the delay in the feedback circuit increase the dynamic response.  Reference: IEEE Standard 421.5-2005 Section 7.6.

	:ilr: Exciter output current limit reference (I).  Typical Value = 4.164. Default: 
	:kci: Exciter output current limit adjustment (K).  Typical Value = 1.0577. Default: 
	:kff: Pre-control gain constant of the inner loop field regulator (K). Typical Value = 1. Default: 
	:kg: Feedback gain constant of the inner loop field regulator (K).  Typical Value = 1. Default: 
	:kia: Voltage regulator integral gain (K).  Typical Value = 45.094. Default: 
	:klr: Exciter output current limiter gain (K).  Typical Value = 17.33. Default: 
	:km: Forward gain constant of the inner loop field regulator (K).  Typical Value = 1. Default: 
	:kpa: Voltage regulator proportional gain (K).  Typical Value = 18.038. Default: 
	:oelin: OEL input selector (OELin). Typical Value = noOELinput. Default: 
	:tg: Feedback time constant of inner loop field voltage regulator (T). Typical Value = 0.02. Default: 
	:vamax: Maximum voltage regulator output (V).  Typical Value = 4.81. Default: 
	:vamin: Minimum voltage regulator output (V).  Typical Value = -3.85. Default: 
	:vrmax: Maximum voltage regulator output (V).  Typical Value = 4.81. Default: 
	:vrmin: Minimum voltage regulator output (V).  Typical Value = -3.85. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ilr': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kci': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kff': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kg': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kia': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'klr': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'km': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kpa': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'oelin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tg': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vamax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vamin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ilr = , kci = , kff = , kg = , kia = , klr = , km = , kpa = , oelin = , tg = , vamax = , vamin = , vrmax = , vrmin = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ilr = ilr
		self.kci = kci
		self.kff = kff
		self.kg = kg
		self.kia = kia
		self.klr = klr
		self.km = km
		self.kpa = kpa
		self.oelin = oelin
		self.tg = tg
		self.vamax = vamax
		self.vamin = vamin
		self.vrmax = vrmax
		self.vrmin = vrmin
		
	def __str__(self):
		str = 'class=ExcIEEEST6B\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
