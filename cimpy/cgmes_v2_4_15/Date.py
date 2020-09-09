from .Base import Base


class Date(Base):
	'''
	Date as "yyyy-mm-dd", which conforms with ISO 8601. UTC time zone is specified as "yyyy-mm-ddZ". A local timezone relative UTC is specified as "yyyy-mm-dd(+/-)hh:mm".

		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DL.value, cgmesProfile.EQ.value, cgmesProfile.SSH.value, cgmesProfile.SV.value, cgmesProfile.GL.value, cgmesProfile.DY.value, cgmesProfile.TP.value, cgmesProfile.TP_BD.value, cgmesProfile.EQ_BD.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=Date\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
