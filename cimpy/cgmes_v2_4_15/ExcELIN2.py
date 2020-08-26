from cimpy.output.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcELIN2(ExcitationSystemDynamics):
	'''
	Detailed Excitation System Model - ELIN (VATECH).  This model represents an all-static excitation system. A PI voltage controller establishes a desired field current set point for a proportional current controller. The integrator of the PI controller has a follow-up input to match its signal to the present field current.  Power system stabilizer models used in conjunction with this excitation system model: PssELIN2, PssIEEE2B, Pss2B.

	:k1: Voltage regulator input gain (K1).  Typical Value = 0. Default: 
	:k1ec: Voltage regulator input limit (K1ec).  Typical Value = 2. Default: 
	:kd1: Voltage controller derivative gain (Kd1).  Typical Value = 34.5. Default: 
	:tb1: Voltage controller derivative washout time constant (Tb1).  Typical Value = 12.45. Default: 
	:pid1max: Controller follow up gain (PID1max).  Typical Value = 2. Default: 
	:ti1: Controller follow up dead band (Ti1).  Typical Value = 0. Default: 
	:iefmax2: Minimum open circuit excitation voltage (Iefmax2).  Typical Value = -5. Default: 
	:k2: Gain (K2).  Typical Value = 5. Default: 
	:ketb: Gain (Ketb).  Typical Value = 0.06. Default: 
	:upmax: Limiter (Upmax).  Typical Value = 3. Default: 
	:upmin: Limiter (Upmin).  Typical Value = 0. Default: 
	:te: Time constant (Te).  Typical Value = 0. Default: 
	:xp: Excitation transformer effective reactance (Xp).  Typical Value = 1. Default: 
	:te2: Time Constant (Te2).  Typical Value = 1. Default: 
	:ke2: Gain (Ke2).  Typical Value = 0.1. Default: 
	:ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1).  Typical Value = 3. Default: 
	:seve1: Exciter saturation function value at the corresponding exciter voltage, Ve1, back of commutating reactance (Se[Ve1]).  Typical Value = 0. Default: 
	:ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve2).  Typical Value = 0. Default: 
	:seve2: Exciter saturation function value at the corresponding exciter voltage, Ve2, back of commutating reactance (Se[Ve2]).  Typical Value = 1. Default: 
	:tr4: Time constant (Tr4).  Typical Value = 1. Default: 
	:k3: Gain (K3).  Typical Value = 0.1. Default: 
	:ti3: Time constant (Ti3).  Typical Value = 3. Default: 
	:k4: Gain (K4).  Typical Value = 0. Default: 
	:ti4: Time constant (Ti4).  Typical Value = 0. Default: 
	:iefmax: Limiter (Iefmax).  Typical Value = 1. Default: 
	:iefmin: Limiter (Iefmin).  Typical Value = 1. Default: 
	:efdbas: Gain (Efdbas).  Typical Value = 0.1. Default: 
		'''

	cgmesProfile = ExcitationSystemDynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k1ec': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kd1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tb1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'pid1max': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ti1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'iefmax2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ketb': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'upmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'upmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'te': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'xp': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'te2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ke2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						've1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'seve1': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						've2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'seve2': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tr4': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ti3': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'k4': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ti4': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'iefmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'iefmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'efdbas': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, k1 = , k1ec = , kd1 = , tb1 = , pid1max = , ti1 = , iefmax2 = , k2 = , ketb = , upmax = , upmin = , te = , xp = , te2 = , ke2 = , ve1 = , seve1 = , ve2 = , seve2 = , tr4 = , k3 = , ti3 = , k4 = , ti4 = , iefmax = , iefmin = , efdbas = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.k1 = k1
		self.k1ec = k1ec
		self.kd1 = kd1
		self.tb1 = tb1
		self.pid1max = pid1max
		self.ti1 = ti1
		self.iefmax2 = iefmax2
		self.k2 = k2
		self.ketb = ketb
		self.upmax = upmax
		self.upmin = upmin
		self.te = te
		self.xp = xp
		self.te2 = te2
		self.ke2 = ke2
		self.ve1 = ve1
		self.seve1 = seve1
		self.ve2 = ve2
		self.seve2 = seve2
		self.tr4 = tr4
		self.k3 = k3
		self.ti3 = ti3
		self.k4 = k4
		self.ti4 = ti4
		self.iefmax = iefmax
		self.iefmin = iefmin
		self.efdbas = efdbas
		
	def __str__(self):
		str = 'class=ExcELIN2\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
