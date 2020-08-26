from cimpy.output.DCConductingEquipment import DCConductingEquipment


class DCLineSegment(DCConductingEquipment):
	'''
	A wire or combination of wires not insulated from one another, with consistent electrical characteristics, used to carry direct current between points in the DC region of the power system.

	:capacitance: Capacitance of the DC line segment. Significant for cables only. Default: 
	:inductance: Inductance of the DC line segment. Neglectable compared with DCSeriesDevice used for smoothing. Default: 
	:resistance: Resistance of the DC line segment. Default: 
	:length: Segment length for calculating line section capabilities. Default: 
	:PerLengthParameter: Set of per-length parameters for this line segment. Default: 
		'''

	cgmesProfile = DCConductingEquipment.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'capacitance': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'inductance': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'resistance': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'length': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'PerLengthParameter': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class DCConductingEquipment: \n' + DCConductingEquipment.__doc__ 

	def __init__(self, capacitance = , inductance = , resistance = , length = , PerLengthParameter = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.capacitance = capacitance
		self.inductance = inductance
		self.resistance = resistance
		self.length = length
		self.PerLengthParameter = PerLengthParameter
		
	def __str__(self):
		str = 'class=DCLineSegment\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
