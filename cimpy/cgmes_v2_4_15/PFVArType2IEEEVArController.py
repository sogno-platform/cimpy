from cimpy.output.PFVArControllerType2Dynamics import PFVArControllerType2Dynamics


class PFVArType2IEEEVArController(PFVArControllerType2Dynamics):
	'''
	The class represents IEEE VAR Controller Type 2 which is a summing point type controller. It makes up the outside loop of a two-loop system. This controller is implemented as a slow PI type controller, and the voltage regulator forms the inner loop and is implemented as a fast controller.  Reference: IEEE Standard 421.5-2005 Section 11.5.

	:qref: Reactive power reference (). Default: 
	:vref: Voltage regulator reference (). Default: 
	:vclmt: Maximum output of the pf controller (). Default: 
	:kp: Proportional gain of the pf controller (). Default: 
	:ki: Integral gain of the pf controller (). Default: 
	:vs: Generator sensing voltage (). Default: 
	:exlon: Overexcitation or under excitation flag () true = 1 (not in the overexcitation or underexcitation state, integral action is active) false = 0 (in the overexcitation or underexcitation state, so integral action is disabled to allow the limiter to play its role). Default: 
		'''

	cgmesProfile = PFVArControllerType2Dynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'qref': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vref': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vclmt': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'kp': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'ki': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vs': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'exlon': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PFVArControllerType2Dynamics: \n' + PFVArControllerType2Dynamics.__doc__ 

	def __init__(self, qref = , vref = , vclmt = , kp = , ki = , vs = , exlon = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.qref = qref
		self.vref = vref
		self.vclmt = vclmt
		self.kp = kp
		self.ki = ki
		self.vs = vs
		self.exlon = exlon
		
	def __str__(self):
		str = 'class=PFVArType2IEEEVArController\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
