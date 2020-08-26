from  import Base


class EquipmentBoundaryVersion(Base):
	'''
	Profile version details.

	:baseUML: Base UML provided by CIM model manager. Default: 
	:baseURI: Profile URI used in the Model Exchange header and defined in IEC standards.  It uniquely identifies the Profile and its version. It is given for information only and to identify the closest IEC profile to which this CGMES profile is based on. Default: 
	:date: Profile creation date Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05. Default: 
	:differenceModelURI: Difference model URI defined by IEC 61970-552. Default: 
	:entsoeUML: UML provided by ENTSO-E. Default: 
	:entsoeURIcore: Profile URI defined by ENTSO-E and used in the Model Exchange header.  It uniquely identifies the Profile and its version. The last two elements in the URI (http://entsoe.eu/CIM/EquipmentBoundary/yy/zzz) indicate major and minor versions where:  - yy - indicates a major version; - zzz - indicates a minor version. Default: 
	:entsoeURIoperation: Profile URI defined by ENTSO-E and used in the Model Exchange header.  It uniquely identifies the Profile and its version. The last two elements in the URI (http://entsoe.eu/CIM/EquipmentBoundaryOperation/yy/zzz) indicate major and minor versions where:  - yy - indicates a major version; - zzz - indicates a minor version. Default: 
	:modelDescriptionURI: Model Description URI defined by IEC 61970-552. Default: 
	:namespaceRDF: RDF namespace. Default: 
	:namespaceUML: CIM UML namespace. Default: 
	:shortName: The short name of the profile used in profile documentation. Default: 
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ_BD'}.value, ],
						'baseUML': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ_BD'}.value, ],
						'baseURI': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ_BD'}.value, ],
						'date': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ_BD'}.value, ],
						'differenceModelURI': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ_BD'}.value, ],
						'entsoeUML': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ_BD'}.value, ],
						'entsoeURIcore': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ_BD'}.value, ],
						'entsoeURIoperation': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ_BD'}.value, ],
						'modelDescriptionURI': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ_BD'}.value, ],
						'namespaceRDF': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ_BD'}.value, ],
						'namespaceUML': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ_BD'}.value, ],
						'shortName': [cgmesProfile.{'$rdf:datatype': 'http://www.w3.org/2001/XMLSchema#string', '_': 'EQ_BD'}.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, baseUML = , baseURI = , date = , differenceModelURI = , entsoeUML = , entsoeURIcore = , entsoeURIoperation = , modelDescriptionURI = , namespaceRDF = , namespaceUML = , shortName = ,  ):
	
		self.baseUML = baseUML
		self.baseURI = baseURI
		self.date = date
		self.differenceModelURI = differenceModelURI
		self.entsoeUML = entsoeUML
		self.entsoeURIcore = entsoeURIcore
		self.entsoeURIoperation = entsoeURIoperation
		self.modelDescriptionURI = modelDescriptionURI
		self.namespaceRDF = namespaceRDF
		self.namespaceUML = namespaceUML
		self.shortName = shortName
		
	def __str__(self):
		str = 'class=EquipmentBoundaryVersion\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
