from .Base import Base


class Integer(Base):
	'''
	An integer number. The range is unspecified and not limited.

		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.GL.value, cgmesProfile.DY.value, cgmesProfile.SSH.value, cgmesProfile.DL.value, cgmesProfile.OP.value, cgmesProfile.EQ.value, cgmesProfile.SC.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=Integer\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
