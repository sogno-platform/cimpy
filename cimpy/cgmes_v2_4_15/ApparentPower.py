from .Base import Base


class ApparentPower(Base):
	'''
	Product of the RMS value of the voltage and the RMS value of the current.

	:value:  Default: 0.0
	:unit:  Default: None
	:multiplier:  Default: None
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.DY.value, ],
						'value': [cgmesProfile.EQ.value, cgmesProfile.DY.value, ],
						'unit': [cgmesProfile.EQ.value, cgmesProfile.DY.value, ],
						'multiplier': [cgmesProfile.EQ.value, cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	

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
