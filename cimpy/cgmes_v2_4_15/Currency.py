from cimpy.cgmes_v2_4_15_flat.Base import Base


class Currency(Base):
	'''
	Monetary currencies. Apologies for this list not being exhaustive.

		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=Currency\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
