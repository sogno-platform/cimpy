from cimpy.cgmes_v2_4_15.Base import Base


class VsPpccControlKind(Base):
	'''
	Types applicable to the control of real power and/or DC voltage by voltage source converter.

		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.SSH.value, ],
						 }

	readInProfile = {}

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=VsPpccControlKind\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
