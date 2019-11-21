from cimpy.cgmes_v2_4_15_flat.Base import Base


class Decimal(Base):
	'''
	Decimal is the base-10 notational system for representing real numbers.

		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=Decimal\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
