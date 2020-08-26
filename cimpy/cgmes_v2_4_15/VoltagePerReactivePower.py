from  import Base


class VoltagePerReactivePower(Base):
	'''
	Voltage variation with reactive power.

	:value:  Default: 
	:unit:  Default: 
	:denominatorMultiplier:  Default: 
	:multiplier:  Default: 
	:denominatorUnit:  Default: 
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'value': [cgmesProfile.EQ.value, ],
						'unit': [cgmesProfile.EQ.value, ],
						'denominatorMultiplier': [cgmesProfile.EQ.value, ],
						'multiplier': [cgmesProfile.EQ.value, ],
						'denominatorUnit': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, value = , unit = , denominatorMultiplier = , multiplier = , denominatorUnit = ,  ):
	
		self.value = value
		self.unit = unit
		self.denominatorMultiplier = denominatorMultiplier
		self.multiplier = multiplier
		self.denominatorUnit = denominatorUnit
		
	def __str__(self):
		str = 'class=VoltagePerReactivePower\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
