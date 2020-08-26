from cimpy.output.PFVArControllerType1Dynamics import PFVArControllerType1Dynamics


class PFVArType1IEEEVArController(PFVArControllerType1Dynamics):
	'''
	The class represents IEEE VAR Controller Type 1 which operates by moving the voltage reference directly.  Reference: IEEE Standard 421.5-2005 Section 11.3.

	:tvarc: Var controller time delay ().  Typical Value = 5. Default: 
	:vvar: Synchronous machine power factor (). Default: 
	:vvarcbw: Var controller dead band ().  Typical Value = 0.02. Default: 
	:vvarref: Var controller reference (). Default: 
	:vvtmax: Maximum machine terminal voltage needed for pf/var controller to be enabled (). Default: 
	:vvtmin: Minimum machine terminal voltage needed to enable pf/var controller (). Default: 
		'''

	cgmesProfile = PFVArControllerType1Dynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tvarc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vvar': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vvarcbw': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vvarref': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vvtmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'vvtmin': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PFVArControllerType1Dynamics: \n' + PFVArControllerType1Dynamics.__doc__ 

	def __init__(self, tvarc = , vvar = , vvarcbw = , vvarref = , vvtmax = , vvtmin = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.tvarc = tvarc
		self.vvar = vvar
		self.vvarcbw = vvarcbw
		self.vvarref = vvarref
		self.vvtmax = vvtmax
		self.vvtmin = vvtmin
		
	def __str__(self):
		str = 'class=PFVArType1IEEEVArController\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
