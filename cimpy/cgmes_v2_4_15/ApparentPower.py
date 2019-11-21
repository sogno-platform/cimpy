from cimpy.cgmes_v2_4_15_flat.Base import Base


class ApparentPower(Base):
	'''
	Product of the RMS value of the voltage and the RMS value of the current.

	:value:  Default: 0.0
	:unit:  Default: None
	:multiplier:  Default: None
		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, cgmesProfile.EQ.value, ],
						'value': [cgmesProfile.DY.value, cgmesProfile.EQ.value, ],
						'unit': [cgmesProfile.DY.value, cgmesProfile.EQ.value, ],
						'multiplier': [cgmesProfile.DY.value, cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	

	def __init__(self, value = 0.0, unit = None, multiplier = None,  ):
	
		self.value = value
		self.unit = unit
		self.multiplier = multiplier
		
	def __str__(self):
		str = 'class=ApparentPower\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
