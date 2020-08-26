from cimpy.output.WindTurbineType1or2Dynamics import WindTurbineType1or2Dynamics


class WindTurbineType1or2IEC(WindTurbineType1or2Dynamics):
	'''
	Generator model for wind turbine of IEC Type 1 or Type 2 is a standard asynchronous generator model.  Reference: IEC Standard 614000-27-1 Section 6.6.3.1.

	:WindMechIEC: Wind mechanical model associated with this wind generator type 1 or 2 model. Default: 
	:WindProtectionIEC: Wind turbune protection model associated with this wind generator type 1 or 2 model. Default: 
		'''

	cgmesProfile = WindTurbineType1or2Dynamics.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'WindMechIEC': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'WindProtectionIEC': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class WindTurbineType1or2Dynamics: \n' + WindTurbineType1or2Dynamics.__doc__ 

	def __init__(self, WindMechIEC = , WindProtectionIEC = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.WindMechIEC = WindMechIEC
		self.WindProtectionIEC = WindProtectionIEC
		
	def __str__(self):
		str = 'class=WindTurbineType1or2IEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
