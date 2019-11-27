from cimpy.cgmes_v2_4_15.Base import Base


class Simple_Float(Base):
	'''
	A floating point number. The range is unspecified and not limited.

	:value:  Default: 0.0
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DI.value, cgmesProfile.DY.value, cgmesProfile.EQ.value, cgmesProfile.SV.value, cgmesProfile.SSH.value, ],
						'value': [cgmesProfile.DI.value, cgmesProfile.DY.value, cgmesProfile.EQ.value, cgmesProfile.SV.value, cgmesProfile.SSH.value, ],
						 }

	readInProfile = {}

	

	def __init__(self, value = 0.0,  ):
	
		self.value = value
		
	def __str__(self):
		str = 'class=Simple_Float\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
