from cimpy.cgmes_v2_4_15_flat.Base import Base


class InputSignalKind(Base):
	'''
	Input signal type.  In Dynamics modelling, commonly represented by j parameter.

		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=InputSignalKind\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
