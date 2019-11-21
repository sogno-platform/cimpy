from cimpy.cgmes_v2_4_15_flat.Base import Base


class DCConverterOperatingModeKind(Base):
	'''
	The operating mode of an HVDC bipole.

		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=DCConverterOperatingModeKind\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
