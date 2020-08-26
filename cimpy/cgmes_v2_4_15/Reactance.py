from  import Base


class Reactance(Base):
	'''
	Reactance (imaginary part of impedance), at rated frequency.

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
		str = 'class=Reactance\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
