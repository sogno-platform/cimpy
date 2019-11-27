from cimpy.cgmes_v2_4_15.Base import Base


class OperationalLimitDirectionKind(Base):
	'''
	The direction attribute describes the side of  a limit that is a violation.

		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=OperationalLimitDirectionKind\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
