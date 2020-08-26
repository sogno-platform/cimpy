from cimpy.output.WindTurbineType3or4IEC import WindTurbineType3or4IEC


class WindGenTurbineType3IEC(WindTurbineType3or4IEC):
	'''
	Generator model for wind turbines of IEC type 3A and 3B.

	:WindAeroLinearIEC: Wind aerodynamic model associated with this wind generator type 3 model. Default: 
	:WindContPitchAngleIEC: Wind control pitch angle model associated with this wind turbine type 3. Default: 
	:WindContPType3IEC: Wind control P type 3 model associated with this wind turbine type 3 model. Default: 
	:dipmax: Maximum active current ramp rate (di). It is project dependent parameter. Default: 
	:diqmax: Maximum reactive current ramp rate (di). It is project dependent parameter. Default: 
	:WindMechIEC: Wind mechanical model associated with this wind turbine Type 3 model. Default: 
		'''

	cgmesProfile = WindTurbineType3or4IEC.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'WindAeroLinearIEC': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'WindContPitchAngleIEC': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'WindContPType3IEC': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'dipmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'diqmax': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'WindMechIEC': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class WindTurbineType3or4IEC: \n' + WindTurbineType3or4IEC.__doc__ 

	def __init__(self, WindAeroLinearIEC = , WindContPitchAngleIEC = , WindContPType3IEC = , dipmax = , diqmax = , WindMechIEC = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.WindAeroLinearIEC = WindAeroLinearIEC
		self.WindContPitchAngleIEC = WindContPitchAngleIEC
		self.WindContPType3IEC = WindContPType3IEC
		self.dipmax = dipmax
		self.diqmax = diqmax
		self.WindMechIEC = WindMechIEC
		
	def __str__(self):
		str = 'class=WindGenTurbineType3IEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
