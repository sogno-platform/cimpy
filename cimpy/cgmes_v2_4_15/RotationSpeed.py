from cimpy.cgmes_v2_4_15_flat.Base import Base


class RotationSpeed(Base):
	'''
	Number of revolutions per second.

	:value:  Default: 0.0
	:unit:  Default: None
	:multiplier:  Default: None
	:denominatorUnit:  Default: None
	:denominatorMultiplier:  Default: None
		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'value': [cgmesProfile.EQ.value, ],
						'unit': [cgmesProfile.EQ.value, ],
						'multiplier': [cgmesProfile.EQ.value, ],
						'denominatorUnit': [cgmesProfile.EQ.value, ],
						'denominatorMultiplier': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	

	def __init__(self, value = 0.0, unit = None, multiplier = None, denominatorUnit = None, denominatorMultiplier = None,  ):
	
		self.value = value
		self.unit = unit
		self.multiplier = multiplier
		self.denominatorUnit = denominatorUnit
		self.denominatorMultiplier = denominatorMultiplier
		
	def __str__(self):
		str = 'class=RotationSpeed\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
