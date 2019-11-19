from cimpy.cgmes_v2_4_15.Base import Base


class UnitSymbol(Base):
	'''
	The units defined for usage in the CIM.

		'''

	

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=UnitSymbol\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
