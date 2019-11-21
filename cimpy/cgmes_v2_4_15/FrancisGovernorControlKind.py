from cimpy.cgmes_v2_4_15_flat.Base import Base


class FrancisGovernorControlKind(Base):
	'''
	Governor control flag for Francis hydro model.

		'''

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=FrancisGovernorControlKind\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
