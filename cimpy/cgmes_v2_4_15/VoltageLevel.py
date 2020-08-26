from cimpy.output.EquipmentContainer import EquipmentContainer


class VoltageLevel(EquipmentContainer):
	'''
	A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.

	:BaseVoltage: The base voltage used for all equipment within the voltage level. Default: 
	:Substation: The substation of the voltage level. Default: 
	:highVoltageLimit: The bus bar`s high voltage limit Default: 
	:lowVoltageLimit: The bus bar`s low voltage limit Default: 
	:Bays: The bays within this voltage level. Default: 
		'''

	cgmesProfile = EquipmentContainer.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'BaseVoltage': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'Substation': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'highVoltageLimit': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'lowVoltageLimit': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'Bays': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class EquipmentContainer: \n' + EquipmentContainer.__doc__ 

	def __init__(self, BaseVoltage = , Substation = , highVoltageLimit = , lowVoltageLimit = , Bays = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.BaseVoltage = BaseVoltage
		self.Substation = Substation
		self.highVoltageLimit = highVoltageLimit
		self.lowVoltageLimit = lowVoltageLimit
		self.Bays = Bays
		
	def __str__(self):
		str = 'class=VoltageLevel\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
