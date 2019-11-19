from cimpy.cimgen_v2_4_15.Base import Base


class SVCControlMode(Base):
	'''
	Static VAr Compensator control mode.

		'''

	

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=SVCControlMode\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
