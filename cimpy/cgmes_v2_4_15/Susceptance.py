from  import Base


class Susceptance(Base):
	'''
	Imaginary part of admittance.

	:value:  Default: 
	:unit:  Default: 
	:multiplier:  Default: 
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'value': [cgmesProfile.EQ.value, ],
						'unit': [cgmesProfile.EQ.value, ],
						'multiplier': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, value = , unit = , multiplier = ,  ):
	
		self.value = value
		self.unit = unit
		self.multiplier = multiplier
		
	def __str__(self):
		str = 'class=Susceptance\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
