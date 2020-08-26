from cimpy.output.DCEquipmentContainer import DCEquipmentContainer


class DCConverterUnit(DCEquipmentContainer):
	'''
	Indivisible operative unit comprising all equipment between the point of common coupling on the AC side and the point of common coupling - DC side, essentially one or more converters, together with one or more converter transformers, converter control equipment, essential protective and switching devices and auxiliaries, if any, used for conversion.

	:operationMode:  Default: 
	:Substation:  Default: 
		'''

	cgmesProfile = DCEquipmentContainer.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'operationMode': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						'Substation': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ'}.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class DCEquipmentContainer: \n' + DCEquipmentContainer.__doc__ 

	def __init__(self, operationMode = , Substation = ,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.operationMode = operationMode
		self.Substation = Substation
		
	def __str__(self):
		str = 'class=DCConverterUnit\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
