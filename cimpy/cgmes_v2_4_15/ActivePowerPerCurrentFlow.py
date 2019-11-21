from cimpy.cgmes_v2_4_15_flat.Base import Base


class ActivePowerPerCurrentFlow(Base):
	'''
	

	:denominatorMultiplier:  Default: None
	:denominatorUnit:  Default: None
	:multiplier:  Default: None
	:unit:  Default: None
	:value:  Default: 0.0
		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'denominatorMultiplier': [cgmesProfile.EQ.value, ],
						'denominatorUnit': [cgmesProfile.EQ.value, ],
						'multiplier': [cgmesProfile.EQ.value, ],
						'unit': [cgmesProfile.EQ.value, ],
						'value': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	

	def __init__(self, denominatorMultiplier = None, denominatorUnit = None, multiplier = None, unit = None, value = 0.0,  ):
	
		self.denominatorMultiplier = denominatorMultiplier
		self.denominatorUnit = denominatorUnit
		self.multiplier = multiplier
		self.unit = unit
		self.value = value
		
	def __str__(self):
		str = 'class=ActivePowerPerCurrentFlow\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
