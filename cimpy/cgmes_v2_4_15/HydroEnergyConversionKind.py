from cimpy.cgmes_v2_4_15_flat.Base import Base


class HydroEnergyConversionKind(Base):
	'''
	Specifies the capability of the hydro generating unit to convert energy as a generator or pump.

		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=HydroEnergyConversionKind\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
