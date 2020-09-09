from .Base import Base


class IdentifiedObject(Base):
	'''
	This is a root class to provide common identification for all classes needing identification and naming attributes.

	:DiagramObjects: The domain object to which this diagram object is associated. Default: "list"
	:mRID: Master resource identifier issued by a model authority. The mRID is globally unique within an exchange context. Global uniqueness is easily achieved by using a UUID,  as specified in RFC 4122, for the mRID.  The use of UUID is strongly recommended. For CIMXML data files in RDF syntax conforming to IEC 61970-552 Edition 1, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. Default: ''
	:name: The name is any free human readable and possibly non unique text naming the object. Default: ''
	:description: The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. Default: ''
	:energyIdentCodeEic: The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. References: Default: ''
	:shortName: The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum. Default: ''
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DL.value, cgmesProfile.EQ.value, cgmesProfile.SSH.value, cgmesProfile.SV.value, cgmesProfile.GL.value, cgmesProfile.DY.value, cgmesProfile.TP.value, cgmesProfile.TP_BD.value, cgmesProfile.EQ_BD.value, ],
						'DiagramObjects': [cgmesProfile.DL.value, ],
						'mRID': [cgmesProfile.DL.value, cgmesProfile.EQ.value, cgmesProfile.SSH.value, cgmesProfile.SV.value, cgmesProfile.GL.value, cgmesProfile.DY.value, cgmesProfile.TP.value, cgmesProfile.TP_BD.value, cgmesProfile.EQ_BD.value, ],
						'name': [cgmesProfile.DL.value, cgmesProfile.EQ.value, cgmesProfile.SSH.value, cgmesProfile.SV.value, cgmesProfile.GL.value, cgmesProfile.DY.value, cgmesProfile.TP.value, cgmesProfile.TP_BD.value, cgmesProfile.EQ_BD.value, ],
						'description': [cgmesProfile.EQ.value, cgmesProfile.DY.value, cgmesProfile.TP.value, cgmesProfile.TP_BD.value, cgmesProfile.EQ_BD.value, ],
						'energyIdentCodeEic': [cgmesProfile.EQ.value, cgmesProfile.TP.value, cgmesProfile.TP_BD.value, cgmesProfile.EQ_BD.value, ],
						'shortName': [cgmesProfile.EQ.value, cgmesProfile.TP.value, cgmesProfile.TP_BD.value, cgmesProfile.EQ_BD.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, DiagramObjects = "list", mRID = '', name = '', description = '', energyIdentCodeEic = '', shortName = '',  ):
	
		self.DiagramObjects = DiagramObjects
		self.mRID = mRID
		self.name = name
		self.description = description
		self.energyIdentCodeEic = energyIdentCodeEic
		self.shortName = shortName
		
	def __str__(self):
		str = 'class=IdentifiedObject\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
