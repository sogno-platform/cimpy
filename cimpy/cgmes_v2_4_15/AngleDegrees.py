from .Base import Base


class AngleDegrees(Base):
	'''
	Measurement of angle in degrees.

	:value:  Default: 0.0
	:unit:  Default: None
	:multiplier:  Default: None
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DL.value, cgmesProfile.EQ.value, cgmesProfile.SSH.value, cgmesProfile.SV.value, cgmesProfile.DY.value, ],
						'value': [cgmesProfile.DL.value, cgmesProfile.EQ.value, cgmesProfile.SSH.value, cgmesProfile.SV.value, cgmesProfile.DY.value, ],
						'unit': [cgmesProfile.DL.value, cgmesProfile.EQ.value, cgmesProfile.SSH.value, cgmesProfile.SV.value, cgmesProfile.DY.value, ],
						'multiplier': [cgmesProfile.DL.value, cgmesProfile.EQ.value, cgmesProfile.SSH.value, cgmesProfile.SV.value, cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, value = 0.0, unit = None, multiplier = None,  ):
	
		self.value = value
		self.unit = unit
		self.multiplier = multiplier
		
	def __str__(self):
		str = 'class=AngleDegrees\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
