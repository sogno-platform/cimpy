from cimpy.output.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class Pss1A(PowerSystemStabilizerDynamics):
	'''
	Single input power system stabilizer. It is a modified version in order to allow representation of various vendors' implementations on PSS type 1A.

	:inputSignalType: Type of input signal. Default: 
	:a1: Notch filter parameter (A1). Default: 
	:a2: Notch filter parameter (A2). Default: 
	:t1: Lead/lag time constant (T1). Default: 
	:t2: Lead/lag time constant (T2). Default: 
	:t3: Lead/lag time constant (T3). Default: 
	:t4: Lead/lag time constant (T4). Default: 
	:t5: Washout time constant (T5). Default: 
	:t6: Transducer time constant (T6). Default: 
	:ks: Stabilizer gain (Ks). Default: 
	:vrmax: Maximum stabilizer output (Vrmax). Default: 
	:vrmin: Minimum stabilizer output (Vrmin). Default: 
	:vcu: Stabilizer input cutoff threshold (Vcu). Default: 
	:vcl: Stabilizer input cutoff threshold (Vcl). Default: 
	:a3: Notch filter parameter (A3). Default: 
	:a4: Notch filter parameter (A4). Default: 
	:a5: Notch filter parameter (A5). Default: 
	:a6: Notch filter parameter (A6). Default: 
	:a7: Notch filter parameter (A7). Default: 
	:a8: Notch filter parameter (A8). Default: 
	:kd: Selector (Kd).  true = e used false = e not used. Default: 
	:tdelay: Time constant (Tdelay). Default: 
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
						'vcu': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vcl': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'a3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'a4': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'a5': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'a6': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'a7': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'a8': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kd': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tdelay': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemStabilizerDynamics: \n' + PowerSystemStabilizerDynamics.__doc__ 

	def __init__(self, inputSignalType = , a1 = , a2 = , t1 = , t2 = , t3 = , t4 = , t5 = , t6 = , ks = , vrmax = , vrmin = , vcu = , vcl = , a3 = , a4 = , a5 = , a6 = , a7 = , a8 = , kd = , tdelay = ,  *args, **kw_args):
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
		self.vcu = vcu
		self.vcl = vcl
		self.a3 = a3
		self.a4 = a4
		self.a5 = a5
		self.a6 = a6
		self.a7 = a7
		self.a8 = a8
		self.kd = kd
		self.tdelay = tdelay
		
	def __str__(self):
		str = 'class=Pss1A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
