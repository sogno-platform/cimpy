from cimpy.cgmes_v2_4_15_flat.Base import Base


class EquipmentVersion(Base):
	'''
	Version details.

	:baseUML: Base UML provided by CIM model manager. Default: ''
	:baseURIcore: Profile URI used in the Model Exchange header and defined in IEC standards.  It uniquely identifies the Profile and its version. It is given for information only and to identify the closest IEC profile to which this CGMES profile is based on. Default: ''
	:baseURIoperation: Profile URI used in the Model Exchange header and defined in IEC standards.  It uniquely identifies the Profile and its version. It is given for information only and to identify the closest IEC profile to which this CGMES profile is based on. Default: ''
	:baseURIshortCircuit: Profile URI used in the Model Exchange header and defined in IEC standards.  It uniquely identifies the Profile and its version. It is given for information only and to identify the closest IEC profile to which this CGMES profile is based on. Default: ''
	:date: Profile creation date Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05. Default: ''
	:differenceModelURI: Difference model URI defined by IEC 61970-552. Default: ''
	:entsoeUML: UML provided by ENTSO-E. Default: ''
	:entsoeURIcore: Profile URI defined by ENTSO-E and used in the Model Exchange header.  It uniquely identifies the Profile and its version. The last two elements in the URI (http://entsoe.eu/CIM/EquipmentCore/yy/zzz) indicate major and minor versions where:  - yy - indicates a major version; - zzz - indicates a minor version. Default: ''
	:entsoeURIoperation: Profile URI defined by ENTSO-E and used in the Model Exchange header.  It uniquely identifies the Profile and its version. The last two elements in the URI (http://entsoe.eu/CIM/EquipmentOperation/yy/zzz) indicate major and minor versions where:  - yy - indicates a major version; - zzz - indicates a minor version. Default: ''
	:entsoeURIshortCircuit: Profile URI defined by ENTSO-E and used in the Model Exchange header.  It uniquely identifies the Profile and its version. The last two elements in the URI (http://entsoe.eu/CIM/EquipmentShortCircuit/yy/zzz) indicate major and minor versions where:  - yy - indicates a major version; - zzz - indicates a minor version. Default: ''
	:modelDescriptionURI: Model Description URI defined by IEC 61970-552. Default: ''
	:namespaceRDF: RDF namespace. Default: ''
	:namespaceUML: CIM UML namespace. Default: ''
	:shortName: The short name of the profile used in profile documentation. Default: ''
		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'baseUML': [cgmesProfile.EQ.value, ],
						'baseURIcore': [cgmesProfile.EQ.value, ],
						'baseURIoperation': [cgmesProfile.EQ.value, ],
						'baseURIshortCircuit': [cgmesProfile.EQ.value, ],
						'date': [cgmesProfile.EQ.value, ],
						'differenceModelURI': [cgmesProfile.EQ.value, ],
						'entsoeUML': [cgmesProfile.EQ.value, ],
						'entsoeURIcore': [cgmesProfile.EQ.value, ],
						'entsoeURIoperation': [cgmesProfile.EQ.value, ],
						'entsoeURIshortCircuit': [cgmesProfile.EQ.value, ],
						'modelDescriptionURI': [cgmesProfile.EQ.value, ],
						'namespaceRDF': [cgmesProfile.EQ.value, ],
						'namespaceUML': [cgmesProfile.EQ.value, ],
						'shortName': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	

	def __init__(self, baseUML = '', baseURIcore = '', baseURIoperation = '', baseURIshortCircuit = '', date = '', differenceModelURI = '', entsoeUML = '', entsoeURIcore = '', entsoeURIoperation = '', entsoeURIshortCircuit = '', modelDescriptionURI = '', namespaceRDF = '', namespaceUML = '', shortName = '',  ):
	
		self.baseUML = baseUML
		self.baseURIcore = baseURIcore
		self.baseURIoperation = baseURIoperation
		self.baseURIshortCircuit = baseURIshortCircuit
		self.date = date
		self.differenceModelURI = differenceModelURI
		self.entsoeUML = entsoeUML
		self.entsoeURIcore = entsoeURIcore
		self.entsoeURIoperation = entsoeURIoperation
		self.entsoeURIshortCircuit = entsoeURIshortCircuit
		self.modelDescriptionURI = modelDescriptionURI
		self.namespaceRDF = namespaceRDF
		self.namespaceUML = namespaceUML
		self.shortName = shortName
		
	def __str__(self):
		str = 'class=EquipmentVersion\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
