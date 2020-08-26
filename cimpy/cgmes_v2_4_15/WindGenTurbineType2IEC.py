from cimpy.output.WindTurbineType1or2IEC import WindTurbineType1or2IEC


class WindGenTurbineType2IEC(WindTurbineType1or2IEC):
	'''
	Wind turbine IEC Type 2.  Reference: IEC Standard 61400-27-1, section 6.5.3.

	:WindContRotorRIEC: Wind control rotor resistance model associated with wind turbine type 2 model. Default: 
	:WindPitchContEmulIEC: Pitch control emulator model associated with this wind turbine type 2 model. Default: 
		'''

	cgmesProfile = WindTurbineType1or2IEC.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'WindContRotorRIEC': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'WindPitchContEmulIEC': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class WindTurbineType1or2IEC: \n' + WindTurbineType1or2IEC.__doc__ 

	def __init__(self, WindContRotorRIEC = , WindPitchContEmulIEC = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.WindContRotorRIEC = WindContRotorRIEC
		self.WindPitchContEmulIEC = WindPitchContEmulIEC
		
	def __str__(self):
		str = 'class=WindGenTurbineType2IEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
