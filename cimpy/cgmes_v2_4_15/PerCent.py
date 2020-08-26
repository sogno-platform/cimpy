from  import Base


class PerCent(Base):
	'''
	Percentage on a defined base.   For example, specify as 100 to indicate at the defined base.

	:value: Normally 0 - 100 on a defined base Default: 
	:unit:  Default: 
	:multiplier:  Default: 
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.SSH.value, ],
						'value': [cgmesProfile.EQ.value, cgmesProfile.SSH.value, ],
						'unit': [cgmesProfile.EQ.value, cgmesProfile.SSH.value, ],
						'multiplier': [cgmesProfile.EQ.value, cgmesProfile.SSH.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, value = , unit = , multiplier = ,  ):
	
		self.value = value
		self.unit = unit
		self.multiplier = multiplier
		
	def __str__(self):
		str = 'class=PerCent\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
