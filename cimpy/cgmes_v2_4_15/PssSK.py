from cimpy.output.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class PssSK(PowerSystemStabilizerDynamics):
	'''
	PSS Slovakian type - three inputs.

	:k1: Gain P (K1).  Typical Value = -0.3. Default: 
	:k2: Gain fe (K2).  Typical Value = -0.15. Default: 
	:k3: Gain If (K3).  Typical Value = 10. Default: 
	:t1: Denominator time constant (T1).  Typical Value = 0.3. Default: 
	:t2: Filter time constant (T2).  Typical Value = 0.35. Default: 
	:t3: Denominator time constant (T3).  Typical Value = 0.22. Default: 
	:t4: Filter time constant (T4).  Typical Value = 0.02. Default: 
	:t5: Denominator time constant (T5).  Typical Value = 0.02. Default: 
	:t6: Filter time constant (T6).  Typical Value = 0.02. Default: 
	:vsmax: Stabilizer output max limit (Vsmax).  Typical Value = 0.4. Default: 
	:vsmin: Stabilizer output min limit (Vsmin).  Typical Value = -0.4. Default: 
		'''

	cgmesProfile = PowerSystemStabilizerDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't4': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't5': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't6': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vsmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vsmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemStabilizerDynamics: \n' + PowerSystemStabilizerDynamics.__doc__ 

	def __init__(self, k1 = , k2 = , k3 = , t1 = , t2 = , t3 = , t4 = , t5 = , t6 = , vsmax = , vsmin = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.k1 = k1
		self.k2 = k2
		self.k3 = k3
		self.t1 = t1
		self.t2 = t2
		self.t3 = t3
		self.t4 = t4
		self.t5 = t5
		self.t6 = t6
		self.vsmax = vsmax
		self.vsmin = vsmin
		
	def __str__(self):
		str = 'class=PssSK\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
