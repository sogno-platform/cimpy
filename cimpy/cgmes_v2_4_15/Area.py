from  import Base


class Area(Base):
	'''
	Area.

	:value:  Default: 
	:unit:  Default: 
	:multiplier:  Default: 
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'value': [cgmesProfile.DY.value, ],
						'unit': [cgmesProfile.DY.value, ],
						'multiplier': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, value = , unit = , multiplier = ,  ):
	
		self.value = value
		self.unit = unit
		self.multiplier = multiplier
		
	def __str__(self):
		str = 'class=Area\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
