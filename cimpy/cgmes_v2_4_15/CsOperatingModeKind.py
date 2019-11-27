from cimpy.cgmes_v2_4_15.Base import Base


class CsOperatingModeKind(Base):
	'''
	Operating mode for HVDC line operating as Current Source Converter.

		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.SSH.value, ],
						 }

	readInProfile = {}

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=CsOperatingModeKind\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
