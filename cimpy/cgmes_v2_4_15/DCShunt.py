from cimpy.output.DCConductingEquipment import DCConductingEquipment


class DCShunt(DCConductingEquipment):
	'''
	A shunt device within the DC system, typically used for filtering.  Needed for transient and short circuit studies.

	:capacitance: Capacitance of the DC shunt. Default: 
	:resistance: Resistance of the DC device. Default: 
	:ratedUdc: Rated DC device voltage. Converter configuration data used in power flow. Default: 
		'''

	cgmesProfile = DCConductingEquipment.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'capacitance': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'resistance': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'ratedUdc': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class DCConductingEquipment: \n' + DCConductingEquipment.__doc__ 

	def __init__(self, capacitance = , resistance = , ratedUdc = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.capacitance = capacitance
		self.resistance = resistance
		self.ratedUdc = ratedUdc
		
	def __str__(self):
		str = 'class=DCShunt\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
