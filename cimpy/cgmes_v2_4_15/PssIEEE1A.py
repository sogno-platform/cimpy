from cimpy.output.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class PssIEEE1A(PowerSystemStabilizerDynamics):
	'''
	The class represents IEEE Std 421.5-2005 type PSS1A power system stabilizer model. PSS1A is the generalized form of a PSS with a single input. Some common stabilizer input signals are speed, frequency, and power.  Reference: IEEE 1A 421.5-2005 Section 8.1.

	:inputSignalType: Type of input signal.  Typical Value = rotorAngularFrequencyDeviation. Default: 
	:a1: PSS signal conditioning frequency filter constant (A1).  Typical Value = 0.061. Default: 
	:a2: PSS signal conditioning frequency filter constant (A2).  Typical Value = 0.0017. Default: 
	:t1: Lead/lag time constant (T1).  Typical Value = 0.3. Default: 
	:t2: Lead/lag time constant (T2).  Typical Value = 0.03. Default: 
	:t3: Lead/lag time constant (T3).  Typical Value = 0.3. Default: 
	:t4: Lead/lag time constant (T4).  Typical Value = 0.03. Default: 
	:t5: Washout time constant (T5).  Typical Value = 10. Default: 
	:t6: Transducer time constant (T6).  Typical Value = 0.01. Default: 
	:ks: Stabilizer gain (Ks).  Typical Value = 5. Default: 
	:vrmax: Maximum stabilizer output (Vrmax).  Typical Value = 0.05. Default: 
	:vrmin: Minimum stabilizer output (Vrmin).  Typical Value = -0.05. Default: 
		'''

	cgmesProfile = PowerSystemStabilizerDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'inputSignalType': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'a1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'a2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't4': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't5': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't6': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ks': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemStabilizerDynamics: \n' + PowerSystemStabilizerDynamics.__doc__ 

	def __init__(self, inputSignalType = , a1 = , a2 = , t1 = , t2 = , t3 = , t4 = , t5 = , t6 = , ks = , vrmax = , vrmin = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.inputSignalType = inputSignalType
		self.a1 = a1
		self.a2 = a2
		self.t1 = t1
		self.t2 = t2
		self.t3 = t3
		self.t4 = t4
		self.t5 = t5
		self.t6 = t6
		self.ks = ks
		self.vrmax = vrmax
		self.vrmin = vrmin
		
	def __str__(self):
		str = 'class=PssIEEE1A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
