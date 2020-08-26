from cimpy.output.RegulatingCondEq import RegulatingCondEq


class RotatingMachine(RegulatingCondEq):
	'''
	A rotating machine which may be used as a generator or motor.

	:GeneratingUnit: A synchronous machine may operate as a generator and as such becomes a member of a generating unit. Default: 
	:HydroPump: The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating. Default: 
	:ratedPowerFactor: Power factor (nameplate data). It is primarily used for short circuit data exchange according to IEC 60909. Default: 
	:ratedS: Nameplate apparent power rating for the unit. The attribute shall have a positive value. Default: 
	:ratedU: Rated voltage (nameplate data, Ur in IEC 60909-0). It is primarily used for short circuit data exchange according to IEC 60909. Default: 
	:p: Active power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution. Default: 
	:q: Reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution. Default: 
		'''

	cgmesProfile = RegulatingCondEq.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'GeneratingUnit': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'HydroPump': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'ratedPowerFactor': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'ratedS': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'ratedU': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'p': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						'q': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class RegulatingCondEq: \n' + RegulatingCondEq.__doc__ 

	def __init__(self, GeneratingUnit = , HydroPump = , ratedPowerFactor = , ratedS = , ratedU = , p = , q = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.GeneratingUnit = GeneratingUnit
		self.HydroPump = HydroPump
		self.ratedPowerFactor = ratedPowerFactor
		self.ratedS = ratedS
		self.ratedU = ratedU
		self.p = p
		self.q = q
		
	def __str__(self):
		str = 'class=RotatingMachine\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
