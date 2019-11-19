from cimpy.cgmes_v2_4_15.Base import Base


class Integer(Base):
	'''
	An integer number. The range is unspecified and not limited.

		'''

	

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=Integer\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
