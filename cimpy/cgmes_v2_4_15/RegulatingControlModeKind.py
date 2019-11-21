from cimpy.cgmes_v2_4_15_flat.Base import Base


class RegulatingControlModeKind(Base):
	'''
	The kind of regulation model.   For example regulating voltage, reactive power, active power, etc.

		'''

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						 }

	readInProfile = {}

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=RegulatingControlModeKind\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
