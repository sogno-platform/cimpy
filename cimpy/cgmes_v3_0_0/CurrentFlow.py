from .Base import Base


class CurrentFlow(Base):
	'''
	Electrical current with sign convention: positive flow is out of the conducting equipment into the connectivity node. Can be both AC and DC.

	:value:  Default: 0.0
	:multiplier:  Default: None
	:unit:  Default: None
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.SSH.value, cgmesProfile.EQ.value, cgmesProfile.SC.value, cgmesProfile.SV.value, ],
						'value': [cgmesProfile.SSH.value, cgmesProfile.EQ.value, cgmesProfile.SC.value, cgmesProfile.SV.value, ],
						'multiplier': [cgmesProfile.SSH.value, cgmesProfile.EQ.value, cgmesProfile.SC.value, cgmesProfile.SV.value, ],
						'unit': [cgmesProfile.SSH.value, cgmesProfile.EQ.value, cgmesProfile.SC.value, cgmesProfile.SV.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, value = 0.0, multiplier = None, unit = None,  ):
	
		self.value = value
		self.multiplier = multiplier
		self.unit = unit
		
	def __str__(self):
		str = 'class=CurrentFlow\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
