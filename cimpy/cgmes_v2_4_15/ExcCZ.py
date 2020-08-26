from cimpy.output.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcCZ(ExcitationSystemDynamics):
	'''
	Czech Proportion/Integral Exciter.

	:kp: Regulator proportional gain (Kp). Default: 
	:tc: Regulator integral time constant (Tc). Default: 
	:vrmax: Voltage regulator maximum limit (Vrmax). Default: 
	:vrmin: Voltage regulator minimum limit (Vrmin). Default: 
	:ka: Regulator gain (Ka). Default: 
	:ta: Regulator time constant (Ta). Default: 
	:ke: Exciter constant related to self-excited field (Ke). Default: 
	:te: Exciter time constant, integration rate associated with exciter control (Te). Default: 
	:efdmax: Exciter output maximum limit (Efdmax). Default: 
	:efdmin: Exciter output minimum limit (Efdmin). Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kp': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ka': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ta': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ke': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'te': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'efdmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'efdmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, kp = , tc = , vrmax = , vrmin = , ka = , ta = , ke = , te = , efdmax = , efdmin = ,  *args, **kw_args):
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
