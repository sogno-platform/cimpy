from cimpy.cgmes_v2_4_15.Base import Base


class DroopSignalFeedbackKind(Base):
	'''
	Governor droop signal feedback source.

		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						 }

	readInProfile = {}

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=DroopSignalFeedbackKind\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
