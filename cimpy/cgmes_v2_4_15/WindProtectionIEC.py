from cimpy.output.IdentifiedObject import IdentifiedObject


class WindProtectionIEC(IdentifiedObject):
	'''
	The grid protection model includes protection against over and under voltage, and against over and under frequency.  Reference: IEC Standard 614000-27-1 Section 6.6.6.

	:fover: Set of wind turbine over frequency protection levels (). It is project dependent parameter. Default: 
	:funder: Set of wind turbine under frequency protection levels (). It is project dependent parameter. Default: 
	:tfover: Set of corresponding wind turbine over frequency protection disconnection times (). It is project dependent parameter. Default: 
	:tfunder: Set of corresponding wind turbine under frequency protection disconnection times (). It is project dependent parameter. Default: 
	:tuover: Set of corresponding wind turbine over voltage protection disconnection times (). It is project dependent parameter. Default: 
	:tuunder: Set of corresponding wind turbine under voltage protection disconnection times (). It is project dependent parameter. Default: 
	:uover: Set of wind turbine over voltage protection levels (). It is project dependent parameter. Default: 
	:uunder: Set of wind turbine under voltage protection levels (). It is project dependent parameter. Default: 
	:WindTurbineType3or4IEC: Wind generator type 3 or 4 model with which this wind turbine protection model is associated. Default: 
	:WindTurbineType1or2IEC: Wind generator type 1 or 2 model with which this wind turbine protection model is associated. Default: 
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'fover': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'funder': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tfover': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tfunder': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tuover': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tuunder': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'uover': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'uunder': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'WindTurbineType3or4IEC': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'WindTurbineType1or2IEC': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, fover = , funder = , tfover = , tfunder = , tuover = , tuunder = , uover = , uunder = , WindTurbineType3or4IEC = , WindTurbineType1or2IEC = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.fover = fover
		self.funder = funder
		self.tfover = tfover
		self.tfunder = tfunder
		self.tuover = tuover
		self.tuunder = tuunder
		self.uover = uover
		self.uunder = uunder
		self.WindTurbineType3or4IEC = WindTurbineType3or4IEC
		self.WindTurbineType1or2IEC = WindTurbineType1or2IEC
		
	def __str__(self):
		str = 'class=WindProtectionIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
