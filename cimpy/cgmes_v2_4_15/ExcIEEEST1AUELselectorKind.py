from cimpy.cgmes_v2_4_15.Base import Base


class ExcIEEEST1AUELselectorKind(Base):
	'''
	Type of connection for the UEL input used in ExcIEEEST1A.

		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=ExcIEEEST1AUELselectorKind\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
