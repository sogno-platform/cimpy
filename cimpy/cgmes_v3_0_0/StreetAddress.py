from .Base import Base


class StreetAddress(Base):
	'''
	General purpose street and postal address information.

	:streetDetail: Street detail. Default: 0.0
	:townDetail: Town detail. Default: 0.0
	:status: Status of this address. Default: 0.0
	:postalCode: Postal code for the address. Default: ''
	:poBox: Post office box. Default: ''
	:language: The language in which the address is specified, using ISO 639-1 two digit language code. Default: ''
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.GL.value, ],
						'streetDetail': [cgmesProfile.GL.value, ],
						'townDetail': [cgmesProfile.GL.value, ],
						'status': [cgmesProfile.GL.value, ],
						'postalCode': [cgmesProfile.GL.value, ],
						'poBox': [cgmesProfile.GL.value, ],
						'language': [cgmesProfile.GL.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, streetDetail = 0.0, townDetail = 0.0, status = 0.0, postalCode = '', poBox = '', language = '',  ):
	
		self.streetDetail = streetDetail
		self.townDetail = townDetail
		self.status = status
		self.postalCode = postalCode
		self.poBox = poBox
		self.language = language
		
	def __str__(self):
		str = 'class=StreetAddress\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
