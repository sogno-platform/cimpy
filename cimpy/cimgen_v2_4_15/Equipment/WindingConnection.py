from cimpy.cimgen_v2_4_15.Base import Base


class WindingConnection(Base):
	'''
	Winding connection type.

		'''

	

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=WindingConnection\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
