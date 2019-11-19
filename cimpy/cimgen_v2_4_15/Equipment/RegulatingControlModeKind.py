from cimpy.cimgen_v2_4_15.Base import Base


class RegulatingControlModeKind(Base):
	'''
	The kind of regulation model.   For example regulating voltage, reactive power, active power, etc.

		'''

	

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=RegulatingControlModeKind\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
