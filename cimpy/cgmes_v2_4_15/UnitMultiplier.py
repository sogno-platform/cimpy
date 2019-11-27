from cimpy.cgmes_v2_4_15.Base import Base


class UnitMultiplier(Base):
	'''
	The unit multipliers defined for the CIM.

		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DI.value, cgmesProfile.DY.value, cgmesProfile.EQ.value, cgmesProfile.SV.value, cgmesProfile.SSH.value, ],
						 }

	readInProfile = {}

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=UnitMultiplier\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
