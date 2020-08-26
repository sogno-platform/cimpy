from cimpy.output.ConductingEquipment import ConductingEquipment


class RegulatingCondEq(ConductingEquipment):
	'''
	A type of conducting equipment that can regulate a quantity (i.e. voltage or flow) at a specific point in the network.

	:RegulatingControl: The regulating control scheme in which this equipment participates. Default: 
	:controlEnabled: Specifies the regulation status of the equipment.  True is regulating, false is not regulating. Default: 
		'''

	cgmesProfile = ConductingEquipment.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'DY'}.value, ],
						'RegulatingControl': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'controlEnabled': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'SSH'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class ConductingEquipment: \n' + ConductingEquipment.__doc__ 

	def __init__(self, RegulatingControl = , controlEnabled = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.RegulatingControl = RegulatingControl
		self.controlEnabled = controlEnabled
		
	def __str__(self):
		str = 'class=RegulatingCondEq\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
