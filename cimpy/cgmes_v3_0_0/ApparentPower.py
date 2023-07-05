from .Base import Base


class ApparentPower(Base):
	'''
	Product of the RMS value of the voltage and the RMS value of the current.

	:value:  Default: 0.0
	:multiplier:  Default: None
	:unit:  Default: None
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, cgmesProfile.SSH.value, cgmesProfile.EQ.value, ],
						'value': [cgmesProfile.DY.value, cgmesProfile.SSH.value, cgmesProfile.EQ.value, ],
						'multiplier': [cgmesProfile.DY.value, cgmesProfile.SSH.value, cgmesProfile.EQ.value, ],
						'unit': [cgmesProfile.DY.value, cgmesProfile.SSH.value, cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, value = 0.0, multiplier = None, unit = None,  ):
	
		self.value = value
		self.multiplier = multiplier
		self.unit = unit
		
	def __str__(self):
		str = 'class=ApparentPower\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
