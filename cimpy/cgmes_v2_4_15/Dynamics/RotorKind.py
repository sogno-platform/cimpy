from cimpy.cgmes_v2_4_15.Base import Base


class RotorKind(Base):
	'''
	Type of rotor on physical machine.

		'''

	

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=RotorKind\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
