from  import Base


class ResistancePerLength(Base):
	'''
	Resistance (real part of impedance) per unit of length.

	:value:  Default: 
	:unit:  Default: 
	:multiplier:  Default: 
	:denominatorUnit:  Default: 
	:denominatorMultiplier:  Default: 
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'value': [cgmesProfile.EQ.value, ],
						'unit': [cgmesProfile.EQ.value, ],
						'multiplier': [cgmesProfile.EQ.value, ],
						'denominatorUnit': [cgmesProfile.EQ.value, ],
						'denominatorMultiplier': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, value = , unit = , multiplier = , denominatorUnit = , denominatorMultiplier = ,  ):
	
		self.value = value
		self.unit = unit
		self.multiplier = multiplier
		self.denominatorUnit = denominatorUnit
		self.denominatorMultiplier = denominatorMultiplier
		
	def __str__(self):
		str = 'class=ResistancePerLength\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
