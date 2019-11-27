from cimpy.cgmes_v2_4_15.Base import Base


class SynchronousMachineOperatingMode(Base):
	'''
	Synchronous machine operating mode.

		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.SSH.value, ],
						 }

	readInProfile = {}

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=SynchronousMachineOperatingMode\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
