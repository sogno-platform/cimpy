from cimpy.output.IdentifiedObject import IdentifiedObject


class WindContPType4bIEC(IdentifiedObject):
	'''
	P control model Type 4B.  Reference: IEC Standard 61400-27-1 Section 6.6.5.5.

	:dpmax: Maximum wind turbine power ramp rate (). It is project dependent parameter. Default: 
	:tpaero: Time constant in aerodynamic power response (). It is type dependent parameter. Default: 
	:tpord: Time constant in power order lag (). It is type dependent parameter. Default: 
	:tufilt: Voltage measurement filter time constant (). It is type dependent parameter. Default: 
	:WindTurbineType4bIEC: Wind turbine type 4B model with which this wind control P type 4B model is associated. Default: 
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'dpmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tpaero': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tpord': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'tufilt': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'WindTurbineType4bIEC': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, dpmax = , tpaero = , tpord = , tufilt = , WindTurbineType4bIEC = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.dpmax = dpmax
		self.tpaero = tpaero
		self.tpord = tpord
		self.tufilt = tufilt
		self.WindTurbineType4bIEC = WindTurbineType4bIEC
		
	def __str__(self):
		str = 'class=WindContPType4bIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
