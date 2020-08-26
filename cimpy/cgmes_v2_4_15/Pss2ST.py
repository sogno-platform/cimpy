from cimpy.output.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class Pss2ST(PowerSystemStabilizerDynamics):
	'''
	PTI Microprocessor-Based Stabilizer type 1.

	:inputSignal1Type: Type of input signal #1.  Typical Value = rotorAngularFrequencyDeviation. Default: 
	:inputSignal2Type: Type of input signal #2.  Typical Value = generatorElectricalPower. Default: 
	:k1: Gain (K1). Default: 
	:k2: Gain (K2). Default: 
	:t1: Time constant (T1). Default: 
	:t2: Time constant (T2). Default: 
	:t3: Time constant (T3). Default: 
	:t4: Time constant (T4). Default: 
	:t5: Time constant (T5). Default: 
	:t6: Time constant (T6). Default: 
	:t7: Time constant (T7). Default: 
	:t8: Time constant (T8). Default: 
	:t9: Time constant (T9). Default: 
	:t10: Time constant (T10). Default: 
	:lsmax: Limiter (Lsmax). Default: 
	:lsmin: Limiter (Lsmin). Default: 
	:vcu: Cutoff limiter (Vcu). Default: 
	:vcl: Cutoff limiter (Vcl). Default: 
		'''

	cgmesProfile = PowerSystemStabilizerDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'inputSignal1Type': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'inputSignal2Type': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't4': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't5': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't6': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't7': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't8': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't9': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't10': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'lsmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'lsmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vcu': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vcl': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemStabilizerDynamics: \n' + PowerSystemStabilizerDynamics.__doc__ 

	def __init__(self, inputSignal1Type = , inputSignal2Type = , k1 = , k2 = , t1 = , t2 = , t3 = , t4 = , t5 = , t6 = , t7 = , t8 = , t9 = , t10 = , lsmax = , lsmin = , vcu = , vcl = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.inputSignal1Type = inputSignal1Type
		self.inputSignal2Type = inputSignal2Type
		self.k1 = k1
		self.k2 = k2
		self.t1 = t1
		self.t2 = t2
		self.t3 = t3
		self.t4 = t4
		self.t5 = t5
		self.t6 = t6
		self.t7 = t7
		self.t8 = t8
		self.t9 = t9
		self.t10 = t10
		self.lsmax = lsmax
		self.lsmin = lsmin
		self.vcu = vcu
		self.vcl = vcl
		
	def __str__(self):
		str = 'class=Pss2ST\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
