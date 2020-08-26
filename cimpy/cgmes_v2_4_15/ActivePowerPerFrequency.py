from  import Base


class ActivePowerPerFrequency(Base):
	'''
	Active power variation with frequency.

	:denominatorMultiplier:  Default: 
	:denominatorUnit:  Default: 
	:multiplier:  Default: 
	:unit:  Default: 
	:value:  Default: 
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'denominatorMultiplier': [cgmesProfile.EQ.value, ],
						'denominatorUnit': [cgmesProfile.EQ.value, ],
						'multiplier': [cgmesProfile.EQ.value, ],
						'unit': [cgmesProfile.EQ.value, ],
						'value': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, denominatorMultiplier = , denominatorUnit = , multiplier = , unit = , value = ,  ):
	
		self.denominatorMultiplier = denominatorMultiplier
		self.denominatorUnit = denominatorUnit
		self.multiplier = multiplier
		self.unit = unit
		self.value = value
		
	def __str__(self):
		str = 'class=ActivePowerPerFrequency\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
