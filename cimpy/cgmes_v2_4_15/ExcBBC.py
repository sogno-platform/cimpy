from cimpy.output.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcBBC(ExcitationSystemDynamics):
	'''
	Transformer fed static excitation system (static with ABB regulator). This model represents a static excitation system in which a gated thyristor bridge fed by a transformer at the main generator terminals feeds the main generator directly.

	:t1: Controller time constant (T1).  Typical Value = 6. Default: 
	:t2: Controller time constant (T2).  Typical Value = 1. Default: 
	:t3: Lead/lag time constant (T3).  Typical Value = 0.05. Default: 
	:t4: Lead/lag time constant (T4).  Typical Value = 0.01. Default: 
	:k: Steady state gain (K).  Typical Value = 300. Default: 
	:vrmin: Minimum control element output (Vrmin).  Typical Value = -5. Default: 
	:vrmax: Maximum control element output (Vrmax).  Typical Value = 5. Default: 
	:efdmin: Minimum open circuit exciter voltage (Efdmin).  Typical Value = -5. Default: 
	:efdmax: Maximum open circuit exciter voltage (Efdmax).  Typical Value = 5. Default: 
	:xe: Effective excitation transformer reactance (Xe).  Typical Value = 0.05. Default: 
	:switch: Supplementary signal routing selector (switch). true = Vs connected to 3rd summing point false =  Vs connected to 1st summing point (see diagram). Typical Value = true. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						't4': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vrmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'efdmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'efdmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'xe': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'switch': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, t1 = , t2 = , t3 = , t4 = , k = , vrmin = , vrmax = , efdmin = , efdmax = , xe = , switch = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.t1 = t1
		self.t2 = t2
		self.t3 = t3
		self.t4 = t4
		self.k = k
		self.vrmin = vrmin
		self.vrmax = vrmax
		self.efdmin = efdmin
		self.efdmax = efdmax
		self.xe = xe
		self.switch = switch
		
	def __str__(self):
		str = 'class=ExcBBC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
