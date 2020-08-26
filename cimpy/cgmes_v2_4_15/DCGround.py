from cimpy.output.DCConductingEquipment import DCConductingEquipment


class DCGround(DCConductingEquipment):
	'''
	A ground within a DC system.

	:inductance: Inductance to ground. Default: 
	:r: Resistance to ground. Default: 
		'''

	cgmesProfile = DCConductingEquipment.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'inductance': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'r': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class DCConductingEquipment: \n' + DCConductingEquipment.__doc__ 

	def __init__(self, inductance = , r = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.inductance = inductance
		self.r = r
		
	def __str__(self):
		str = 'class=DCGround\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
