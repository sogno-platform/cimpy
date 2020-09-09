from .Base import Base


class ReactivePower(Base):
	'''
	Product of RMS value of the voltage and the RMS value of the quadrature component of the current.

	:value:  Default: 0.0
	:unit:  Default: None
	:multiplier:  Default: None
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.SSH.value, cgmesProfile.SV.value, ],
						'value': [cgmesProfile.EQ.value, cgmesProfile.SSH.value, cgmesProfile.SV.value, ],
						'unit': [cgmesProfile.EQ.value, cgmesProfile.SSH.value, cgmesProfile.SV.value, ],
						'multiplier': [cgmesProfile.EQ.value, cgmesProfile.SSH.value, cgmesProfile.SV.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, value = 0.0, unit = None, multiplier = None,  ):
	
		self.value = value
		self.unit = unit
		self.multiplier = multiplier
		
	def __str__(self):
		str = 'class=ReactivePower\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
