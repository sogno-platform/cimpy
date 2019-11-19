from cimpy.cimgen_v2_4_15.Base import Base


class VsQpccControlKind(Base):
	'''
	

		'''

	

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=VsQpccControlKind\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
