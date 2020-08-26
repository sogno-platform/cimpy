from  import Base


class Temperature(Base):
	'''
	Value of temperature in degrees Celsius.

	:multiplier:  Default: 
	:unit:  Default: 
	:value:  Default: 
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.DY.value, ],
						'multiplier': [cgmesProfile.EQ.value, cgmesProfile.DY.value, ],
						'unit': [cgmesProfile.EQ.value, cgmesProfile.DY.value, ],
						'value': [cgmesProfile.EQ.value, cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, multiplier = , unit = , value = ,  ):
	
		self.multiplier = multiplier
		self.unit = unit
		self.value = value
		
	def __str__(self):
		str = 'class=Temperature\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
