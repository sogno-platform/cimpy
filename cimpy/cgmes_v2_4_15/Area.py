from cimpy.cgmes_v2_4_15_flat.Base import Base


class Area(Base):
	'''
	Area.

	:value:  Default: 0.0
	:unit:  Default: None
	:multiplier:  Default: None
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'value': [cgmesProfile.DY.value, ],
						'unit': [cgmesProfile.DY.value, ],
						'multiplier': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	

	def __init__(self, value = 0.0, unit = None, multiplier = None,  ):
	
		self.value = value
		self.unit = unit
		self.multiplier = multiplier
		
	def __str__(self):
		str = 'class=Area\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
