from cimpy.output.WindTurbineType3or4Dynamics import WindTurbineType3or4Dynamics


class WindTurbineType3or4IEC(WindTurbineType3or4Dynamics):
	'''
	Parent class supporting relationships to IEC wind turbines Type 3 and 4 and wind plant including their control models.

	:WindContCurrLimIEC: Wind control current limitation model associated with this wind turbine type 3 or 4 model. Default: 
	:WIndContQIEC: Wind control Q model associated with this wind turbine type 3 or 4 model. Default: 
	:WindProtectionIEC: Wind turbune protection model associated with this wind generator type 3 or 4 model. Default: 
		'''

	cgmesProfile = WindTurbineType3or4Dynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'WindContCurrLimIEC': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'WIndContQIEC': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'WindProtectionIEC': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class WindTurbineType3or4Dynamics: \n' + WindTurbineType3or4Dynamics.__doc__ 

	def __init__(self, WindContCurrLimIEC = , WIndContQIEC = , WindProtectionIEC = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.WindContCurrLimIEC = WindContCurrLimIEC
		self.WIndContQIEC = WIndContQIEC
		self.WindProtectionIEC = WindProtectionIEC
		
	def __str__(self):
		str = 'class=WindTurbineType3or4IEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
