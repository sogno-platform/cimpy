from cimpy.cgmes_v2_4_15.Base import Base


class String(Base):
	'''
	A string consisting of a sequence of characters. The character encoding is UTF-8. The string length is unspecified and unlimited.

		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DI.value, cgmesProfile.DY.value, cgmesProfile.EQ.value, cgmesProfile.GL.value, cgmesProfile.SV.value, cgmesProfile.SSH.value, cgmesProfile.TP.value, ],
						 }

	readInProfile = {}

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=String\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
