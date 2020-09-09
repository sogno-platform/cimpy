from .Base import Base


class Simple_Float(Base):
	'''
	A floating point number. The range is unspecified and not limited.

	:value:  Default: 0.0
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DL.value, cgmesProfile.EQ.value, cgmesProfile.SSH.value, cgmesProfile.SV.value, cgmesProfile.DY.value, ],
						'value': [cgmesProfile.DL.value, cgmesProfile.EQ.value, cgmesProfile.SSH.value, cgmesProfile.SV.value, cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, value = 0.0,  ):
	
		self.value = value
		
	def __str__(self):
		str = 'class=Simple_Float\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
