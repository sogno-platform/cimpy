from cimpy.cgmes_v2_4_15_flat.Base import Base


class ExcST7BOELselectorKind(Base):
	'''
	Type of connection for the OEL input used for static excitation systems type 7B.

		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=ExcST7BOELselectorKind\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
