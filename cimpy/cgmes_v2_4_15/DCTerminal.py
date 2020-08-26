from cimpy.output.DCBaseTerminal import DCBaseTerminal


class DCTerminal(DCBaseTerminal):
	'''
	An electrical connection point to generic DC conducting equipment.

	:DCConductingEquipment:  Default: 
		'''

	cgmesProfile = DCBaseTerminal.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'TP'}.value, ],
						'DCConductingEquipment': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class DCBaseTerminal: \n' + DCBaseTerminal.__doc__ 

	def __init__(self, DCConductingEquipment = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.DCConductingEquipment = DCConductingEquipment
		
	def __str__(self):
		str = 'class=DCTerminal\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
