from  import Base


class Frequency(Base):
	'''
	Cycles per second.

	:value:  Default: 
	:unit:  Default: 
	:multiplier:  Default: 
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.DY.value, ],
						'value': [cgmesProfile.EQ.value, cgmesProfile.DY.value, ],
						'unit': [cgmesProfile.EQ.value, cgmesProfile.DY.value, ],
						'multiplier': [cgmesProfile.EQ.value, cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, value = , unit = , multiplier = ,  ):
	
		self.value = value
		self.unit = unit
		self.multiplier = multiplier
		
	def __str__(self):
		str = 'class=Frequency\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
